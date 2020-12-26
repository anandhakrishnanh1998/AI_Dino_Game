# This script will convert whatever video into frames with the correct bounding box
import cv2
from os import listdir
import os
from PIL import ImageGrab

def get_files(folder_path):
    files = [f for f in listdir(folder_path)]
    files = sorted(files)
    return (files)

input_path = "/home/anandhakrishnanh/Scripts/Dino_Game_Bot/data_collection/data/videos/"
output_path = "/home/anandhakrishnanh/Scripts/Dino_Game_Bot/data_collection/data/frames/"

files = get_files(input_path)
print(files)
frame_count = 0



resolution = ImageGrab.grab()
reso = resolution.size

x = int(reso[0] * (266/1920))
y = int(reso[1] * (555/1080))
len_x = int(reso[0] * (177/1920))
len_y = int(reso[1] * (183/1080))

bb_box = [x,y,len_x,len_y]



for i in files:
    video = cv2.VideoCapture(input_path + i)
    while (True):
        ret, frame = video.read()
        frame = frame[bb_box[1]:bb_box[3] + bb_box[1], bb_box[0]:bb_box[2] + bb_box[0], :]

        if ret:
            cv2.imwrite(output_path + str(frame_count) + '.png', frame)
            frame_count += 1
        else:
            break
        frame_count = frame_count + 1
    video.release()
    cv2.destroyAllWindows()
