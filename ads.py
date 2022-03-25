import time

import pyautogui

import schedule

from pygame import mixer

adsTimeInterval = (int(input('De quanto em quantos minutos?')))


def start_python_code():
    pyautogui.press('playpause')
    mixer.init()
    mixer.music.load('audio.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    pyautogui.press('playpause')


start_python_code()
schedule.every(adsTimeInterval).minutes.do(
    start_python_code)
while 1:
    schedule.run_pending()
    time.sleep(1)
