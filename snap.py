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
        img_path = os.path.join(c.temp_dir, "popup_data.jpg")
        crop(c.sc_img, img_path, sub_shape)
        return img_path
    print(f'没有弹框')


def crop(source_path, target_path, shape):
    with Image.open(source_path) as img:
        img.crop(shape).save(target_path)
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
    crop(c.sc_img, c.fight_img, c.fight_shape) # 战斗标识截图
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
    for i in range(4):
        shape = (w * i, 0, w * (i + 1), h)
        img_name = str((i + 1)) + str(int(round(time.time() * 1000))) + ".jpg"
        crop(c.popup_img, os.path.join(c.data_dir, img_name), shape)


def is_same_fight(img):
    if img is None:
        return True
    # 得到最新的一张保存的四小人截图
    files = os.listdir(c.data_dir)
    recent_file = None
    for file in files:
        if recent_file is None:
            recent_file = file
        elif convert_to_int(file) > convert_to_int(recent_file):
            recent_file = file
    # 确认刚截的图不是已经保存过的
    shape, score = template_match(recent_file, img)
    if score >= 3:
        return False
    return True


def convert_to_int(file_name):
    return int(str(file_name).split('.')[0])


def task():
    if shot() & is_fight():
        temp_img = popup_crop()
        if is_same_fight(temp_img):
            return
        else:
            shutil.copy(os.path.join(c.temp_dir, "popup_data.jpg"),
                        os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".jpg"))


if __name__ == '__main__':
    while True:
        time.sleep(3)
        task()
