import win32gui
import sys
import cv2 as cv
from utils import constants as c
from PyQt5.QtWidgets import QApplication
from skimage.metrics import structural_similarity
from PIL import Image
from utils.log import info

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


def game_shot(shape, path):
    """
    游戏窗口内截图
    """
    shot()
    Image.open(c.temp_game).crop(shape).save(path)


def game_template_match(path):
    """
    游戏窗口内模板匹配
    """
    shot()
    return template_match(path, c.temp_game)


def find_xy_in_game(template_path):
    shape, score = game_template_match(template_path)
    info("模板匹配相似度分数:", score)
    if score >= 5:
        x = (shape[0] + shape[2]) // 2
        y = (shape[1] + shape[3]) // 2
        return x, y
    else:
        return None
