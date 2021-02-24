# This script will tell the speed at which the obstacles are moving.

# importing libraries
import cv2
from commands import find_roi
from PIL import ImageGrab
import numpy as np

# useful functions



bb_box = find_roi()

while(True):
    screen = np.array(ImageGrab.grab())
    roi = screen[bb_box[1]:bb_box[3] + bb_box[1], bb_box[0]:bb_box[2] + bb_box[0], :]
    cv2.imshow('test',roi)
    cv2.waitKey(0)

