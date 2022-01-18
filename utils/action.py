"""
鼠标: 用于对游戏进行操作，包括鼠标点击、键盘按键
"""
from ctypes import windll
import pyautogui
import time
import utils.game_rect as game_rect
import constants as c
import utils.camera as camera
import utils.log as log


class Action:
    def __init__(self):
        self.driver = windll.LoadLibrary(c.dd_dll_path)
        self.rect = game_rect.get_mh_rect()
        self.camera = camera.Camera()
        st = self.driver.DD_btn(0)
        if st == 1:
            print("DD Load Success!")
        else:
            print("DD Load Failed!")
            exit(101)

    def left_click(self):
        self.driver.DD_btn(1)
        time.sleep(0.01)
        self.driver.DD_btn(2)

    def right_click(self):
        self.driver.DD_btn(4)
        time.sleep(0.01)
        self.driver.DD_btn(8)

    def keyboard1(self, code):
        self.driver.DD_key(code, 1)
        time.sleep(0.01)
        self.driver.DD_key(code, 2)

    def keyboard2(self, code1, code2):
        self.driver.DD_key(code1, 1)
        self.driver.DD_key(code2, 1)
        time.sleep(0.01)
        self.driver.DD_key(code2, 2)
        time.sleep(0.01)
        self.driver.DD_key(code1, 2)

    def move_game(self, x, y):
        x_target, y_target = self.move_direct(x, y)
        time.sleep(0.1)
        xy_mouse = self.camera.find_mouse_desktop()
        if xy_mouse is not None:
            time.sleep(0.1)
            x_rel = x_target - xy_mouse[0]
            y_rel = y_target - xy_mouse[1]
            pyautogui.moveRel(x_rel, y_rel, 0.1)
            xy_mouse = self.camera.find_mouse_desktop()
            if xy_mouse is not None:
                time.sleep(0.1)
                x_rel = x_target - xy_mouse[0]
                y_rel = y_target - xy_mouse[1]
                pyautogui.moveRel(x_rel, y_rel, 0.1)

    def move_direct(self, x, y):
        x_target = self.rect[0] + x
        y_target = self.rect[1] + y
        pyautogui.moveTo(x_target, y_target, 0.1)
        return x_target, y_target

    def move_left_click(self, x, y, direct=False):
        if direct:
            self.move_direct(x, y)
        else:
            self.move_game(x, y)
        self.left_click()
        time.sleep(0.1)

    def move_right_click(self, x, y, direct=False):
        if direct:
            self.move_direct(x, y)
        else:
            self.move_game(x, y)
        self.right_click()
        time.sleep(0.1)

    def alt_q(self):
        self.keyboard2(604, 301)
        time.sleep(0.1)

    def alt_a(self):
        self.keyboard2(604, 401)
        time.sleep(0.1)

    def alt_e(self):
        self.keyboard2(604, 303)
        time.sleep(0.1)

    def alt_d(self):
        self.keyboard2(604, 403)
        time.sleep(0.1)

    def alt_g(self):
        self.keyboard2(604, 405)
        time.sleep(0.1)

    def alt_h(self):
        self.keyboard2(604, 406)
        time.sleep(0.1)

    def tab(self):
        self.keyboard1(300)
        time.sleep(0.1)

    def f9(self):
        self.keyboard1(109)
        time.sleep(0.1)

    def f6(self):
        self.keyboard1(106)
        time.sleep(0.1)

    def do_find_npc(self, npc):
        name, paths = npc[0], npc[1]
        self.do_hide()
        while True:
            time.sleep(0.1)
            log.info("寻找" + name + "中...")
            found = False
            for path in paths:
                result = self.camera.find_xy_in_game(path)
                if result is not None:
                    found = True
                    x, y = result[0], result[1]
                    log.info("找到" + name + "，位置:", x, y)
                    self.move_left_click(x, y)
                    break
            if found:
                log.info("已找到" + name + "，退出寻找")
                break
            else:
                log.info("未找到" + name + "，继续寻找")
                time.sleep(5)
                self.do_hide()

    def do_hide(self):
        log.info("隐藏人物和摊位")
        self.f9()
        self.alt_h()

    def do_heal(self):
        log.info("酒肆")
        self.f6()
        self.move_left_click(194, 452)

    def do_fight(self, action1=alt_q, action2=alt_q):
        """
        action1: 人物操作 q-施法 a-攻击 d-防御
        action2: 宠物操作 q-施法 a-攻击 d-防御
        """
        log.info("攻击/施法")
        action1()
        action2()

    def do_fight5(self, action1=alt_q, action2=alt_q):
        """
        action1: 人物操作 q-施法 a-攻击 d-防御
        action2: 宠物操作 q-施法 a-攻击 d-防御
        """
        for t in c.temp_tabs:
            self.move_left_click(t.position[0], t.position[1], True)
            log.info("攻击/施法")
            action1()
            action2()
