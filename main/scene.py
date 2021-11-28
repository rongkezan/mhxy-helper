import shutil
from utils.watcher import *
from utils.action import *

move_around_count = 0


def save_crop4():
    info("战斗出现弹框，保存4小人图片")
    shutil.copy(c.temp_popup, os.path.join(c.data_crop_dir, str(int(round(time.time() * 1000))) + ".png"))


def save_monster():
    temp_path = shot_monster()
    target_path = os.path.join(c.data_monster_dir, str(int(round(time.time() * 1000))) + ".png")
    shutil.copy(temp_path, target_path)


def move_around():
    global move_around_count
    tab()
    if move_around_count == 0:
        move_left_click(129, 339)
        move_around_count = 1
    elif move_around_count == 1:
        move_left_click(139, 403)
        move_around_count = 2
    elif move_around_count == 2:
        move_left_click(196, 343)
        move_around_count = 3
    else:
        move_left_click(197, 397)
        move_around_count = 1
    tab()
    time.sleep(1)


def task():
    load_driver()
    heal_flag = 0
    info("开始刷场景")
    while True:
        heal_flag += 1
        while not is_fight():
            if heal_flag % 4 == 0:
                heal_flag += 1
                info("3轮战斗定期检查人物血蓝")
                for k in c.temp_ch_dict:
                    move_left_click(c.temp_ch_dict[k][2][0], c.temp_ch_dict[k][2][1], True)
                    if is_need_heal():
                        f6()
                        move_left_click(194, 452)

            info("非战斗状态，晃悠晃悠")
            while not is_leader():
                info("选择队长")
                move_left_click(c.temp_ch_dict['ch1'][2][0], c.temp_ch_dict['ch1'][2][1], True)
            move_around()

        shot_popup_flag = 0
        shot_monster_flag = 0
        while is_fight():
            info("战斗状态")

            # 弹框验证
            if shot_popup_flag == 0:
                if is_popup():
                    shot_popup_flag = 1
                    save_crop4()
                # 循环判断是否有通知，有弹窗通知则循环点击保存，直到没有通知退出循环
                while True:
                    notify_xy = is_notify()
                    if notify_xy:
                        info("有通知, 坐标:", notify_xy, "")
                        move_left_click(notify_xy[0], notify_xy[1], True)
                        if is_popup():
                            shot_popup_flag = 1
                            save_crop4()
                    else:
                        break

            # 有弹窗的情况下退出程序
            if shot_popup_flag == 1:
                sys.exit()

            # 怪物截图
            if shot_monster_flag == 0:
                info("截取怪物图片")
                shot_monster_flag = 1
                save_monster()
                # for bb in c.flag_bb:
                #     res = find_xy_in_game(bb)
                #     if res is not None:
                #         x, y = res[0], res[1]
                #         for k in c.temp_ch_dict:
                #             move_left_click(c.temp_ch_dict[k][2][0], c.temp_ch_dict[k][2][1], True)
                #             info("发现目标召唤兽，进行捕捉:", bb)
                #             alt_g()
                #             move_left_click(x, y)
                #             alt_d()

            # 攻击施法
            if is_ready_fight():
                for k in c.temp_ch_dict:
                    move_left_click(c.temp_ch_dict[k][2][0], c.temp_ch_dict[k][2][1], True)
                    info("攻击/施法")
                    alt_q()
                    alt_d()


if __name__ == '__main__':
    task()
