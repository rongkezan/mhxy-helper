from utils.game_action import *
from utils.game_watcher import *
from utils.map import Map
from utils.bag import Bag
from utils.mission import Mission
import shutil

npc_list = ["秦琼", "程咬金", "空度禅师", "孙婆婆", "东海龙王", "地藏王", "观音姐姐", "镇元大仙", "牛魔王",
                   "大大王", "二大王", "三大王", "杨戬", "李靖", "菩提祖师", "白晶晶", "花十娘"]
bag = Bag()
mission = Mission()
map = Map()


def get_mission():
    bag.right_click(5, 1)  # 点击导标旗
    move_left_click(647, 342)  # 导标旗点击镖局
    move_left_click(484, 280)  # 进入镖局
    move_left_click(688, 303)  # 走向镖头
    time.sleep(5)
    f9()
    while True:
        print("寻找镖头中...")
        shot()
        result = find_xy_in_game("../resources/img/flag/character/biao_tou.png")
        if result is not None:
            x, y = result[0], result[1]
            print("找到镖头，位置:", x, y)
            move_left_click(x, y)
            break
        else:
            print("未找到镖头，继续寻找")
        time.sleep(1)
    move_left_click(303, 479)  # 选4级镖
    move_left_click(304, 418)  # 选4级镖二级菜单
    move_left_click(304, 418)  # 关闭对话框
    move_left_click(335, 584)  # 走向镖局门口
    time.sleep(3)
    move_left_click(409, 521)  # 走出镖局
    text = mission.read_mission()
    for npc in npc_list:
        if text.__contains__(npc):
            print("接到任务运镖给: ", npc)
            return npc
    return None


def is_arrive():
    # TODO 是否已经到达终点
    return True


def check_fight(place, x, y):
    fight_flag = 0
    while is_fight():
        fight_flag = 1
        if is_popup() and is_not_same_crop4():
            print(">>> 保存4小人图片 >>>")
            shutil.copy(c.temp_popup, os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".jpg"))
            break
        if is_ready_fight():
            print(">>> 战斗施法 >>>")
            alt_q()
            alt_q()
    if fight_flag == 1:
        map.click(place, x, y)


def qf():
    print("长安 -> 秦府")
    map.click("cac", 88, 79)
    while is_arrive():
        time.sleep(0.1)
        check_fight("cac", 88, 79)
    print("进入秦府")
    move_left_click(343, 260)
    print("寻找秦琼")
    move_left_click(196, 209)
    time.sleep(5)
    f9()
    res = find_xy_in_game(os.path.join(c.flag_dir, "qin_qiong.png"))
    if res is not None:
        alt_g()
        move_left_click(res[0], res[1])


def dt():
    print("长安 -> 大唐官府")
    open_map_move(438, 222)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(438, 222)
        if is_target_point((427, 223, 450, 237)):
            break
    if map_is_open():
        tab()
    print("进入大唐官府")
    move_left_click(343, 86)
    print("大唐官府 -> 大唐官府府邸")
    open_map_move(352, 386)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(352, 386)
        if is_target_point((344, 384, 361, 395)):
            break
    print("进入大唐官府府邸")
    if map_is_open():
        tab()
    move_left_click(339, 310)
    print("寻找程咬金")
    move_left_click(363, 334)
    time.sleep(5)
    f9()
    res = find_xy_in_game(os.path.join(c.flag_dir, "chengyaojin.png"))
    if res is not None:
        alt_g()
        move_left_click(res[0], res[1])


def hs():
    print("长安 -> 化生寺")
    open_map_move(636, 227)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(636, 227)
        if is_target_point((627, 222, 643, 237)):
            break
    if map_is_open():
        tab()
    print("进入化生寺")
    move_left_click(497, 106)
    print("化生寺 -> 化生寺庙")
    open_map_move(451, 351)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(451, 351)
        if is_target_point((435, 347, 456, 361)):
            break
    print("进入化生寺庙")
    if map_is_open():
        tab()
    move_left_click(482, 293)
    print("寻找空度禅师")
    f9()
    res = find_xy_in_game(os.path.join(c.flag_dir, "kongduchanshi.png"))
    if res is not None:
        alt_g()
        move_left_click(res[0], res[1])


def ps(flag):
    """
    flag = 1 白晶晶
    flag = 2 花十娘
    """
    print("长安 -> 大唐国境")
    open_map_move(139, 495)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(139, 495)
        if is_target_point((131, 492, 152, 505)):
            break
    if map_is_open():
        tab()
    print("进入大唐国境")
    move_left_click(100, 606)
    print("大唐国境 -> 大唐境外")
    open_map_move(182, 468)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(182, 468)
        if is_target_point((172, 454, 192, 480)):
            break
    print("进入大唐境外")
    if map_is_open():
        tab()
    move_left_click(45, 237)
    print("大唐境外 -> 盘丝岭")
    open_map_move(594, 308)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(594, 308)
        if is_target_point((582, 311, 302, 322)):
            break
    print("进入盘丝岭")
    if map_is_open():
        tab()
    move_left_click(370, 79)
    print("盘丝岭 -> 盘丝洞")
    open_map_move(533, 278)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(533, 278)
        if is_target_point((526, 263, 542, 280)):
            break
    print("进入盘丝洞")
    if map_is_open():
        tab()
    move_left_click(691, 262)
    if flag == 1:
        move_left_click(359, 106)
        time.sleep(5)
        move_left_click(600, 113)
        time.sleep(5)
        f9()
        res = find_xy_in_game(os.path.join(c.flag_dir, "ps1.png"))
        if res is not None:
            alt_g()
            move_left_click(res[0], res[1])
    if flag == 2:
        move_left_click(522, 263)
        time.sleep(3)
        f9()
        res = find_xy_in_game(os.path.join(c.flag_dir, "ps2.png"))
        if res is not None:
            alt_g()
            move_left_click(res[0], res[1])


