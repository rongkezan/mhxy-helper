from utils.game_action import *
from utils.game_watcher import *
from utils.window import *
import shutil


def qf():
    print("长安 -> 秦府")
    open_map_move(213, 422)
    while True:
        time.sleep(1)
        if done_fight():
            open_map_move(213, 418)
        if is_target_point((200, 408, 227, 431)):
            break
    if map_is_open():
        tab()
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


def is_target_point(shape):
    shot()
    temp_path = os.path.join(c.temp_dir, "red_point.png")
    Image.open(c.temp_game).crop(shape).save(temp_path)
    _, score = template_match(os.path.join(c.flag_dir, "red_point.png"), temp_path)
    if score >= 5:
        return True
    return False


def open_map_move(x, y):
    tab()
    move_left_click(x, y)
    move(741, 81)


def done_fight():
    fight_flag = 0
    while is_fight():
        fight_flag = 1
        time.sleep(1)
        # 有4小人验证，先点击4小人
        while is_popup():
            time.sleep(1)
            if is_not_same_crop4():
                print(">>> 保存4小人图片 >>>")
                shutil.copy(c.temp_popup, os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".jpg"))
                break
        # 已经过4小人验证，战斗
        if is_ready_fight():
            print(">>> 战斗施法 >>>")
            alt_q()
            alt_q()
    if fight_flag == 1:
        return True
    return False
