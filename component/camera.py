"""
摄像机
用于捕获游戏截图
封装了图片相关的方法: 模板匹配，相似度比对，文字识别(百度API)
"""
import utils.game_rect as game_rect
import sys
import cv2 as cv
import os
import constants.path as p
from PyQt5.QtWidgets import QApplication
from skimage.metrics import structural_similarity
from aip import AipOcr
from PIL import Image
import time

APP_ID = '14495489'
API_KEY = 'MGp1SKRuGUl0EIM8iTSZqs9S'
SECRET_KEY = 'x0a5yBnI7TxQZGwvWA22Mg1s4zPPHdXT'


class Camera:
    def __init__(self):
        self.rect = game_rect.get_mh_rect()
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    @staticmethod
    def shot():
        h = game_rect.get_mh_hwnd()
        app = QApplication(sys.argv)
        desktop_id = app.desktop().winId()
        screen = QApplication.primaryScreen()
        temp_desktop = screen.grabWindow(desktop_id).toImage()
        temp_game = screen.grabWindow(h).toImage()
        temp_desktop.save(p.temp_desktop)
        temp_game.save(p.temp_game)

    @staticmethod
    def template_match(template_path, img_path):
        img = cv.imread(img_path, 0)
        template = cv.imread(template_path, 0)
        w, h = template.shape[::-1]
        methods = [cv.TM_CCOEFF, cv.TM_CCOEFF_NORMED, cv.TM_CCORR, cv.TM_CCORR_NORMED, cv.TM_SQDIFF,
                   cv.TM_SQDIFF_NORMED]
        shape_dict = {}
        for method in methods:
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

    @staticmethod
    def compare_image(img_path1, img_path2):
        gray1 = cv.cvtColor(cv.imread(img_path1), cv.COLOR_BGR2GRAY)
        gray2 = cv.cvtColor(cv.imread(img_path2), cv.COLOR_BGR2GRAY)
        score, diff = structural_similarity(gray1, gray2, full=True)
        return score

    def game_shot(self, shape, path):
        self.shot()
        Image.open(p.temp_game).crop(shape).save(path)

    def read_text_basic(self, filepath):
        with open(filepath, 'rb') as fp:
            img = fp.read()
            result = self.client.basicGeneral(img)
            if 'words_result' in result:
                items = result['words_result']
                words = ""
                for item in items:
                    words += item['words']
                return words
            else:
                return None

    def read_text_accurate(self, filepath):
        with open(filepath, 'rb') as fp:
            img = fp.read()
            result = self.client.basicAccurate(img)
            if 'words_result' in result:
                items = result['words_result']
                words = ""
                for item in items:
                    words += item['words']
                return words
            else:
                return None

    def find_mouse_desktop(self):
        self.shot()
        shape, score = self.template_match(p.flag_mouse, p.temp_game)
        if score >= 3:
            x = self.rect[0] + shape[0] - 9
            y = self.rect[1] + shape[1] - 9
            return x, y
        else:
            return None

    def find_xy_in_game(self, template_path):
        self.shot()
        shape, score = self.template_match(template_path, p.temp_game)
        if score >= 3:
            x = (shape[0] + shape[2]) // 2
            y = (shape[1] + shape[3]) // 2
            return x, y
        else:
            return None

    def shot_monster(self):
        pth = os.path.join(p.temp_dir, "monster.png")
        self.game_shot((100, 100, 510, 415), pth)
        return pth

    def shot_tab(self):
        self.game_shot((20, 33, 780, 53), p.temp_tab_group)
        for t in p.temp_tabs:
            Image.open(p.temp_tab_group).crop(t.shape).save(t.p)

    def is_not_same_crop4(self):
        # 得到最新的一张保存的四小人截图
        files = os.listdir(p.data_crop_dir)
        recent_file = None
        for file in files:
            if recent_file is None:
                recent_file = file
            elif int(str(file).split('.')[0]) > int(str(recent_file).split('.')[0]):
                recent_file = file
        if recent_file is None:
            return True
        # 确认刚截的图不是已经保存过的
        score = self.compare_image(os.path.join(p.data_crop_dir, recent_file), p.temp_popup)
        if score > 0.8:
            print("弹框已保存过，Score:", score)
            return False
        else:
            print("保存弹框，Score:", score)
        return True

    def is_fight(self):
        path1 = os.path.join(p.temp_dir, 'fight_bar.png')
        path2 = os.path.join(p.flag_dir, 'fight_bar.png')
        self.game_shot((795, 190, 805, 430), path1)
        score = self.compare_image(path1, path2)
        return score > 0.95

    def is_ready_fight(self):
        pth = os.path.join(p.flag_dir, "fight_tool.png")
        _, score = self.template_match(pth, p.temp_game)
        return score >= 3

    def is_popup1(self):
        offset_shape = (-107, 28, 97, 130)
        return self._is_popup(offset_shape, p.flag_popup1)

    def is_popup2(self):
        offset_shape = (-46, 29, 174, 130)
        return self._is_popup(offset_shape, p.flag_popup2)

    def _is_popup(self, offset_shape, flag_popup):
        shape, score = self.template_match(flag_popup, p.temp_game)
        if score >= 5:
            x, y = shape[0] + offset_shape[0], shape[1] + offset_shape[1]
            sub_shape = (x, y, x + 360, y + 120)
            self.game_shot(sub_shape, p.temp_popup)
            return sub_shape
        return None

    def is_auto_fight(self):
        path = os.path.join(p.flag_dir, 'fight_auto.png')
        _, score = self.template_match(path, p.temp_game)
        return score >= 3

    def is_need_heal(self):
        self.game_shot((740, 60, 800, 80), os.path.join(p.temp_dir, "status.png"))
        img = cv.imread(p)
        if not (img[15][15][0] == 248):
            return True
        return False

    def is_leader(self):
        self.shot_tab()
        img = cv.imread(p.temp_tabs[0].p)
        return (img[10][115] == [221, 221, 221]).all()

    def is_notify(self):
        self.shot_tab()
        for t in p.temp_tabs:
            img = cv.imread(t.p)
            if (img[10][115] == [149, 203, 253]).all():
                return t.position
        return False

    def is_arrived(self):
        while True:
            shape = (38, 83, 143, 98)
            self.game_shot(shape, p.temp_place1)
            time.sleep(0.5)
            self.game_shot(shape, p.temp_place2)
            score = self.compare_image(p.temp_place1, p.temp_place2)
            if score > 0.99:
                return True
