# importing libraries
import time
import commands
from PIL import ImageGrab
import numpy as np
import cv2

# calibarion to find out where the Region of Intrest ( ROI ) will be in your screen
bb_box = commands.find_roi()

# Lauching the Dino app on Chrome
time.sleep(5)
commands.start_dino_game()

while (True):
    screen = np.array(ImageGrab.grab())
    roi = screen[bb_box[1]:bb_box[3] + bb_box[1], bb_box[0]:bb_box[2] + bb_box[0], :]


    # diff = commands.diff_between_images()

cv2.destroyAllWindows()







































































