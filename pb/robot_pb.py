"""
1.get mission -> 2.transfer cargo -> 3.release cargo
notice: 2,3 maybe meet robber
"""
from pb.action import *


def get_mission():
    bag.right_click(1, 2)  # 点击导标旗
    move_left_click(647, 342)  # 导标旗点击镖局
    move_left_click(530, 238)  # 进入镖局
    move_left_click(688, 303)  # 走向镖头
    time.sleep(5)
    find_npc([os.path.join(c.flag_ch_dir, "bt.png")], "镖头")
    move_left_click(303, 479)  # 选4级镖
    move_left_click(304, 418)  # 选4级镖二级菜单
    move_left_click(304, 418)  # 关闭对话框
    move_left_click(335, 584)  # 走向镖局门口
    time.sleep(3)
    b_move(409, 521)  # 走出镖局
    text = mission.read_mission()
    for npc in npc_dict:
        if text.__contains__(npc):
            info("接到任务运镖给: ", npc)
            return npc
    return None


def ca_to_dtjw():
    """
    去大唐境外
    """
    b_move_map(map.click_cac, 283, 38, log="长安 -> 驿站")
    find_npc(c.flag_yz, "驿站车夫")
    while not is_place("大唐境外"):
        b_move_map(map.click_dtgj, 5, 84, log="大唐国境 -> 大唐境外")
        b_move(45, 237, log="进入大唐境外")


def ca_to_dhw():
    """
    去东海湾
    """
    while not is_place("江南野外"):
        b_move_map(map.click_cac, 545, 10, log="长安 -> 江南野外")
        b_move(700, 621, log="进入江南野外")
    while not is_place("建邺城"):
        b_move_map(map.click_jnyw, 152, 55, log="江南野外 -> 建邺城")
        b_move(701, 278, log="进入建邺城")
    while not is_place("东海湾"):
        b_move_map(map.click_jyc, 274, 34, log="建邺城 -> 东海湾")
        b_move(573, 397, log="进入东海湾")


def qf():
    b_move_map(map.click_cac, 88, 79, log="长安 -> 秦府")
    b_move(343, 260, log="进入秦府")
    while not is_place("秦府"):
        b_move(196, 209, 5, log="寻找秦琼")
        release_cargo("秦琼")


def dt():
    while not is_place("大唐官府"):
        b_move_map(map.click_cac, 312, 277, log="长安 -> 大唐官府")
        b_move(343, 86, log="进入大唐官府")
    while not is_place("大唐官府府邸"):
        b_move_map(map.click_dtgf, 74, 48, log="大唐官府 -> 大唐官府府邸")
        b_move(339, 310, log="进入大唐官府府邸")
    while not is_place("大唐官府府邸"):
        b_move(363, 334, 5, log="寻找程咬金")
        release_cargo("程咬金")


def hs():
    while not is_place("化生寺"):
        b_move_map(map.click_cac, 513, 277, log="长安 -> 化生寺")
        b_move(513, 277, log="进入化生寺")
    while not is_place("化生寺庙"):
        b_move_map(map.click_hss, 92, 56, log="化生寺 -> 化生寺庙")
        b_move(482, 293, log="进入化生寺庙")
    release_cargo("空度禅师")


def df():
    b_move_map(map.click_cac, 283, 38, log="长安 -> 驿站")
    find_npc(c.flag_yz, "驿站车夫")
    while not is_place("地府"):
        b_move_map(map.click_dtgj, 49, 332, log="大唐国境 -> 地府")
        b_move(0, 0, log="进入地府")
    while not is_place("地藏王府"):
        b_move_map(map.click_df, 29, 70, log="地府 -> 地藏王府")
        b_move(0, 0, log="进入地藏王府")
    while not is_place("地藏王内府"):
        b_move(0, 0, log="地藏王府 -> 地藏王内府")
        b_move(0, 0, log="进入地藏王内府")
    release_cargo("地藏王")


def pt():
    while not is_place("大唐国境"):
        b_move_map(map.click_cac, 10, 3, log="长安城 -> 大唐国境")
        b_move(0, 0, log="进入大唐国境")
    while not is_place("普陀山"):
        b_move_map(map.click_dtgj, 219, 69, log="大唐国境 -> 普陀山")
        b_move(0, 0, log="进入普陀山")
    while not is_place("潮音洞"):
        b_move_map("pts", 6, 65, log="普陀山 -> 潮音洞")
        b_move(0, 0, log="进入潮音洞")
    b_move(0, 0, log="走向观音姐姐")
    info("寻找观音姐姐")
    release_cargo("观音姐姐")


def lg():
    ca_to_dhw()
    while not is_place("龙宫"):
        b_move_map(map.click_dhw, 113, 90, log="东海湾 -> 龙宫")
        b_move(0, 0, log="进入龙宫")
    while not is_place("龙宫殿"):
        b_move_map(map.click_lg, 113, 64, log="龙宫 -> 龙宫殿")
        b_move(0, 0, log="进入龙宫殿")
    b_move(0, 0, log="走向东海龙王")
    release_cargo("东海龙王")


