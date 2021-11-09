from auto import *
from window import *
from map import *

rect = None


def get_mission():
    alt_e()
    move_right_click(rect, 50, 373)  # 点击导标旗
    alt_e()
    move_left_click(rect, 645, 311)  # 导标旗点击镖局
    move_left_click(rect, 486, 273)  # 进入镖局
    move_left_click(rect, 702, 284)  # 走向镖头
    time.sleep(5)
    f9()
    while True:
        time.sleep(3)
        print("寻找镖头中...")
        shot()
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


if __name__ == '__main__':
    load_driver()
    rect = get_rect()
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
        shot()
        if fight_done():
            gj_to_jw()
        elif is_gj_to_jw():
            break







