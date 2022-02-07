"""
厢房
"""
from auto.component.mission import mission
from auto.component.bag import bag
from auto.component.action import action
from auto.component.camera import camera
from constants.npc import NPC
from constants.place import *
import auto.utils.log as log
import sys
import constants.path as p
import os


class Xf:
    def click_fxf(self, x, y, msg):
        log.info("飞行符点击", msg)
        bag.right_click(1, 2)
        action.move_left_click(x, y)

    def click_banner(self, bx, by, x, y, msg):
        log.info("导标旗点击", msg)
        bag.right_click(bx, by)
        action.move_left_click(x, y)

    def deliver_letters(self, text):
        school = appear_school(text)
        if school is None:
            log.error("未识别到地点:", text)
            sys.exit()
        if school == SCHOOL.DT.value:
            self.click_banner(1, 1, 0, 0, "大唐官府")
            mission.click_target()
        elif school == SCHOOL.HS.value:
            self.click_banner(1, 1, 0, 0, "化生寺")
            mission.click_target()
        elif school == SCHOOL.NE.value:
            self.click_banner(4, 1, 0, 0, "女儿")
            action.do_find_npc(NPC.ALG_DHW)
            mission.click_target()
        elif school == SCHOOL.PT.value:
            self.click_banner(1, 1, 0, 0, "普陀山")
            mission.click_target()
        elif school == SCHOOL.LG.value:
            self.click_banner(4, 1, 0, 0, "龙宫")
            action.do_find_npc(NPC.ALG_DHW)
            mission.click_target()
        elif school == SCHOOL.DF.value:
            self.click_banner(1, 1, 0, 0, "阴曹地府")
            action.do_find_npc(NPC.YZ)
            mission.click_target()

    def target_fight_mission(self, text):
        place = appear_city(text)
        if place is None:
            log.error("未识别到地点:", text)
            sys.exit()
        log.info("识别到地点:", place)
        if place == CITY.JY.value:
            self.click_fxf(538, 416, "建邺城")
            mission.click_target()
        elif place == CITY.CS.value:
            self.click_fxf(312, 243, "长寿村")
            mission.click_target()
        elif place == CITY.AL.value:
            self.click_fxf(387, 485, "傲来国")
            mission.click_target()
        elif place == CITY.ZZ.value:
            self.click_fxf(358, 453, "朱紫国")
            mission.click_target()
        elif place == CITY.BX.value:
            self.click_fxf(300, 386, "宝象国")
            mission.click_target()
        elif place == CITY.XL.value:
            self.click_fxf(307, 301, "西凉女国")
            mission.click_target()
        elif place == CITY.HW.value:
            self.click_banner(4, 1, 504, 466, "东海湾")
            mission.click_target()
        elif place == CITY.YW.value:
            self.click_banner(1, 1, 670, 491, "江南野外")
            mission.click_target()
        elif place == CITY.CSJW.value:
            self.click_banner(2, 1, 509, 526, "长寿郊外")
            mission.click_target()

    def run(self):
        # log.info("点击导标旗")
        # bag.right_click(5, 1)
        # action.move_left_click(517, 233)
        # action.do_hide()
        # log.info("点击帮派传送人")
        # action.move_left_click(329, 222)
        # action.move_left_click(212, 394)
        # log.info("点击帮派车夫")
        # action.move_left_click(310, 230)
        # action.move_left_click(427, 416)
        # log.info("点击玄武堂总管接任务")
        # while camera.find_xy_in_game(os.path.join(p.flag_npc_dir, "xwtzg_head.png")) is None:
        #     action.do_find_npc(NPC.XWTZG.value)
        # action.move_left_click(204, 396)
        # action.move_left_click(405, 417)

        log.info("查看任务")
        text = mission.read()
        if text.__contains__("巡逻"):
            need_fight = True
            count = 0
            while need_fight:
                if count == 0:
                    action.move_left_click(173, 486)
                    count = 1
                else:
                    action.move_left_click(508, 329)
                    count = 0
                if camera.is_fight():
                    need_fight = False
                    action.do_fight5()
        elif text.__contains__("召唤兽"):
            action.do_find_npc(NPC.BPJGR.value)
            action.move_left_click(197, 436)
            log.info("点击帮派车夫")
            action.move_left_click(307, 228)
            action.move_left_click(180, 417)
            action.do_find_npc(NPC.BPSHS)
            action.move_left_click(204, 394)
            if camera.is_fight():
                action.do_fight5()
        elif text.__contains__("送信"):
            self.deliver_letters(text)
        else:
            self.target_fight_mission(text)


if __name__ == '__main__':
    xf = Xf()
    xf.run()
