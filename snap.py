# import win32gui
import util
import sys
import os
import constants as c
from PIL import Image
from skimage.metrics import structural_similarity
import cv2 as cv
from PyQt5.QtWidgets import QApplication

hwnd_title = dict()


# def get_all_hwnd(hwnd, mouse):
#     if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
#         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def fight_crop():
    util.log_title('战斗标识截图')
    return crop(c.img_sc_path, c.fighting_img_path, c.fight_shape)


def popup_crop():
    util.log_title('弹窗判断')
    shape_dict = {}
    for i in range(len(c.popup_flag_img_paths)):
        shape, score = template_match(c.popup_flag_img_paths[i], c.img_sc_path)
        shape_dict[shape] = (score, i)

    print(shape_dict)
    max_shape = max(shape_dict, key=shape_dict.get)
    score, i = shape_dict[max_shape]
    print(f'最大区域 {max_shape} 最终得分为 {score}')
    if score >= 3:
        sub_shape = (
            max_shape[0] + c.popup_move_shapes[i][0],
            max_shape[1] + c.popup_move_shapes[i][1],
            max_shape[2] + c.popup_move_shapes[i][2],
            max_shape[3] + c.popup_move_shapes[i][3]
        )
        print(f'弹框区域  {sub_shape}')
        return crop(c.img_sc_path, c.popup_sub_img_path, sub_shape)
    print(f'没有弹框')
    return False


def crop(source_path, target_path, shape):
    with Image.open(source_path) as img:
        fighting_flag_img = img.crop(shape)
        fighting_flag_img.save(target_path)
        return True


def template_match(template_path, src_path):
    img = cv.imread(src_path, 0)
    img2 = img.copy()
    template = cv.imread(template_path, 0)
    w, h = template.shape[::-1]
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
               'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    shape_dict = {}
    for meth in methods:
        img = img2.copy()
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


# def shot():
#     util.log_title('截图')
#     win32gui.EnumWindows(get_all_hwnd, 0)
#     title = ''
#     for h, t in hwnd_title.items():
#         if t.startswith('梦幻西游 ONLINE'):
#             title = t
#             print(title)
#             hwnd = win32gui.FindWindow(None, title)
#             app = QApplication(sys.argv)
#             desktop_id = app.desktop().winId()
#             screen = QApplication.primaryScreen()
#             img_desk = screen.grabWindow(desktop_id).toImage()
#             img_sc = screen.grabWindow(hwnd).toImage()
#             img_desk.save(c.img_desktop_path)
#             img_sc.save(c.img_sc_path)
#             print(f'img_desktop save to -> {os.path.abspath(c.img_desktop_path)}')
#             print(f'img_mhxy save to -> {os.path.abspath(c.img_sc_path)}')
#     if title == '':
#         print('mhxy not start')
#         return False
#     return True


def image_check(img_path, size):
    util.log_title('截图检查')
    with Image.open(img_path) as img:
        if img.size == size:
            print(f'\t\tsize={size}\t\tok')
            return True
    print('Image Size Error')
    return False


def is_fight():
    util.log_title('状态判断')
    rate = compare_image(c.fighting_flag_img_path, c.fighting_img_path)
    if rate > 0.95:
        print('战斗 状态')
        return True
    else:
        print('非战斗 状态')
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
    for i in range(len(c.crop_4_img_names)):
        shape = (w * i, 0, w * (i + 1), h)
        crop(c.popup_sub_img_path, c.crop_4_img_paths[i], shape)


def locate(screen, wanted, show=0):
    loc_pos = []


if __name__ == '__main__':
    shape, score = template_match(r'images/flag/popup_flag_1.jpg', r'images/flag/1.png')
    print(shape, score)
    # if shot():  # 截图
    #     if image_check(c.img_sc_path, c.screen_size):  # 检查截图大小
    #         fight_crop()  # 战斗标识截图
    #         if is_fight():  # 判断是否在战斗
    #             if popup_sub_crop():  # 弹窗识别 与 人物区域切出
    #                 if image_check(c.popup_sub_img_path, c.sub_size):  # 弹窗人物截图检查
    #                     crop_4()  # 弹窗人物切分
    #                     print()
