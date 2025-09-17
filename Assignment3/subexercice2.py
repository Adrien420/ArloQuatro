# This script shows how to open a camera the picamera2 module and grab frames and show these.
# Kim S. Pedersen, 2023

import cv2 # Import the OpenCV library
import time
from pprint import *
from time import sleep

try:
    import picamera2
    print("Camera.py: Using picamera2 module")
except ImportError:
    print("Camera.py: picamera2 module not available")
    exit(-1)

print("OpenCV version = " + cv2.__version__)

# Open a camera device for capturing
imageSize = (1280, 960)
#imageSize = (1640, 1232)
FPS = 30
cam = picamera2.Picamera2()
frame_duration_limit = int(1/FPS * 1000000) # Microseconds

picam2_config = cam.create_video_configuration({"size": imageSize, "format": 'RGB888'},
                                                            controls={"FrameDurationLimits": (frame_duration_limit, frame_duration_limit),
                                                            "ScalerCrop": (300,1000,3280-1000,2464-1000)},
                                                            queue=False)
cam.configure(picam2_config) # Not really necessary
cam.start(show_preview=False)

pprint(cam.camera_configuration()) # Print the camera configuration in use

win = "Measure (ESC=quit, C=clear)"
cv2.namedWindow(win)

time.sleep(1)  # wait for camera to setup


while cv2.waitKey(4) == -1: # Wait for a key pressed event
    frame = cam.capture_array("main")

    cv2.imshow(win, frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # ESC
        break
    elif k in (ord('c'), ord('C')):
        pt_a = pt_b = None
    

# Finished successfully