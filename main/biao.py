from utils.game_action import *
from utils.game_watcher import *
from utils.map import Map
from utils.bag import Bag
from utils.mission import Mission
from utils.log import info, warn, error
import shutil

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
    "菩提祖师": "fc",
}

bag = Bag()
mission = Mission()
map = Map()


def get_mission():
    bag.right_click(5, 1)  # 点击导标旗
    b_move(647, 342)  # 导标旗点击镖局
    b_move(484, 280)  # 进入镖局
    b_move(688, 303)  # 走向镖头
    time.sleep(5)
    f9()
    while True:
        info("寻找镖头中...")
        result = find_xy_in_game(os.path.join(c.flag_character_dir, "bt.png"))
        if result is not None:
            x, y = result[0], result[1]
            info("找到镖头，位置:", x, y)
            b_move(x, y)
            break
        else:
            info("未找到镖头，继续寻找")
        time.sleep(1)
    b_move(303, 479)  # 选4级镖
    b_move(304, 418)  # 选4级镖二级菜单
    b_move(304, 418)  # 关闭对话框
    b_move(335, 584)  # 走向镖局门口
    time.sleep(3)
    b_move(409, 521)  # 走出镖局
    text = mission.read_mission()
    for npc in npc_dict:
        if text.__contains__(npc):
            info("接到任务运镖给: ", npc)
            return npc
    return None


def is_place(place_name):
    # TODO 是否已经在指定地点
    return True


def is_arrive():
    # TODO 是否已经到达终点
    return True


def mission_finished():
    pass


def meet_robber():
    """
    遭遇劫镖强盗
    :return: True = 发生了战斗，False = 未发生战斗
    """
    fight_flag = 0
    while is_fight():
        info("遭遇劫镖强盗")
        fight_flag = 1
        if is_popup() and is_not_same_crop4():
            info("保存4小人图片")
            shutil.copy(c.temp_popup, os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".png"))
            break
        if is_ready_fight():
            info("战斗施法")
            alt_q()
            alt_q()
    if fight_flag == 1:
        return True
    return False


def b_move_map(place, x, y, log=None):
    """
    打开地图移动到指定地点并检查战斗，战斗结束会再次点击指定坐标，当判断已经到达目的地时，结束。
    """
    if log is not None:
        info(log)
    map.click(place, x, y)
    while not is_arrive():
        time.sleep(0.1)
        if meet_robber():
            map.click(place, x, y)


def b_move(x, y, sleep=0, log=None):
    """
    点击指定坐标并检查战斗，战斗结束会再次点击指定坐标。
    """
    if log is not None:
        info(log)
    b_move(x, y)
    time.sleep(sleep)
    if meet_robber():
        b_move(x, y)


def release_cargo(npc_name):
    """
    交付镖银
    """
    f9()
    while not mission_finished():
        info("向", npc_name, "交付镖银")
        if meet_robber():
            info("交付镖银时遭遇强盗")
        filename = npc_dict[npc_name]
        res = find_xy_in_game(os.path.join(c.flag_character_dir, filename + ".png"))
        if res is not None:
            x, y = res[0], res[1]
            info("找到", npc_name, ",坐标为:", x, y, ",准备投送镖银")
            alt_g()
            b_move(x, y)


def transfer_yz():
    """
    驿站车夫传送
    """
    while True:
        time.sleep(0.1)
        meet_robber()
        info("寻找驿站车夫")
        res = None
        for yz in c.flag_yz:
            res = find_xy_in_game(yz)
            break
        if res is not None:
            x, y = res[0], res[1]
            info("找到驿站车夫, 坐标为:", x, y, "点击驿站车夫")
            b_move(x, y)
            info("驿站车夫传送大唐国境")
            b_move(268, 472)
            if is_place("大唐国境"):
                break
        else:
            warn("未能找到驿站车夫")


def ca_to_dtjw():
    """
    去大唐境外
    """
    b_move_map("cac", 0, 0, log="长安 -> 驿站")
    transfer_yz()
    b_move_map("dtgj", 0, 0, log="大唐国境 -> 大唐境外")
    b_move(45, 237, log="进入大唐境外")


