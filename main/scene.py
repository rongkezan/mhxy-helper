import shutil
from utils.map import *

hwnd_title = dict()
move_around_count = 0


def save_crop4():
    # if is_not_same_crop4():
    shutil.copy(c.temp_popup, os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".png"))


def save_monster():
    shot_monster()
    # if is_not_same_monster():
    shutil.copy(os.path.join(c.temp_dir, "monster.png"), os.path.join(c.data_dir + "monster/", str(int(round(time.time() * 1000))) + ".png"))


def move_around():
    global move_around_count
    tab()
    if move_around_count == 0:
        move_left_click(254, 323)
        move_around_count = 1
    elif move_around_count == 1:
        move_left_click(536, 279)
        move_around_count = 2
    elif move_around_count == 2:
        move_left_click(261, 504)
        move_around_count = 3
    else:
        move_left_click(521, 482)
        move_around_count = 1
    tab()


def task():
    load_driver()
    heal_flag = 1
    print(">>> 开始刷场景 >>>")
    while True:
        print(">>> 状态判断 >>>")
        while not is_fight():
            if heal_flag % 5 == 0:
                print(">>> 10轮战斗定期检查人物血蓝 >>>")
                heal_flag += 1
                for k in c.ch_dict:
                    move_left_click(c.ch_dict[k][2][0], c.ch_dict[k][2][1], True)
                    if is_need_heal():
                        f6()
                        move_left_click(194, 452)

            print(">>> 非战斗状态，晃悠晃悠 >>>")
            while not leader_is_active():
                print(">>> 选择队长 >>>")
                move_left_click(c.ch_dict['ch1'][2][0], c.ch_dict['ch1'][2][1], True)
            if arrived():
                move_around()

        need_shot_popup1 = 0
        need_shot_popup2 = 0
        shot_monster_flag = 0
        while is_fight():
            print(">>> 战斗状态 >>>")

            # 识别队长是否有4小人弹窗
            if need_shot_popup1 == 0:
                need_shot_popup1 = 1
                if is_popup():
                    print(">>> 战斗出现弹框，保存4小人图片 >>>")
                    save_crop4()
                    sys.exit()
            # 识别队员是否有4小人弹窗
            if need_shot_popup2 == 0:
                need_shot_popup2 = 1
                notify_xy = is_notify()
                while notify_xy:
                    time.sleep(1)
                    print(">>> 有通知, 坐标:", notify_xy, " >>>")
                    move_left_click(notify_xy[0], notify_xy[1], True)
                    if is_popup():
                        print(">>> 战斗出现弹框，保存4小人图片 >>>")
                        save_crop4()
                        sys.exit()
                    else:
                        break
            # 怪物截图
            if shot_monster_flag == 0:
                print(">>> 截取怪物图片 >>>")
                shot_monster_flag = 1
                save_monster()
            # 攻击施法
            if is_ready_fight():
                for k in c.ch_dict:
                    move_left_click(c.ch_dict[k][2][0], c.ch_dict[k][2][1], True)
                    print(">>> 攻击/施法 >>>")
                    alt_q()
                    alt_d()
            time.sleep(1)


if __name__ == '__main__':
    task()
