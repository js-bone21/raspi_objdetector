


import os
import cv2
import sys
import datetime


# Set up camera constants
IM_WIDTH = 1280
IM_HEIGHT = 720
#IM_WIDTH = 640    Use smaller resolution for
#IM_HEIGHT = 480   slightly faster framerate

# Select camera type (if user enters --usbcam when calling this script,
# a USB webcam will be used)
camera_type = 'usb'

camera = cv2.VideoCapture(0)

# Read from the camera
return_value, image = camera.read()

now = datetime.datetime.now()
# Save the image
# Add this 'now.strftime("%H:%M")' into filename if you wish to add a timestamp to the captured images
cv2.imwrite('/home/pi/Documents/ocvpy/images/opencv_img'+'.png',image)
del(camera)
