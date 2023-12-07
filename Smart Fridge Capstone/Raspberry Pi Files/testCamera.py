# test hardware

import cv2

from picamera import PiCamera
from time import sleep

# from brightpi import *

camera = PiCamera()
# light = BrightPi()
# special = BrightPiSpecialEffects()

camera.resolution = (640, 480)
camera.rotation = 0

image_path = '/home/pi/tflite1/testCamera.jpg'

# special.set_led_on_off(LED_WHITE, ON)
while(1):
    camera.start_preview()
    sleep(3)
    camera.capture(image_path)
    camera.stop_preview()
    
    image = cv2.imread(image_path)
    cv2.imshow('Camera Test', image)
    
    # Press any key to continue to next image, or press 'q' to quit
    if cv2.waitKey(0) == ord('q'):
        break
# special.set_led_on_off(LED_WHITE, OFF)