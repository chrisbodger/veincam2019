# Import Libraries
import io
import threading
import time
from _thread import get_ident

import cv2
import numpy as np
import picamera


class CameraEvent:
    """An Event-like class that signals all active clients when a new frame is available."""
    def __init__(self):
        self.events = {}

    def wait(self):
        """Invoked from each client's thread to wait for the next frame."""
        ident = get_ident()
        if ident not in self.events:
            self.events[ident] = [threading.Event(), time.time()]
        return self.events[ident][0].wait()

    def set(self):
        """Invoked by the camera thread when a new frame is available."""
        now = time.time()
        remove = None
        for ident, event in self.events.items():
            if not event[0].isSet():
                event[0].set()
                event[1] = now
            else:
                if now - event[1] > 3:
                    remove = ident
        if remove:
            del self.events[remove]

    def clear(self):
        """Invoked from each client's thread after a frame was processed."""
        self.events[get_ident()][0].clear()


class BaseCamera:
    thread = None
    frame = None
    last_access = 0
    event = CameraEvent()

    def __init__(self):
        if BaseCamera.thread is None:
            BaseCamera.last_access = time.time()
            BaseCamera.thread = threading.Thread(target=self._thread)
            BaseCamera.thread.start()
            BaseCamera.test = io.BytesIO()
            print(type(BaseCamera.test))
            BaseCamera.bytes = bytes(BaseCamera.test)
            print(type(BaseCamera.bytes))

            while self.get_frame() is None:
                time.sleep(0)

    def get_frame(self):
        BaseCamera.last_access = time.time()
        BaseCamera.event.wait()
        BaseCamera.event.clear()
        return BaseCamera.frame

    @staticmethod
    def frames():
        raise RuntimeError('Must be implemented by subclasses.')

    @classmethod
    def _thread(cls):
        print('Starting Camera Thread.')
        frames_iterator = cls.frames()
        for frame in frames_iterator:
            print(np.shape(list(frame)))
            BaseCamera.frame = frame
            BaseCamera.event.set()
            time.sleep(0)
            if time.time() - BaseCamera.last_access > 2:
                frames_iterator.close()
                print('Stopping camera thread due to inactivity.')
                break
        BaseCamera.thread = None


class StreamOutput():
    def __init__(self):
        self.frame = None
        self.stream = io.BytesIO()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self.frame = self.stream.seek(0)


class Camera:

    def __init__(self, settings_cache):
        self.settings = settings_cache
        self.res_height = 720
        self.res_width = 1280
        self.crop = self.crop_size(600, 600)
        self.roi = np.zeros([2, 4])
        self.roi[0] = self.crop_size(400, 400)
        self.roi[1] = self.crop_size(250, 250)

    def crop_size(self, w, h):
        crop_points = []
        crop_points.append(int((self.res_height/2) - (h/2)))
        crop_points.append(crop_points[0] + h)
        crop_points.append(int((self.res_width / 2) - (w / 2)))
        crop_points.append(crop_points[2] + w)
        return np.array(crop_points)

    def update_settings(self):
        try:
            self.roi_setting = self.settings["roi"]
            if int(picamera.contrast) != int(self.settings["cam_contrast"]):
                picamera.contrast = int(self.settings["cam_contrast"])
            if int(picamera.brightness) != int(self.settings["cam_brightness"]):
                picamera.brightness = int(self.settings["cam_brightness"])
        except KeyError:
            print('no entry under that name')

    def frames(self):
        with picamera.PiCamera(resolution=(self.res_width, self.res_height)) as picamera:
            time.sleep(1)
            output = StreamOutput()
            picamera.start_recording(output, format='mjpeg')
            picamera.rotation = 180
            try:
                while True:
                    try:
                        if output.frame is not None:
                            string_array = np.fromstring(output.frame, np.uint8)
                        if np.shape(string_array)[0] > 0:
                            img = cv2.imdecode(string_array, cv2.IMREAD_GRAYSCALE)

                        self.update_settings()

                        img = img[self.crop[0]:self.crop[1], self.crop[2]:self.crop[3]]
                        img_final = img.copy()

                        if self.roi_setting == "Large":
                            roi_index = 0
                        elif self.roi_setting == "Small":
                            roi_index = 1

                        if self.roi_setting in ("Large", "Small"):
                            roi_img = img[self.roi[roi_index][0]: self.roi[roi_index][1], self.roi[roi_index][2]: self.roi[roi_index][3]]
                            clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(5, 5))
                            roi_img = clahe.apply(roi_img)
                            img_final[self.roi[roi_index][0]: self.roi[roi_index][1], self.roi[roi_index][2]: self.roi[roi_index][3]] = roi_img
                        yield cv2.imencode('.jpg', img_final)[1].tobytes()
                    except GeneratorExit:
                        return
                    except UnboundLocalError:
                        pass
                    except cv2.error:
                        pass
            finally:
                picamera.stop_recording()
