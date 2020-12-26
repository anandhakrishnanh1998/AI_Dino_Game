# importing libraries
import time
import commands
from PIL import ImageGrab
import numpy as np
import cv2
from commands import get_files

############################# PATHS #######################################

jump_frames_folder = '/home/anandhakrishnanh/Scripts/Dino_Game_Bot/data_collection/data/jump_frames/'

#############################################################################

# calibarion to find out where the Region of Intrest ( ROI ) will be in your screen
bb_box = commands.find_roi()

# Getting all the images to skip for
files = get_files(jump_frames_folder)
jump_frames = []
for i in files:
    jump_frames.append(cv2.imread(jump_frames_folder + i))
#
# # Lauching the Dino app on Chrome
time.sleep(5)
commands.start_dino_game()
time.sleep(4)

while (True):
    screen = np.array(ImageGrab.grab())
    roi = screen[bb_box[1]:bb_box[3] + bb_box[1], bb_box[0]:bb_box[2] + bb_box[0], :]

    diff = []
    for i in jump_frames:
        diff.append(commands.diff_between_images(roi, i))

    if np.average(diff) >= 20000:
        commands.jump()








































































