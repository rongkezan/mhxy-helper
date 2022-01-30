from auto.utils.log import info
import constants as c
from verify import handle_popup
import time
import os
from auto.utils import Map, Bag, Mission

bag = Bag()
mission = Mission()
map = Map()

npc_dict = {
    "秦琼": "qq",
    "程咬金": "dt",
    "空度禅师": "hs",
    "地藏王": "df",
    "观音姐姐": "pt",
    "东海龙王": "lg",
    "孙婆婆": "ne",
    "镇元大仙": "wz",
    "白晶晶": "ps1",
    "花十娘": "ps2",
    "牛魔王": "mw",
    "大大王": "st1",
    "二大王": "st2",
    "三大王": "st3",
    "李靖": "tg1",
    "杨戬:": "tg2",
    "菩提祖师": "fc"
}


def is_place(place_name):
    pass


def met_robber():
    fight_flag = 0
    while is_fight():
        info("遭遇劫镖强盗")
        fight_flag = 1
        if is_popup():
            handle_popup()
        if is_ready_fight():
            do_fight()
    if fight_flag == 1:
        return True
    return False


def find_npc(paths, npc_name="npc"):
    """
    根据npc图片寻找npc
    paths: npc图片列表
    """
    do_hide()
    while True:
        time.sleep(0.1)
        info("寻找" + npc_name + "中...")
        if met_robber():
            info("寻找" + npc_name + "时遭遇劫镖强盗")
        found = False
        for path in paths:
            result = find_xy_in_game(path)
            if result is not None:
                found = True
                x, y = result[0], result[1]
                info("找到" + npc_name + "，位置:", x, y)
                b_move(x, y)
                break
        if found:
            info("已找到" + npc_name + "，退出寻找")
            break
        else:
            info("未找到" + npc_name + "，继续寻找")
            time.sleep(5)
            do_hide()


def b_move_map(func, x, y, log=None):
    """
    打开地图移动到指定地点并检查战斗，战斗结束会再次点击指定坐标，当判断已经到达目的地时，结束。
    """
    if log is not None:
        info(log)
    func(x, y)
    while not is_arrived():
        time.sleep(0.1)
        if met_robber():
            func(x, y)


def b_move(x, y, sleep=0, log=None):
    """
    点击指定坐标并检查战斗，战斗结束会再次点击指定坐标。
    """
    if log is not None:
        info(log)
    move_left_click(x, y)
    time.sleep(sleep)
    if met_robber():
        move_left_click(x, y)


def release_cargo(npc_name):
    """
    交付镖银
    """
    do_hide()
    while mission_not_finished():
        info("向", npc_name, "交付镖银")
        if met_robber():
            info("交付镖银时遭遇强盗")
        filename = npc_dict[npc_name]
        res = find_xy_in_game(os.path.join(c.flag_ch_dir, filename + ".png"))
        if res is not None:
            x, y = res[0], res[1]
            info("找到", npc_name, ",坐标为:", x, y, ",准备投送镖银")
            alt_g()
            move_left_click(x, y)
            result = game_template_match(c.flag_cargo)  # TODO截图
            if result is not None:
                x, y = result[0], result[1]
                move_left_click(x, y)
                move_left_click(0, 0)  # TODO 点击给予


def mission_not_finished():
    return bag.is_item_exist(os.path.join(c.temp_dir, "cargo.png"))
