


import os
import cv2
import sys


# Set up camera constants
IM_WIDTH = 1280
IM_HEIGHT = 720
#IM_WIDTH = 640    Use smaller resolution for
#IM_HEIGHT = 480   slightly faster framerate

# Select camera type (if user enters --usbcam when calling this script,
# a USB webcam will be used)
camera_type = 'usb'

camera = cv2.VideoCapture(0)

tod_date = date "+%Y-%m-%d"
cv2.imwrite('opencv_img'+ tod_date+'.png',image)
del(camera)
