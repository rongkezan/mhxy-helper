"""
场景
"""
import constants.path as p
import keyboard
import sys
from neural.classify.popup_verify import *
from auto.component.action import action
from auto.component.camera import camera


def run():
    log.info("开始刷场景")
    while True:
        time.sleep(0.5)
        log.info("检测中...")
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


def stop():
    sys.exit()


if __name__ == '__main__':
    keyboard.add_hotkey('f11', run)
    keyboard.add_hotkey('f12', stop)
    keyboard.wait()
    run()
