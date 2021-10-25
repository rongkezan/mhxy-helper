import win32gui
import util
import sys
import os
import shutil
import constants as c
from PIL import Image
from skimage.metrics import structural_similarity
import cv2 as cv
from PyQt5.QtWidgets import QApplication
import time

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def popup_crop():
    util.log_title('弹窗判断')
    shape, score = template_match(c.popup_flag_img, c.sc_img)
    print(f'弹框提示区域 {shape} 最终得分为 {score}')
    if score >= 3:
        sub_shape = (
            shape[0] + c.popup_move_shape[0],
            shape[1] + c.popup_move_shape[1],
            shape[2] + c.popup_move_shape[2],
            shape[3] + c.popup_move_shape[3]
        )
        print(f'弹框区域  {sub_shape}')
        return crop(c.sc_img, c.popup_img, sub_shape)
    print(f'没有弹框')
    return False


def crop(source_path, target_path, shape):
    Image.open(source_path).crop(shape).save(target_path)
    return True


def template_match(template_path, src_path):
    img = cv.imread(src_path, 0)
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


def shot():
    util.log_title('截图')
    win32gui.EnumWindows(get_all_hwnd, 0)
    title = ''
    for h, t in hwnd_title.items():
        if t.startswith('梦幻西游 ONLINE'):
            title = t
            print(title)
            hwnd = win32gui.FindWindow(None, title)
            app = QApplication(sys.argv)
            desktop_id = app.desktop().winId()
            screen = QApplication.primaryScreen()
            img_desk = screen.grabWindow(desktop_id).toImage()
            img_sc = screen.grabWindow(hwnd).toImage()
            img_desk.save(c.desktop_img)
            img_sc.save(c.sc_img)
            print(f'img_desktop save to -> {os.path.abspath(c.desktop_img)}')
            print(f'img_mhxy save to -> {os.path.abspath(c.sc_img)}')
    if title == '':
        print('mhxy not start')
        return False
    if image_check(c.sc_img, c.screen_size):
        return False
    return True


def image_check(img_path, size):
    util.log_title('截图检查')
    with Image.open(img_path) as img:
        if img.size == size:
            print(f'\t\tsize={size}\t\tok')
            return True
    print('Image Size Error')
    return False


def is_fight():
    util.log_title('战斗状态判断')
    crop(c.sc_img, c.fight_img, c.fight_shape)  # 战斗标识截图
    rate = compare_image(c.fighting_flag_img_path, c.fight_img)
    print(rate)
    if rate > 0.95:
        print('战斗状态')
        return True
    else:
        print('非战斗状态')
        return False


def compare_image(path_image1, path_image2):
    imageA = cv.imread(path_image1)
    imageB = cv.imread(path_image2)
    grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
    grayB = cv.cvtColor(imageB, cv.COLOR_BGR2GRAY)
    score, diff = structural_similarity(grayA, grayB, full=True)
    return score


def crop_4():
    util.log_title('弹窗人物切分')
    w = 90
    h = 120
    for i in range(len(c.crop_4_imgs)):
        shape = (w * i, 0, w * (i + 1), h)
        crop(c.popup_img, os.path.join(c.data_dir, c.crop_4_imgs[i]), shape)


def find_xy_desktop(template_path):
    util.log_title('坐标查找')
    shape, score = template_match(template_path, c.desktop_img)
    if score >= 3:
        x = shape[2] + shape[0]
        y = shape[3] + shape[1]
        print("中心点坐标为:", (x, y))
        return x, y
    print("匹配失败")


def task():
    if shot() & is_fight():
        if popup_crop():
            crop_4()
            return True
    return False