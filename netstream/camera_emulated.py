# VEINCAM Camera stream emulation script
# Idea from https://blog.miguelgrinberg.com/post/video-streaming-with-flask
import os
import time
import numpy as np
import cv2

from camera_base import BaseCamera
from flask import Flask

app = Flask(__name__)

class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    imgs = [open(os.path.join(app.static_folder, 'images/testhires/') + 'test_image' + suffix + '.jpeg', 'rb').read() 
        for suffix in ['1', '2', '3', '4', '5']]
    cvimgs = [cv2.imread(os.path.join(app.static_folder, 'images/testhires/test_image') + suffix + '.jpeg', 0) 
        for suffix in ['1', '2', '3', '4', '5']]

    settings = {}

    # Set sizes for image manipulation
    img_height, img_width = 720, 1280

    # Crop range
    crpd_height, crpd_width = 640, 600
    crp_hstart=int((img_height/2)-(crpd_height/2))
    crp_hend=int((img_height/2)+(crpd_height/2))
    crp_wstart=int((img_width/2)-(crpd_width/2))
    crp_wend=int((img_width/2)+(crpd_width/2))

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
    def frames():
        roi_setting = "Off"

        while True:
            time.sleep(1)
            # print('Sent image %d' % (int(time.time()) % 3))
            # print("Contrast set in FRAMES: %d" % Camera.settings["cam_contrast"])
            if bool(Camera.settings):
                try:
                    # print(Camera.settings["cam_contrast"])
                    roi_setting = Camera.settings["roi"]
                except:
                    pass

            # Aquire image
            img = Camera.cvimgs[int(time.time()) % 5]
            # print(Camera.cvimgs[int(time.time()) % 5])

            # Crop it
            # https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
            # We have a 1280,720 image.  Cropping to 640,720 as above
            #crop_img = img[y:y+h, x:x+w], img = img[0:720, 320:960]
            img = img[Camera.crp_hstart : Camera.crp_hend, Camera.crp_wstart : Camera.crp_wend] # Crop it. Overwrite to minimise memory use
            img_final = img.copy()

            if (roi_setting in ("Large","Small")):
                roi_ranges = Camera.roi_map[roi_setting]
                # Define and apply filtering to region of interest; 'roi'
                # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html
                # tileGridSize row column
                roi = img[roi_ranges["roi_hstart"] : roi_ranges["roi_hend"], roi_ranges["roi_wstart"] : roi_ranges["roi_wend"]]

                clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(5,5)) # 14 good small window. 400, 300
                roi = clahe.apply(roi)

                #roi = cv2.equalizeHist(roi)
                # TODO add Frangi

                # Overwrite the ROI into a composite final - must use copy of image
                img_final[roi_ranges["roi_hstart"] : roi_ranges["roi_hend"], roi_ranges["roi_wstart"] : roi_ranges["roi_wend"]] = roi

            #-- Ouput
            #yield Camera.imgs[int(time.time()) % 3]
            yield cv2.imencode('.jpg', img_final)[1].tobytes()