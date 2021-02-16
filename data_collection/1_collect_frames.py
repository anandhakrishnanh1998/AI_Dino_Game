# This script will save a screenshot when space is pressed.

from PIL import ImageGrab, Image
import commands
import numpy as np
import keyboard
import datetime
import os

##############################################################3

output_file_path = "/home/anandhakrishnanh/Scripts/Dino_Game_Bot/New_Dino/data_collection/frames/"

###############################################################
bb_box = commands.find_roi()

os.mkdir(output_file_path + 'jump/')
os.mkdir(output_file_path + 'dont_jump/')

count = 1
while True:
    screen = np.array(ImageGrab.grab())
    im = Image.fromarray(screen)

    if keyboard.read_key() == "space":
        print("Space Pressed")
        # im = Image.fromarray(screen)

        im.save(output_file_path + '_' + str(datetime.datetime.now()) + '_' + str(count) + '.png')
        count = count + 1

    if keyboard.read_key() == "q":
        break

# the roi should be a rectangle from the left most part to some part after that.
# Convert the images into some border only thing