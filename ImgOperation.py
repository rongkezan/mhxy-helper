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


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def shot():
    util.log_title("截图")
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
    score = compare_image(c.flag_fight, c.temp_fight)
    if score > 0.95:
        print('战斗状态')
        return True
    else:
        print('非战斗状态')
        return False


def save_temp_popup():
    util.log_title('弹窗判断')
    shape, score = template_match(c.flag_popup, c.temp_game)
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


def template_match(template_path, img_path):
    img = cv.imread(img_path, 0)
    template = cv.imread(template_path, 0)
    w, h = template.shape[::-1]
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
               'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    shape_dict = {}
    for meth in methods:
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        shape = (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
        if shape_dict.get(shape) is None:
            shape_dict[shape] = 1
        else:
            shape_dict[shape] = shape_dict[shape] + 1
        max_shape = max(shape_dict, key=shape_dict.get)
    return max_shape, shape_dict[max_shape]


def compare_image(img_path1, img_path2):
    imageA = cv.imread(img_path1)
    imageB = cv.imread(img_path2)
    grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
    grayB = cv.cvtColor(imageB, cv.COLOR_BGR2GRAY)
    score, diff = structural_similarity(grayA, grayB, full=True)
    return score


def find_xy_game(template_path):
    shape, score = template_match(template_path, c.temp_game)
    if score >= 3:
        x = (shape[0] + shape[2]) // 2
        y = (shape[1] + shape[3]) // 2
        return x, y
    else:
        return None


def find_mouse_desktop():
    shape, score = template_match(c.flag_mouse, c.temp_desktop)
    if score >= 3:
        x = shape[0]
        y = shape[1]
        return x - 8, y - 8
    else:
        return None


def crop4():
    if shot() & is_fight() & save_temp_popup():
        util.log_title('弹窗人物切分')
        w = 90
        h = 120
        for i in range(len(c.temp_crop4)):
            shape = (w * i, 0, w * (i + 1), h)
            for i in range(len(c.temp_crop4)):
                Image.open(c.temp_popup).crop(shape).save(c.temp_crop4[i])
        return True
    return False
