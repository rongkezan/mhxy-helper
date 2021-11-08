import win32gui
import util
import sys
import constants as c
import cv2 as cv
from PIL import Image
from skimage.metrics import structural_similarity
from PyQt5.QtWidgets import QApplication
import numpy as np

hwnd_title = dict()


def __get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def __get_mhxy_hwnd():
    win32gui.EnumWindows(__get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t.startswith('梦幻西游 ONLINE'):
            return h


def get_rect():
    h = __get_mhxy_hwnd()
    return win32gui.GetWindowRect(h)


def shot():
    h = __get_mhxy_hwnd()
    app = QApplication(sys.argv)
    desktop_id = app.desktop().winId()
    screen = QApplication.primaryScreen()
    temp_desktop = screen.grabWindow(desktop_id).toImage()
    temp_game = screen.grabWindow(h).toImage()
    temp_desktop.save(c.temp_desktop)
    temp_game.save(c.temp_game)

