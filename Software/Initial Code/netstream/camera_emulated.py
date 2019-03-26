# VEINCAM Camera stream emulation script
# Idea from https://blog.miguelgrinberg.com/post/video-streaming-with-flask

# Imports Libraries
import os
import time
import numpy as np
import cv2
from camera_base import BaseCamera
from flask import Flask

# Obtains name of current Module
app = Flask(__name__)


class Camera(BaseCamera):
    cv_images = [cv2.imread(os.path.join(app.static_folder, 'images/testhires/test_image') + suffix + '.jpeg', 0)
                 for suffix in ['1', '2', '3', '4', '5']]

    # Initialises Settings
    settings = {}

    # Sets Sizes For Image Manipulation and Initialises ROI Map
    img_height, img_width = 1920, 1080
    crop_height, crop_width = 1000, 1000
    roi_large_height, roi_large_width = 400, 300
    roi_small_height, roi_small_width = 240, 200
    roi_map = {}

    # Defines Crop Ranges from Centre of Image
    crop_height_start = int((img_height / 2) - (crop_height / 2))
    crop_height_end = crop_height_start + crop_height
    crop_width_start = int((img_width / 2) - (crop_width / 2))
    crop_width_end = crop_width_start + crop_width

    # Defines Large ROI Range from Centre of Cropped Image
    roil_height_start = int((crop_height / 2) - (roi_large_height / 2))
    roil_height_end = roil_height_start + roi_large_height
    roil_width_start = int((crop_width / 2) - (roi_large_width / 2))
    roil_width_end = roil_width_start + roi_large_width
    roi_map["Large"] = {"roi_height_start": roil_height_start, "roi_height_end": roil_height_end,
                        "roi_width_start": roil_width_start, "roi_width_end": roil_width_end}

    # -- ROI range small
    rois_height_start = int((crop_height / 2) - (roi_small_height / 2))
    rois_height_end = rois_height_start + roi_small_height
    rois_width_start = int((crop_width / 2) - (roi_small_width / 2))
    rois_width_end = rois_width_start + roi_small_width
    roi_map["Small"] = {"roi_height_start": rois_height_start, "roi_height_end": rois_height_end,
                        "roi_width_start": rois_width_start, "roi_width_end": rois_width_end}

    @staticmethod
    def update_settings(settings):
        Camera.settings = settings

    @staticmethod
    def close():
        pass

    @staticmethod
    def frames():
        roi_setting = "Off"
        frame_rate = 2
        period = round(1/frame_rate, 4)
        count = 0
        while True:

            time.sleep(period)

            # print('Sent image %d' % (int(time.time()) % 3))
            # print("Contrast set in FRAMES: %d" % Camera.settings["cam_contrast"])
            if bool(Camera.settings):
                try:
                    # print(Camera.settings["cam_contrast"])
                    roi_setting = Camera.settings["roi"]
                except:
                    pass

            # Acquire Image
            img = Camera.cv_images[count]
            print(np.shape(img))
            if count == 4:
                count = 0
            else:
                count += 1

            img = img[Camera.crp_hstart: Camera.crp_hend, Camera.crp_wstart: Camera.crp_wend]
            img_final = img.copy()

            if roi_setting in ("Large", "Small"):
                roi_ranges = Camera.roi_map[roi_setting]
                # Define and apply filtering to region of interest; 'roi'
                # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html
                # tileGridSize row column
                roi = img[roi_ranges["roi_height_start"] : roi_ranges["roi_height_end"], roi_ranges["roi_width_start"] : roi_ranges["roi_wend"]]

                clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(5,5)) # 14 good small window. 400, 300
                roi = clahe.apply(roi)

                #roi = cv2.equalizeHist(roi)
                # TODO add Frangi

                # Overwrite the ROI into a composite final - must use copy of image
                img_final[roi_ranges["roi_hstart"] : roi_ranges["roi_hend"], roi_ranges["roi_wstart"] : roi_ranges["roi_wend"]] = roi

            #-- Ouput
            #yield Camera.imgs[int(time.time()) % 3]
            yield cv2.imencode('.jpg', img_final)[1].tobytes()