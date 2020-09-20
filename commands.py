import pyautogui



def start_dino_game():
    pyautogui.keyDown('ctrlleft')
    pyautogui.keyDown('l')
    pyautogui.keyUp('ctrlleft')
    pyautogui.keyUp('l')
    pyautogui.write('chrome://dino')
    pyautogui.press('enter')
    pyautogui.press('space')