import win32gui
import sys
import constants as c
from PyQt5.QtWidgets import QApplication
import cv2 as cv
from PIL import Image

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
    """
    游戏窗口及桌面截图
    """
    h = __get_mhxy_hwnd()
    app = QApplication(sys.argv)
    desktop_id = app.desktop().winId()
    screen = QApplication.primaryScreen()
    temp_desktop = screen.grabWindow(desktop_id).toImage()
    temp_game = screen.grabWindow(h).toImage()
    temp_desktop.save(c.temp_desktop)
    temp_game.save(c.temp_game)


def shot_monster():
    """
    怪物截图
    """
    shot()
    Image.open(c.temp_game).crop((0, 100, 550, 400)).save("img/temp/monster.png")


def shot_tag():
    """
    人物标签截图
    """
    shot()
    Image.open(c.temp_game).crop((20, 33, 780, 53)).save(c.ch_temp_img)
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch1'][0]).save(c.ch_dict['ch1'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch2'][0]).save(c.ch_dict['ch2'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch3'][0]).save(c.ch_dict['ch3'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch4'][0]).save(c.ch_dict['ch4'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch5'][0]).save(c.ch_dict['ch5'][1])


def shot_status():
    """
    人物状态截图
    """
    shot()
    Image.open(c.temp_game).crop((740, 60, 800, 80)).save("img/temp/status.png")


def shot_fight_tool():
    """
    战斗工具栏截图
    """
    shot()
    path = "img/temp/fight_tool.png"
    Image.open(c.temp_game).crop((673, 220, 735, 300)).save(path)
    return path


if __name__ == '__main__':
    shot_monster()
