import win32gui
import util
import sys
import constants as c
import cv2 as cv
from PIL import Image
from skimage.metrics import structural_similarity
from PyQt5.QtWidgets import QApplication
import numpy as np
import time
from ImgOperation import *
from Auto import *

hwnd_title = dict()
rect = None


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def shot():
    global rect
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t.startswith('梦幻西游 ONLINE'):
            app = QApplication(sys.argv)
            desktop_id = app.desktop().winId()
            screen = QApplication.primaryScreen()
            temp_desktop = screen.grabWindow(desktop_id).toImage()
            temp_game = screen.grabWindow(h).toImage()
            temp_desktop.save(c.temp_desktop)
            temp_game.save(c.temp_game)
            rect = win32gui.GetWindowRect(h)


def save_temp_ch():
    shot()
    Image.open(c.temp_game).crop((20, 33, 780, 53)).save(c.ch_temp_img)
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch1'][0]).save(c.ch_dict['ch1'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch2'][0]).save(c.ch_dict['ch2'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch3'][0]).save(c.ch_dict['ch3'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch4'][0]).save(c.ch_dict['ch4'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch5'][0]).save(c.ch_dict['ch5'][1])


if __name__ == '__main__':
    load_driver()
    while True:
        print(">>> 检测人物框通知 >>>")
        time.sleep(1)
        save_temp_ch()
        for k in c.ch_dict:
            img = cv.imread(c.ch_dict[k][1])
            if (img[10][115] == [155, 202, 254]).all():
                print(">>> 通知点击坐标: ", c.ch_dict[k][2], " >>>")
                move_left_click(rect, c.ch_dict[k][2][0], c.ch_dict[k][2][1], True)
