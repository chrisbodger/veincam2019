#VEINCAM Camera Image Script
#Authored by Alex Ollman for ENGN4221 Engineering Project
#Based on open source code from Miguel Grinberg (October 2014).
#https://blog.miguelgrinberg.com/post/video-streaming-with-flask
#Last Edited 8/10/2018

#import random
import time
import numpy as np
import cv2
import picamera  # Raspberry Pi camera module (requires picamera package)
#from picamera.array import PiRGBArray

from camera_base import BaseCamera

class Camera(BaseCamera):
    video_source = 0
    settings = {}

    # Set sizes for resolution, cropping and region of interest
    # https://picamera.readthedocs.io/en/release-1.13/fov.html
    # https://picamera.readthedocs.io/en/latest/recipes2.html
    """when outputting to unencoded formats, the camera rounds 
        the requested resolution. The horizontal resolution is rounded
        up to the nearest multiple of 32 pixels, while the vertical 
        resolution is rounded up to the nearest multiple of 16 pixels""" 

    # Set sizes for image manipulation
    #res_height, res_width = 1080, 1920
    res_height, res_width = 720, 1280
    fheight = (res_height + 15) // 16 * 16
    fwidth = (res_width + 31) // 32 * 32

    # Crop range
    crpd_height, crpd_width = 640, 600
    crp_hstart = int((fheight/2)-(crpd_height/2))
    crp_hend = int((fheight/2)+(crpd_height/2))
    crp_wstart = int((fwidth/2)-(crpd_width/2))
    crp_wend = int((fwidth/2)+(crpd_width/2))

    # ROI ranges arge - remembering you are now working with the cropped image sizing.
    roil_height, roil_width = 400, 300 # Large 560, 400 ... 220, 320
    rois_height, rois_width = 240, 260 # Small 560, 400 ... 220, 320
    roi_map = {}
    # -- ROI range large
    roil_hstart=int((crpd_height/2)-(roil_height/2))
    roil_hend=int((crpd_height/2)+(roil_height/2))
    roil_wstart=int((crpd_width/2)-(roil_width/2))
    roil_wend=int((crpd_width/2)+(roil_width/2))
    roi_map["Large"] = {"roi_hstart":roil_hstart, "roi_hend":roil_hend, "roi_wstart":roil_wstart, "roi_wend":roil_wend}

    # -- ROI range small
    rois_hstart=int((crpd_height/2)-(rois_height/2))
    rois_hend=int((crpd_height/2)+(rois_height/2))
    rois_wstart=int((crpd_width/2)-(rois_width/2))
    rois_wend=int((crpd_width/2)+(rois_width/2))
    roi_map["Small"] = {"roi_hstart":rois_hstart, "roi_hend":rois_hend, "roi_wstart":rois_wstart, "roi_wend":rois_wend}

    @staticmethod
    def update_settings(settings):
        Camera.settings = settings

    @staticmethod
    def close():
        pass

    @staticmethod
    def set_video_source(source): # Declare picam to be desired camera source. 
        Camera.video_source = source

    @staticmethod
    def frames(): #function used by app.py to retrieve image
        
        # https://picamera.readthedocs.io/en/release-1.13/api_camera.html#picamera
        # brightness, contrast, zoom, awb_mode, exposure_mode, image_denoise, sharpness
        # iso - light sensitivity of camera
        # These changes can be EXPENSIVE, so only adjust if they are different!
        roi_setting = "Off"

        with picamera.PiCamera(
            resolution = (Camera.res_width, Camera.res_height)
            , framerate = 20
        ) as camera:

            # Initiate array to capture greyscale data from a YUV stream
            # https://picamera.readthedocs.io/en/latest/recipes2.html#rapid-capture-and-processing
            # 'the YUV420 format contains 1.5 bytes worth of data for each pixel'
            rawCapture = np.empty(int(Camera.fheight * Camera.fwidth * 1.5), dtype=np.uint8)

            #Let camera warm up
            time.sleep(1)

            for frame in camera.capture_continuous(rawCapture, format="yuv", use_video_port=False):                
                # Acquire the raw NumPy array representing the image, 
                
                # NOTE Operation below is EXPENSIVE - may need to modify if things are too slow
                # An empty dictionary returns false to bool, but true if it contains values
                if bool(Camera.settings):
                    try:
                        if int(camera.contrast) != int(Camera.settings["cam_contrast"]):
                            camera.contrast = int(Camera.settings["cam_contrast"])
                        if int(camera.brightness) != int(Camera.settings["cam_brightness"]):
                            camera.brightness = int(Camera.settings["cam_brightness"])
                        if int(camera.shutter_speed) != (int(Camera.settings["cam_shutspeed"])*10000):
                            # =2/100ths of a second = ~framerate 50
                            camera.shutter_speed = int(Camera.settings["cam_shutspeed"])*10000 
                        roi_setting = Camera.settings["roi"]
                    except:
                        pass

                # Aquire image: save last YUV frame array taken by camera as image, greyscale component only
                img = rawCapture[:Camera.fwidth*Camera.fheight].reshape((Camera.fheight, Camera.fwidth))

                # Uncomment if you want to SAVE FILES for development (slows processing)
                # ALSO uncomment random import above.
                # fname = "test_image%d.jpeg" % random.randint(1,5)
                # cv2.imwrite(fname, img) 
 
                # Crop it. Overwrite to minimise memory use
                img = img[Camera.crp_hstart : Camera.crp_hend, Camera.crp_wstart : Camera.crp_wend] 
                img_final = img.copy()

                if (roi_setting in ("Large","Small")):
                    roi_ranges = Camera.roi_map[roi_setting]

                    # Define and apply filtering to region of interest; 'roi'
                    roi = img[roi_ranges["roi_hstart"] : roi_ranges["roi_hend"], roi_ranges["roi_wstart"] : roi_ranges["roi_wend"]]

                    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(5,5)) # tileGridSize row column
                    roi = clahe.apply(roi)

                    # Overwrite the ROI into a composite final - must use copy of image
                    img_final[roi_ranges["roi_hstart"] : roi_ranges["roi_hend"], roi_ranges["roi_wstart"] : roi_ranges["roi_wend"]] = roi

                # Return augmented image
                yield cv2.imencode('.jpg', img_final)[1].tobytes()
                
                # Clear last frame from camera stream - not using PiRGBArray any more
                #rawCapture.seek(0)
                #rawCapture.truncate()