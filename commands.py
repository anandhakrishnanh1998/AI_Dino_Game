import pyautogui
import os
from PIL import ImageGrab
import numpy as np


def start_dino_game():
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('l')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyUp('l')
    pyautogui.write('chrome://dino')
    pyautogui.press('enter')
    pyautogui.press('space')

def jump():
    pyautogui.press('up')

def dunk():
    pyautogui.press('down')

def find_roi():
    resolution = ImageGrab.grab()
    reso = resolution.size
    x = int(reso[0] * (266 / 1920))
    y = int(reso[1] * (555 / 1080))
    len_x = int(reso[0] * (177 / 1920))
    len_y = int(reso[1] * (183 / 1080))
    bb_box = [x, y, len_x, len_y]
    return bb_box

def diff_between_images(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err
