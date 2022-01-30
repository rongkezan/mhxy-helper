"""
厢房
"""
from auto.component.bag import mission
from constants import NPC
import auto.utils.log as log
import sys

class Xf:
    def click_fxf(self, x, y, msg):
        log.info("飞行符点击", msg)
        bag.right_click(1, 5)
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
            mission.click_mission()
        elif school == SCHOOL.HS.value:
            self.click_banner(1, 1, 0, 0, "化生寺")
            mission.click_mission()
        elif school == SCHOOL.NE.value:
            self.click_banner(1, 4, 0, 0, "女儿")
            action.do_find_npc(NPC.ALG_DHW)
            mission.click_mission()
        elif school == SCHOOL.PT.value:
            self.click_banner(1, 1, 0, 0, "普陀山")
            mission.click_mission()
        elif school == SCHOOL.LG.value:
            self.click_banner(1, 4, 0, 0, "龙宫")
            action.do_find_npc(NPC.ALG_DHW)
            mission.click_mission()
        elif school == SCHOOL.DF.value:
            self.click_banner(1, 1, 0, 0, "阴曹地府")
            action.do_find_npc(NPC.YZ)
            mission.click_mission()

    def target_fight_mission(self, text):
        place = appear_city(text)
        if place is None:
            log.error("未识别到地点:", text)
            sys.exit()
        log.info("识别到地点:", place)
        if place == CITY.JY.value:
            self.click_fxf(0, 0, "建邺城")
            mission.click_mission()
        elif place == CITY.CS.value:
            self.click_fxf(0, 0, "长寿村")
            mission.click_mission()
        elif place == CITY.AL.value:
            self.click_fxf(0, 0, "傲来国")
            mission.click_mission()
        elif place == CITY.ZZ.value:
            self.click_fxf(0, 0, "朱紫国")
            mission.click_mission()
        elif place == CITY.BX.value:
            self.click_fxf(0, 0, "宝象国")
            mission.click_mission()
        elif place == CITY.XL.value:
            self.click_fxf(0, 0, "西凉女国")
            mission.click_mission()
        elif place == CITY.HW.value:
            self.click_banner(4, 3, 504, 466, "东海湾")
            mission.click_mission()
        elif place == CITY.YW.value:
            self.click_fxf(0, 0, "江南野外")
        elif place == CITY.CSJW.value:
            self.click_fxf(0, 0, "长寿郊外")
            mission.click_mission()

    def run(self):
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
        log.info("查看任务")
        text = mission.read_mission()
        if text.__contains__("巡逻"):
            while True:
                action.move_left_click(0, 0)
                if camera.is_fight():
                    action.do_fight5()
        elif text.__contains__("召唤兽"):
            action.do_find_npc(NPC.BPJGR)
            action.move_left_click(0, 0)
            action.do_find_npc(NPC.BPTDGG)
            action.move_left_click(0, 0)
            action.do_find_npc(NPC.BPZHS)
            action.move_left_click(0, 0)
            if camera.is_fight():
                action.do_fight5()
        elif text.__contains__("送信"):
            self.deliver_letters(text)
        else:
            self.target_fight_mission(text)
