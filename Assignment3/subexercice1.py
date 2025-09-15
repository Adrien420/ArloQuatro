# This script shows how to open a camera the picamera2 module and grab frames and show these.
# Kim S. Pedersen, 2023

import cv2 # Import the OpenCV library
import time
from pprint import *
from time import sleep

dragging = False
pt_a = None      # premier point (x,y)
pt_b = None      # point courant ou final

def on_mouse(event, x, y, flags, param):
    global dragging, pt_a, pt_b
    if event == cv2.EVENT_LBUTTONDOWN:
        dragging = True
        pt_a = (x, y)
        pt_b = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and dragging:
        pt_b = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False
        pt_b = (x, y)

def draw_measure(img, a, b):
    # Dessine une ligne + un rectangle englobant et affiche les mesures
    (x1, y1), (x2, y2) = a, b
    dx, dy = x2 - x1, y2 - y1
    dist = int(round((dx*dx + dy*dy) ** 0.5))
    w, h = abs(dx), abs(dy)

    # ligne et points
    cv2.line(img, a, b, (0, 255, 0), 2)
    cv2.circle(img, a, 4, (0, 255, 255), -1)
    cv2.circle(img, b, 4, (0, 255, 255), -1)

    # rectangle (optionnel)
    cv2.rectangle(img, (min(x1,x2), min(y1,y2)), (max(x1,x2), max(y1,y2)), (255, 0, 0), 1)

    # texte
    txt1 = f"dx={dx:+d}px, dy={dy:+d}px"
    txt2 = f"w={w}px, h={h}px"
    txt3 = f"dist={dist}px"
    y0 = 20
    for i, t in enumerate([txt1, txt2, txt3]):
        cv2.putText(img, t, (10, y0 + 18*i), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0,0,0), 3, cv2.LINE_AA)
        cv2.putText(img, t, (10, y0 + 18*i), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255,255,255), 1, cv2.LINE_AA)

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
cv2.setMouseCallback(win, on_mouse)

time.sleep(1)  # wait for camera to setup


# Open a window
WIN_RF = "Example 1"
cv2.namedWindow(WIN_RF)
cv2.moveWindow(WIN_RF, 100, 100)


while cv2.waitKey(4) == -1: # Wait for a key pressed event
    frame = cam.capture_array("main")
    
    disp = frame.copy()

    # Affiche la position de la souris en direct (facultatif)
    # (OpenCV ne donne pas la position sans évènement; on la lit quand on drag)

    # Dessine les mesures si on a des points
    if pt_a is not None and pt_b is not None:
        draw_measure(disp, pt_a, pt_b)

    cv2.imshow(win, disp)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # ESC
        break
    elif k in (ord('c'), ord('C')):
        pt_a = pt_b = None
    

# Finished successfully