def wz():
    print("长安 -> 大唐国境")
    open_map_move(139, 495)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(139, 495)
        if is_target_point((131, 492, 152, 505)):
            break
    if map_is_open():
        tab()
    print("进入大唐国境")
    move_left_click(100, 606)
    print("大唐国境 -> 大唐境外")
    open_map_move(182, 468)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(182, 468)
        if is_target_point((172, 454, 192, 480)):
            break
    print("进入大唐境外")
    if map_is_open():
        tab()
    move_left_click(45, 237)
    print("大唐境外 -> 五庄观")
    open_map_move(688, 341)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(688, 341)
        if is_target_point((684, 336, 701, 355)):
            break
    print("进入五庄观")
    if map_is_open():
        tab()
    move_left_click(778, 258)
    print("五庄观 -> 五庄道馆")
    open_map_move(399, 369)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(399, 369)
        if is_target_point((377, 370, 395, 386)):
            break
    if map_is_open():
        tab()
    move_left_click(495, 283)
    f9()
    res = find_xy_in_game(os.path.join(c.flag_dir, "wz.png"))
    if res is not None:
        alt_g()
        move_left_click(res[0], res[1])


def st(flag):
    """
    flag = 1 大大王
    flag = 2 二大王
    flag = 3 三大王
    """
    print("长安 -> 大唐国境")
    open_map_move(139, 495)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(139, 495)
        if is_target_point((131, 492, 152, 505)):
            break
    if map_is_open():
        tab()
    print("进入大唐国境")
    move_left_click(100, 606)
    print("大唐国境 -> 大唐境外")
    open_map_move(182, 468)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(182, 468)
        if is_target_point((172, 454, 192, 480)):
            break
    print("进入大唐境外")
    if map_is_open():
        tab()
    move_left_click(45, 237)
    print("大唐境外 -> 狮驼岭")
    open_map_move(118, 369)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(118, 369)
        if is_target_point((108, 365, 127, 381)):
            break
    print("进入狮驼岭")
    move_left_click(52, 392)
    if flag == 1:
        print("寻找大大王")
        open_map_move(508, 434)
        while True:
            time.sleep(1)
            if done_fight():
                open_map_move(508, 434)
            if is_target_point((496, 435, 514, 447)):
                break
        print("进入大大王洞")
        if map_is_open():
            tab()
        move_left_click(567, 255)
        print("寻找大大王")
        move_left_click(527, 271)
        time.sleep(3)
        f9()
        res = find_xy_in_game(os.path.join(c.flag_dir, "st3.png"))
        if res is not None:
            alt_g()
            move_left_click(res[0], res[1])
    if flag == 2:
        print("寻找二大王洞")
        open_map_move(255, 284)
        while True:
            time.sleep(1)
            if done_fight():
                open_map_move(255, 284)
            if is_target_point((252, 273, 270, 290)):
                break
        print("进入二大王洞")
        if map_is_open():
            tab()
        move_left_click(423, 239)
        print("寻找二大王")
        f9()
        res = find_xy_in_game(os.path.join(c.flag_dir, "st2.png"))
        if res is not None:
            alt_g()
            move_left_click(res[0], res[1])
    if flag == 3:
        print("寻找三大王")
        open_map_move(217, 402)
        while True:
            time.sleep(1)
            if done_fight():
                open_map_move(217, 402)
            if is_target_point((204, 387, 226, 410)):
                break
        print("进入三大王洞")
        if map_is_open():
            tab()
        move_left_click(345, 300)
        print("寻找三大王")
        move_left_click(618, 349)
        time.sleep(5)
        f9()
        res = find_xy_in_game(os.path.join(c.flag_dir, "st3.png"))
        if res is not None:
            alt_g()
            move_left_click(res[0], res[1])


if __name__ == '__main__':
    load_driver()
    while True:
        npc = get_mission()
        if mission is None:
            print("[Error] 未获取到任务,请确认跑镖任务是否已加入自定义")
            sys.exit()
        elif mission == "秦琼":
            qf()
        elif mission == "程咬金":
            dt()
        elif mission == "空度禅师":
            hs()
        elif mission == "白晶晶":
            ps(1)
        elif mission == "花十娘":
            ps(2)
        elif mission == "镇元大仙":
            wz()
        elif mission == "大大王":
            st(1)
        elif mission == "二大王":
            st(2)
        elif mission == "三大王":
            st(3)
        else:
            sys.exit()