def ca_to_dhw():
    """
    去东海湾
    """
    b_move_map("cac", 0, 0, log="长安 -> 江南野外")
    b_move(0, 0, log="进入江南野外")
    b_move_map("jnyw", 0, 0, log="江南野外 -> 建邺城")
    b_move(0, 0, log="进入建邺城")
    b_move_map("jyc", 0, 0, log="建邺城 -> 东海湾")
    b_move(0, 0, log="进入东海湾")


def qf():
    b_move_map("cac", 88, 79, log="长安 -> 秦府")
    b_move(343, 260, log="进入秦府")
    if is_place("秦府"):
        b_move(196, 209, 5, log="寻找秦琼")
        release_cargo("秦琼")


def dt():
    b_move_map("cac", 0, 0, log="长安 -> 大唐官府")
    b_move(343, 86, log="进入大唐官府")
    if is_place("大唐官府"):
        b_move_map("dtgf", 0, 0, log="大唐官府 -> 大唐官府府邸")
        b_move(339, 310, log="进入大唐官府府邸")
        if is_place("大唐官府府邸"):
            b_move(363, 334, 5, log="寻找程咬金")
            release_cargo("程咬金")


def hs():
    b_move_map("cac", 0, 0, log="长安 -> 化生寺")
    b_move(497, 106, log="进入化生寺")
    b_move_map("hss", 0, 0, log="化生寺 -> 化生寺庙")
    b_move(482, 293, log="进入化生寺庙")
    release_cargo("空度禅师")


def df():
    b_move_map("cac", 0, 0, log="长安 -> 驿站")
    transfer_yz()
    b_move_map("dtgj", 0, 0, log="大唐国境 -> 地府")
    b_move(0, 0, log="进入地府")
    b_move_map("df", 0, 0, log="地府 -> 地藏王府")
    b_move(0, 0, log="进入地藏王府")
    b_move(0, 0, log="地藏王府 -> 地藏王内府")
    b_move(0, 0, log="进入地藏王内府")
    release_cargo("地藏王")


def pt():
    b_move_map("cac", 0, 0, log="长安城 -> 大唐国境")
    b_move(0, 0, log="进入大唐国境")
    b_move_map("dtgj", 0, 0, log="大唐国境 -> 普陀山")
    b_move(0, 0, log="进入普陀山")
    b_move_map("pts", 0, 0, log="普陀山 -> 潮音洞")
    b_move(0, 0, log="进入潮音洞")
    b_move(0, 0, log="走向观音姐姐")
    info("寻找观音姐姐")
    release_cargo("观音姐姐")


def lg():
    ca_to_dhw()
    b_move_map("dhw", 0, 0, log="东海湾 -> 龙宫")
    b_move(0, 0, log="进入龙宫")
    b_move_map("lg", 0, 0, log="龙宫 -> 龙宫殿")
    b_move(0, 0, log="进入龙宫殿")
    b_move(0, 0, log="走向东海龙王")
    release_cargo("东海龙王")


def ne():
    ca_to_dhw()
    b_move_map("dhw", 0, 0, log="东海湾 -> 傲来国")
    b_move(0, 0, log="进入傲来国")
    b_move_map("alg", 0, 0, log="傲来国 -> 女儿村")
    b_move(0, 0, log="进入女儿村")
    b_move_map("nec", 0, 0, log="女儿村 -> 女儿村房")
    b_move(0, 0, log="进入女儿村房")
    release_cargo("孙婆婆")


def wz():
    ca_to_dtjw()
    b_move_map("dtjw", 0, 0, log="大唐境外 -> 五庄观")
    b_move_map("wzg", 0, 0, log="五庄观 -> 五庄道馆")
    b_move(495, 283, log="进入五庄观")
    release_cargo("镇元大仙")


def ps(flag):
    """
    flag = 1 白晶晶
    flag = 2 花十娘
    """
    ca_to_dtjw()
    b_move_map("dtjw", 0, 0, log="大唐境外 -> 盘丝岭")
    b_move(370, 79, log="进入盘丝岭")
    b_move_map("psl", 0, 0, log="盘丝岭 -> 盘丝洞")
    b_move(691, 262, log="进入盘丝洞")
    if flag == 1:
        b_move(359, 106)
        time.sleep(5)
        b_move(600, 113)
        time.sleep(5)
        release_cargo("白晶晶")
    if flag == 2:
        b_move(522, 263)
        time.sleep(3)
        release_cargo("花十娘")