def ne():
    ca_to_dhw()
    while not is_place("傲来国"):
        b_move_map(map.click_dhw, 63, 18, log="东海湾 -> 傲来国")
        b_move(0, 0, log="进入傲来国")
    while not is_place("女儿村"):
        b_move_map(map.click_alg, 6, 141, log="傲来国 -> 女儿村")
        b_move(0, 0, log="进入女儿村")
    while not is_place("女儿村房"):
        b_move_map(map.click_nec, 17, 124, log="女儿村 -> 女儿村房")
        b_move(0, 0, log="进入女儿村房")
    release_cargo("孙婆婆")


def wz():
    ca_to_dtjw()
    while not is_place("五庄观"):
        b_move_map(map.click_dtjw, 633, 85, log="大唐境外 -> 五庄观")
        b_move(0, 0, log="进入五庄观")
    while not is_place("五庄道馆"):
        b_move_map("wzg", 58, 38, log="五庄观 -> 五庄道馆")
        b_move(495, 283, log="进入五庄道馆")
    release_cargo("镇元大仙")


def ps(flag):
    """
    flag = 1 白晶晶
    flag = 2 花十娘
    """
    ca_to_dtjw()
    while not is_place("盘丝岭"):
        b_move_map(map.click_dtjw, 529, 118, log="大唐境外 -> 盘丝岭")
        b_move(370, 79, log="进入盘丝岭")
    while not is_place("盘丝洞"):
        b_move_map("psl", 190, 129, log="盘丝岭 -> 盘丝洞")
        b_move(691, 262, log="进入盘丝洞")
    if flag == 1:
        b_move(359, 106)
        time.sleep(5)
        b_move(600, 113)
        time.sleep(5)
        release_cargo("白晶晶")
    if flag == 2:
        while True:
            time.sleep(3)
            release_cargo("花十娘")


def mw():
    ca_to_dtjw()
    while not is_place("魔王寨"):
        b_move_map(map.click_dtjw, 57, 118, log="大唐境外 -> 魔王寨")
        b_move(0, 0, log="进入魔王寨")
    while not is_place("魔王寨殿"):
        b_move_map(map.click_mwz, 93, 73, log="魔王寨 -> 魔王寨殿")
        b_move(0, 0, log="进入魔王寨殿")
    release_cargo("牛魔王")


def st(flag):
    """
    flag = 1 大大王
    flag = 2 二大王
    flag = 3 三大王
    """
    ca_to_dtjw()
    while not is_place("狮驼岭"):
        b_move_map(map.click_dtjw, 4, 53, log="大唐境外 -> 狮驼岭")
        b_move(52, 392, log="进入狮驼岭")
    if flag == 1:
        while not is_place("大大王洞"):
            b_move_map(map.click_stl, 119, 29, log="狮驼岭 -> 大大王洞")
            b_move(567, 255, log="进入大大王洞")
        b_move(527, 271, log="走向大大王")
        time.sleep(3)
        release_cargo("大大王")
    if flag == 2:
        while not is_place("二大王洞"):
            b_move_map(map.click_stl, 27, 87, log="狮驼岭 -> 二大王洞")
            b_move(423, 239, log="进入二大王洞")
        release_cargo("二大王")
    if flag == 3:
        while not is_place("三大王洞"):
            b_move_map(map.click_stl, 15, 40, log="狮驼岭 -> 三大王洞")
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
    while not is_place("长寿郊外"):
        b_move_map(map.click_dtjw, 50, 23, log="大唐境外 -> 长寿郊外")
        b_move(0, 0, log="进入长寿郊外")
    while not is_place("天宫"):
        b_move_map(map.click_csjw, 22, 64, log="长寿郊外 -> 天宫")
        b_move(0, 0, log="进入天宫")
    while not is_place("凌霄宝殿"):
        b_move_map("tg", 149, 62, log="天宫 -> 凌霄宝殿")
        b_move(0, 0, log="进入凌霄宝殿")
    if flag == 1:
        b_move(0, 0, log="寻找李靖")
        release_cargo("李靖")
    else:
        b_move(0, 0, log="寻找杨戬")
        release_cargo("杨戬")


def fc():
    ca_to_dtjw()
    while not is_place("长寿郊外"):
        b_move_map(map.click_dtjw, 50, 23, log="大唐境外 -> 长寿郊外")
        b_move(0, 0, log="进入长寿郊外")
    while not is_place("长寿村"):
        b_move_map(map.click_csjw, 160, 166, log="长寿郊外 -> 长寿村")
        b_move(0, 0, log="进入长寿村")
    while not is_place("方寸山"):
        b_move_map(map.click_csc, 110, 207, log="长寿村 -> 方寸山")
        b_move(0, 0, log="进入方寸山")
    while not is_place("方寸山殿"):
        b_move_map(map.click_fcs, 131, 137, log="方寸山 -> 方寸山殿")
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
