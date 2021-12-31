"""
厢房
"""
from utils.component import Map, Bag, Mission
from utils.action import *
from utils.npc import NPC
from utils.place import *

map = Map()
bag = Bag()
mission = Mission()


def click_fxf(x, y, log):
    info("飞行符点击", log)
    bag.right_click(1, 5)
    move_left_click(x, y)


def click_banner(n, x, y, log):
    info("导标旗点击", log)
    bag.right_click(1, n)
    move_left_click(x, y)


if __name__ == '__main__':
    info("点击导标旗")
    bag.right_click(2, 5)
    move_left_click(0, 0)
    info("点击帮派传送人")
    do_find_npc(NPC.CAC_BP)
    move_left_click(0, 0)
    info("点击帮派土地")
    do_find_npc(NPC.BPTDGG)
    move_left_click(0, 0)
    info("点击玄武堂总管接任务")
    do_find_npc(NPC.XWTZG)
    move_left_click(0, 0)
    info("查看任务")
    text = mission.read_mission()
    if text.__contains__("巡逻"):
        while True:
            move_left_click(0, 0)
            if is_fight():
                do_fight5()
    elif text.__contains__("召唤兽"):
        do_find_npc(NPC.BPJGR)
        move_left_click(0, 0)
        do_find_npc(NPC.BPTDGG)
        move_left_click(0, 0)
        do_find_npc(NPC.BPZHS)
        move_left_click(0, 0)
        if is_fight():
            do_fight5()
    elif text.__contains__("送信"):
        place = appear_place(text)
        if place is None:
            error("未识别到地点:", text)
            sys.exit()
        if place == PLACE.DT.value:
            click_banner(1, 0, 0, "大唐官府")
        elif place == PLACE.HS.value:
            click_banner(1, 0, 0, "化生寺")
        elif place == PLACE.PT.value:
            click_banner(1, 0, 0, "普陀山")
        elif place == PLACE.DF.value:
            click_banner(1, 0, 0, "阴曹地府")
            do_find_npc(NPC.YZ)
        elif place == PLACE.LG.value:
            click_banner(4, 0, 0, "龙宫")
            do_find_npc(NPC.ALG_DHW)
        elif place == PLACE.NE.value:
            click_banner(4, 0, 0, "女儿")
            do_find_npc(NPC.ALG_DHW)

    place = appear_place(text)
    if place is None:
        error("未识别到地点:", text)
        sys.exit()
    info("识别到地点:", place)
    if place == PLACE.JY.value:
        click_fxf(0, 0, "建邺城")
        mission.click_mission()
    elif place == PLACE.CS.value:
        click_fxf(0, 0, "长寿村")
        mission.click_mission()
    elif place == PLACE.AL.value:
        click_fxf(0, 0, "傲来国")
        mission.click_mission()
    elif place == PLACE.ZZ.value:
        click_fxf(0, 0, "朱紫国")
        mission.click_mission()
    elif place == PLACE.BX.value:
        click_fxf(0, 0, "宝象国")
        mission.click_mission()
    elif place == PLACE.XL.value:
        click_fxf(0, 0, "西凉女国")