def mw():
    ca_to_dtjw()
    b_move_map("dtjw", 0, 0, log="大唐境外 -> 魔王寨")
    b_move(0, 0, log="进入魔王寨")
    b_move_map("mwz", 0, 0, log="魔王寨 -> 魔王寨殿")
    b_move(0, 0, log="进入魔王寨殿")
    release_cargo("牛魔王")


def st(flag):
    """
    flag = 1 大大王
    flag = 2 二大王
    flag = 3 三大王
    """
    ca_to_dtjw()
    b_move_map("dtjw", 0, 0, log="大唐境外 -> 狮驼岭")
    b_move(52, 392, log="进入狮驼岭")
    if flag == 1:
        b_move_map("stl", 0, 0, log="狮驼岭 -> 大大王洞")
        b_move(567, 255, log="进入大大王洞")
        b_move(527, 271, log="走向大大王")
        time.sleep(3)
        release_cargo("大大王")
    if flag == 2:
        b_move_map("stl", 0, 0, log="狮驼岭 -> 二大王洞")
        b_move(423, 239, log="进入二大王洞")
        release_cargo("二大王")
    if flag == 3:
        b_move_map("stl", 0, 0, log="狮驼岭 -> 三大王洞")
        b_move(345, 300, log="进入三大王洞")
        b_move(618, 349, log="走向三大王")
        time.sleep(5)
        release_cargo("三大王")


def tg(flag):
    """
    flag = 1 李靖
    flag = 2 杨戬
    """
    ca_to_dtjw()
    b_move_map("dtjw", 0, 0, log="大唐境外 -> 长寿郊外")
    b_move(0, 0, log="进入长寿郊外")
    b_move_map("csjw", 0, 0, log="长寿郊外 -> 天宫")
    b_move(0, 0, log="进入天宫")
    b_move_map("tg", 0, 0, log="天宫 -> 凌霄宝殿")
    b_move(0, 0, log="进入凌霄宝殿")
    if flag == 1:
        b_move(0, 0, log="寻找李靖")
        release_cargo("李靖")
    else:
        b_move(0, 0, log="寻找杨戬")
        release_cargo("杨戬")


def fc():
    ca_to_dtjw()
    b_move_map("dtjw", 0, 0, log="大唐境外 -> 长寿郊外")
    b_move(0, 0, log="进入长寿郊外")
    b_move_map("csjw", 0, 0, log="长寿郊外 -> 长寿村")
    b_move(0, 0, log="进入长寿村")
    b_move_map("csc", 0, 0, log="长寿村 -> 方寸山")
    b_move(0, 0, log="进入方寸山")
    b_move_map("fcs", 0, 0, log="方寸山 -> 方寸山殿")
    b_move(0, 0, log="进入方寸山殿")
    b_move(0, 0, log="走向菩提祖师")
    release_cargo("菩提祖师")


if __name__ == '__main__':
    load_driver()
    while True:
        npc = get_mission()
        if npc is None:
            error("未获取到任务,请确认跑镖任务是否已加入自定义")
            sys.exit()
        elif npc == "秦琼":
            qf()
        elif npc == "程咬金":
            dt()
        elif npc == "空度禅师":
            hs()
        elif npc == "地藏王":
            df()
        elif npc == "观音姐姐":
            pt()
        elif npc == "东海龙王":
            lg()
        elif npc == "孙婆婆":
            ne()
        elif npc == "镇元大仙":
            wz()
        elif npc == "白晶晶":
            ps(1)
        elif npc == "花十娘":
            ps(2)
        elif npc == "牛魔王":
            mw()
        elif npc == "大大王":
            st(1)
        elif npc == "二大王":
            st(2)
        elif npc == "三大王":
            st(3)
        elif npc == "李靖":
            tg(1)
        elif npc == "杨戬":
            tg(2)
        elif npc == "菩提祖师":
            fc()
        else:
            sys.exit()
