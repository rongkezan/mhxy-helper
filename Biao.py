from Auto import *
from ImgOperation import *

rect = None


def switch_bag():
    keyboard2(604, 303)
    time.sleep(0.5)


def switch_map():
    keyboard(300)
    time.sleep(0.5)


def hide():
    keyboard(109)
    time.sleep(0.5)


def double_alt_q():
    keyboard2(604, 301)
    time.sleep(0.5)
    keyboard2(604, 301)


def fight_done():
    while True:
        time.sleep(3)
        if is_fight():
            while True:
                time.sleep(3)
                shot1()
                shape = (670, 154, 731, 447)
                Image.open(c.temp_game).crop(shape).save("img/temp/temp_fight_tool.jpg")
                score = compare_image("img/flag/flag_fight_tool.jpg", "img/temp/temp_fight_tool.jpg")
                if score > 0.95:
                    double_alt_q()
                    break
        else:
            return False
        return True


def ca_to_gj():
    switch_map()
    move_left_click(rect, 136, 464)
    switch_map()


def gj_to_jw():
    switch_map()
    move_left_click(rect, 181, 440)
    switch_map()


def is_ca_to_gj():
    Image.open(c.temp_game).crop((75, 26, 112, 39)).save("img/temp/temp_ca_to_gj.jpg")
    score = compare_image("img/temp/temp_ca_to_gj.jpg", "img/flag/flag_ca_to_gj.jpg")
    if score > 0.7:
        move_left_click(rect, 157, 549)
        return True


def is_gj_to_jw():
    Image.open(c.temp_game).crop((75, 26, 112, 39)).save("img/temp/temp_gj_to_jw.jpg")
    score = compare_image("img/flag/flag_gj_to_jw.jpg", "img/temp/temp_gj_to_jw.jpg")
    if score > 0.7:
        move_left_click(rect, 39, 270)
        return True


def get_mission():
    switch_bag()
    move_right_click(rect, 50, 373)  # 点击导标旗
    switch_bag()
    move_left_click(rect, 645, 311)  # 导标旗点击镖局
    move_left_click(rect, 486, 273)  # 进入镖局
    move_left_click(rect, 702, 284)  # 走向镖头
    time.sleep(5)
    hide()
    while True:
        time.sleep(3)
        print("寻找镖头中...")
        shot1()
        result = find_xy_game("img/flag/biao_tou.png")
        if result is not None:
            x, y = result[0], result[1]
            print("找到镖头，位置:", x, y)
            move_left_click(rect, x, y)
            break
        else:
            print("未找到镖头，继续寻找")
    move_left_click(rect, 245, 448)  # 选4级镖
    move_left_click(rect, 262, 383)  # 选4级镖二级菜单
    move_left_click(rect, 385, 385)  # 关闭对话框
    move_left_click(rect, 314, 554)  # 走向镖局门口
    move_left_click(rect, 456, 502)  # 走出镖局


def get_hwnd_rect():
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t.startswith('梦幻西游 ONLINE'):
            hwnd = win32gui.FindWindow(None, t)
            rect = win32gui.GetWindowRect(hwnd)
            return rect


if __name__ == '__main__':
    load_driver()
    rect = get_hwnd_rect()
    get_mission()
    ca_to_gj()
    print(">>> 从镖局出发，前往大唐国境 >>>")
    while True:
        time.sleep(3)
        shot1()
        if fight_done():
            ca_to_gj()
        elif is_ca_to_gj():
            break
    print(">>> 从大唐国境触发，前往大唐境外 >>>")
    gj_to_jw()
    while True:
        time.sleep(3)
        shot1()
        if fight_done():
            gj_to_jw()
        elif is_gj_to_jw():
            break







