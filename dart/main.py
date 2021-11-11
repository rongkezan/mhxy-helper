from dart.map import *
from utils.txt import *

target_npc_list = ["秦琼", "程咬金", "空度禅师", "孙婆婆", "东海龙王", "地藏王", "观音姐姐", "镇元大仙", "牛魔王",
                   "大大王", "二大王", "三大王", "杨戬", "李靖", "菩提祖师", "白晶晶", "花十娘"]


def get_mission():
    alt_e()
    move_right_click(61, 497)  # 点击导标旗
    alt_e()
    move_left_click(762, 426)  # 导标旗点击镖局
    move_left_click(557, 416)  # 进入镖局
    move_left_click(693, 421)  # 走向镖头
    time.sleep(5)
    f9()
    while True:
        print("寻找镖头中...")
        shot()
        result = find_xy_in_game("../resources/img/flag/biao_tou.png")
        if result is not None:
            x, y = result[0], result[1]
            print("找到镖头，位置:", x, y)
            move_left_click(x, y)
            break
        else:
            print("未找到镖头，继续寻找")
        time.sleep(3)
    move_left_click(355, 578)  # 选4级镖
    move_left_click(369, 504)  # 选4级镖二级菜单
    move_left_click(355, 578)  # 关闭对话框
    move_left_click(484, 663)  # 走向镖局门口
    move_left_click(606, 681)  # 走出镖局
    alt_q()
    shot_mission()
    mission = ""
    words = read_text_basic(os.path.join(c.temp_dir, "mission.png"))
    for word in words:
        for target_npc in target_npc_list:
            if word.__contains__(target_npc):
                mission = target_npc
    return mission


if __name__ == '__main__':
    load_driver()
    while True:
        mission = get_mission()
        if mission == "":
            print("未获取到任务")
            sys.exit()
        elif mission == "秦琼":
            qf()
        elif mission == "程咬金":
            dt()
        elif mission == "空度禅师":
            hs()
        elif mission == "白晶晶":
            ps(1)
        elif mission == "花十娘":
            ps(2)
        elif mission == "镇元大仙":
            wz()
        elif mission == "大大王":
            st(1)
        elif mission == "二大王":
            st(2)
        elif mission == "三大王":
            st(3)
        else:
            sys.exit()






