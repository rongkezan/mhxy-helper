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


def click_banner(bx, by, x, y, log):
    info("导标旗点击", log)
    bag.right_click(bx, by)
    move_left_click(x, y)


def deliver_letters(text):
    school = appear_school(text)
    if school is None:
        error("未识别到地点:", text)
        sys.exit()
    if school == SCHOOL.DT.value:
        click_banner(1, 1, 0, 0, "大唐官府")
        mission.click_mission()
    elif school == SCHOOL.HS.value:
        click_banner(1, 1, 0, 0, "化生寺")
        mission.click_mission()
    elif school == SCHOOL.NE.value:
        click_banner(1, 4, 0, 0, "女儿")
        do_find_npc(NPC.ALG_DHW)
        mission.click_mission()
    elif school == SCHOOL.PT.value:
        click_banner(1, 1, 0, 0, "普陀山")
        mission.click_mission()
    elif school == SCHOOL.LG.value:
        click_banner(1, 4, 0, 0, "龙宫")
        do_find_npc(NPC.ALG_DHW)
        mission.click_mission()
    elif school == SCHOOL.DF.value:
        click_banner(1, 1, 0, 0, "阴曹地府")
        do_find_npc(NPC.YZ)
        mission.click_mission()


def target_fight_mission(text):
    place = appear_city(text)
    if place is None:
        error("未识别到地点:", text)
        sys.exit()
    info("识别到地点:", place)
    if place == CITY.JY.value:
        click_fxf(0, 0, "建邺城")
        mission.click_mission()
    elif place == CITY.CS.value:
        click_fxf(0, 0, "长寿村")
        mission.click_mission()
    elif place == CITY.AL.value:
        click_fxf(0, 0, "傲来国")
        mission.click_mission()
    elif place == CITY.ZZ.value:
        click_fxf(0, 0, "朱紫国")
        mission.click_mission()
    elif place == CITY.BX.value:
        click_fxf(0, 0, "宝象国")
        mission.click_mission()
    elif place == CITY.XL.value:
        click_fxf(0, 0, "西凉女国")
        mission.click_mission()
    elif place == CITY.HW.value:
        click_banner(4, 3, 504, 466, "东海湾")
        mission.click_mission()
    elif place == CITY.YW.value:
        click_fxf(0, 0, "江南野外")
    elif place == CITY.CSJW.value:
        click_fxf(0, 0, "长寿郊外")
        mission.click_mission()


if __name__ == '__main__':
    load_driver()
    # info("点击导标旗")
    # bag.right_click(4, 4)
    # move_left_click(517, 233)
    # do_hide()
    # info("点击帮派传送人")
    # move_left_click(329, 222)
    # move_left_click(212, 394)
    # info("点击帮派车夫")
    # move_left_click(307, 321)
    # move_left_click(432, 417)
    # info("点击玄武堂总管接任务")
    # do_find_npc(NPC.CAC_BP.value)
    # move_left_click(204, 396)
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
        deliver_letters(text)
    else:
        target_fight_mission(text)