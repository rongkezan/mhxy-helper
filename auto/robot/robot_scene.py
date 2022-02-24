"""
场景
"""
from neural.classify.popup_verify import *
from auto.component.action import action
from auto.component.camera import camera


class Scene:
    def __init__(self):
        self.move_around_count = 0
        self.heal_flag = 0

    def move_around(self):
        action.tab()
        if self.move_around_count == 0:
            action.move_left_click(254, 323)
            self.move_around_count = 1
        elif self.move_around_count == 1:
            action.move_left_click(536, 279)
            self.move_around_count = 2
        elif self.move_around_count == 2:
            action.move_left_click(261, 504)
            self.move_around_count = 3
        else:
            action.move_left_click(521, 482)
            self.move_around_count = 1
        action.tab()
        time.sleep(2)

    @staticmethod
    def check_heal():
        log.info("定期检查人物血蓝")
        for t in p.temp_tabs:
            action.move_left_click(t.position[0], t.position[1], True)
            if camera.is_need_heal():
                action.do_heal()

    def run(self):
        log.info("开始刷场景")
        while True:
            self.heal_flag += 1

            while not camera.is_fight():
                if self.heal_flag % 4 == 0:
                    self.check_heal()

                log.info("非战斗状态，晃悠晃悠")
                while not camera.is_leader():
                    log.info("选择队长")
                    action.move_left_click(p.temp_tabs[0].position[0], p.temp_tabs[0].position[1], True)
                self.move_around()

            while camera.is_fight():
                log.info("战斗状态")
                # 弹框验证
                handle_popup()
                # 循环判断是否有通知，有弹窗通知则循环点击保存，直到没有通知退出循环
                while True:
                    notify_xy = camera.is_notify()
                    if notify_xy:
                        log.info("有通知, 坐标:", notify_xy)
                        action.move_left_click(notify_xy[0], notify_xy[1], True)
                        handle_popup()
                    else:
                        break
                # 攻击施法
                if camera.is_ready_fight():
                    action.do_fight5(action.alt_q, action.alt_d)


if __name__ == '__main__':
    Scene().run()
