"""
场景
"""
from learn.popup_verify import *
from utils.action import Action
from utils.camera import Camera


class Scene:
    def __init__(self):
        self.move_around_count = 0
        self.action = Action()
        self.camera = Camera()

    def move_around(self):
        self.action.tab()
        if self.move_around_count == 0:
            self.action.move_left_click(254, 323)
            self.move_around_count = 1
        elif self.move_around_count == 1:
            self.action.move_left_click(536, 279)
            self.move_around_count = 2
        elif self.move_around_count == 2:
            self.action.move_left_click(261, 504)
            self.move_around_count = 3
        else:
            self.action.move_left_click(521, 482)
            self.move_around_count = 1
        self.action.tab()
        time.sleep(1)

    def check_heal(self):
        info("定期检查人物血蓝")
        for t in c.temp_tabs:
            self.action.move_left_click(t.position[0], t.position[1], True)
            if self.camera.is_need_heal():
                self.action.do_heal()

    def run(self):
        info("开始刷场景")
        heal_flag = 0
        while True:
            heal_flag += 1
            while not self.camera.is_fight():
                if heal_flag % 4 == 0:
                    heal_flag += 1
                    self.check_heal()

                info("非战斗状态，晃悠晃悠")
                while not self.camera.is_leader():
                    info("选择队长")
                    self.action.move_left_click(c.temp_tabs[0].position[0], c.temp_tabs[0].position[1], True)
                self.move_around()

            while self.camera.is_fight():
                info("战斗状态")

                # 弹框验证
                handle_popup()
                # 循环判断是否有通知，有弹窗通知则循环点击保存，直到没有通知退出循环
                while True:
                    notify_xy = self.camera.is_notify()
                    if notify_xy:
                        info("有通知, 坐标:", notify_xy, "")
                        self.action.move_left_click(notify_xy[0], notify_xy[1], True)
                        handle_popup()
                    else:
                        break

                # 攻击施法
                if self.camera.is_ready_fight():
                    self.action.do_fight5(alt_q, alt_d)

