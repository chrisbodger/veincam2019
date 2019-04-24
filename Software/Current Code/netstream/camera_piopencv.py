# Import Libraries
import io
import threading
import time
from _thread import get_ident

import cv2
import numpy as np
import picamera


class CameraEvent:
    """The Event class which signals main script when a new camera frame is available"""
    def __init__(self):
        self.events = {}

    def wait(self):
        ident = get_ident()
        if ident not in self.events:
            self.events[ident] = [threading.Event(), time.time()]
        return self.events[ident][0].wait()

    def set(self):
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
        self.events[get_ident()][0].clear()


class StreamOutput:
    """Defines how the MJPEG stream writes to the buffer and splits each frame"""
    def __init__(self):
        self.frame = None
        self.stream = io.BytesIO()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self.stream.seek(0)
            self.frame = self.stream.getvalue()
            self.stream.truncate()
            self.stream.seek(0)
        return self.stream.write(buf)


class Camera:
    """Obtains image, stores camera settings and performs image processing"""
    def __init__(self, settings_cache):
        self.settings = settings_cache

        # calculates crop and roi sizes
        self.res_height = 720
        self.res_width = 1280
        self.crop = self.crop_size(600, 600, self.res_height, self.res_width)
        self.roi = np.zeros([2, 4])
        self.roi[0] = self.crop_size(400, 400, 600, 600)
        self.roi[1] = self.crop_size(250, 250, 600, 600)
        self.roi = self.roi.astype(int)

        # starts camera thread and initiates event class
        self.thread = threading.Thread(target=self._thread)
        self.thread.start()
        self.event = CameraEvent()

    def crop_size(self, h, w, rh, rw):
        crop_points = []
        crop_points.append(int((rh / 2) - (h / 2)))
        crop_points.append(crop_points[0] + h)
        crop_points.append(int((rw / 2) - (w / 2)))
        crop_points.append(crop_points[2] + w)
        return np.array(crop_points)

    def update_settings(self):
        try:
            self.roi_setting = self.settings["roi"]
            if int(picamera.contrast) != int(self.settings["cam_contrast"]):
                picamera.contrast = int(self.settings["cam_contrast"])
        except KeyError:
            print('No setting of that name currently in json file')

    def get_frame(self):
        self.event.wait()
        self.event.clear()
        return self.frame

    def _thread(self):
        print('Starting Camera Thread')
        frames_iterator = self.frames()
        for frame in frames_iterator:
            self.frame = frame
            self.event.set()
            if bool(self.settings):
                if not self.settings["cam_state"]:
                    print('Stopping Camera Thread')
                    break

    def frames(self):
        with picamera.PiCamera(resolution=(self.res_width, self.res_height)) as self.pi_camera:
            time.sleep(1)
            output = StreamOutput()
            self.pi_camera.start_recording(output, format='mjpeg')
            self.pi_camera.rotation = 180
            try:
                while True:
                    try:
                        # if statements used to suppress initial OpenCV warnings
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
                            roi_img = img[self.roi[roi_index][0]: self.roi[roi_index][1],
                                          self.roi[roi_index][2]: self.roi[roi_index][3]]

                            hist_eq = cv2.createCLAHE(clipLimit=6.0, tileGridSize=(6, 6))
                            roi_img = hist_eq.apply(roi_img)

                            img_final[self.roi[roi_index][0]: self.roi[roi_index][1],
                                      self.roi[roi_index][2]: self.roi[roi_index][3]] = roi_img

                        yield cv2.imencode('.jpg', img_final)[1].tobytes()
                    except GeneratorExit:
                        return
                    except UnboundLocalError:
                        pass
                    except cv2.error:
                        pass
            finally:
                self.pi_camera.stop_recording()
