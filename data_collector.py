import win32gui
import util
import sys
import os
import shutil
import constants as c
from PIL import Image
from PyQt5.QtWidgets import QApplication
import time

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def shot():
    win32gui.EnumWindows(get_all_hwnd, 0)
    title = ''
    for h, t in hwnd_title.items():
        if t.startswith('梦幻西游 ONLINE'):
            title = t
            hwnd = win32gui.FindWindow(None, title)
            app = QApplication(sys.argv)
            desktop_id = app.desktop().winId()
            screen = QApplication.primaryScreen()
            temp_desktop = screen.grabWindow(desktop_id).toImage()
            temp_game = screen.grabWindow(hwnd).toImage()
            temp_desktop.save(c.temp_desktop)
            temp_game.save(c.temp_game)
    if title == '':
        print('MHXY not started.')
        return False
    return True


def is_fight():
    util.log_title('战斗状态判断')
    Image.open(c.temp_game).crop(c.fight_shape).save(c.temp_fight)
    score = util.compare_image(c.flag_fight, c.temp_fight)
    if score > 0.95:
        print('战斗状态')
        return True
    else:
        print('非战斗状态')
        return False


def save_temp_popup():
    util.log_title('弹窗判断')
    shape, score = util.template_match(c.flag_popup, c.temp_game)
    print(f'弹框提示区域 {shape} 最终得分为 {score}')
    if score >= 3:
        sub_shape = (
            shape[0] + c.popup_move_shape[0],
            shape[1] + c.popup_move_shape[1],
            shape[2] + c.popup_move_shape[2],
            shape[3] + c.popup_move_shape[3]
        )
        print(f'四小人区域  {sub_shape}')
        Image.open(c.temp_game).crop(sub_shape).save(c.temp_popup)
        return True
    print(f'没有弹框')
    return False


def is_not_same_fight():
    # 得到最新的一张保存的四小人截图
    files = os.listdir(c.data_dir)
    recent_file = None
    for file in files:
        if recent_file is None:
            recent_file = file
        elif convert_to_int(file) > convert_to_int(recent_file):
            recent_file = file
    if recent_file is None:
        return True
    # 确认刚截的图不是已经保存过的
    score = util.compare_image(os.path.join(c.data_dir, recent_file), c.temp_popup)
    if score > 0.9:
        return False
    return True


def convert_to_int(file_name):
    return int(str(file_name).split('.')[0])


def task():
    if shot() & is_fight() & save_temp_popup() & is_not_same_fight():
        shutil.copy(c.temp_popup, os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".jpg"))


if __name__ == '__main__':
    while True:
        time.sleep(3)
        task()
