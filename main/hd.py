from utils.watcher import *
from utils.action import *
from utils.component import Map, Bag, Mission
from main.pb import yz_transfer

bag = Bag()
mission = Mission()
map = Map()


if __name__ == '__main__':
    load_driver()
    info("点长安旗子")
    bag.right_click(1, 2)
    move_left_click(361, 384)
    f9()
    res = find_xy_in_game("../resources/img/flag/ch/xiong.png")
    if res is not None:
        info("点击任务人坐标:", res)
        move_left_click(res[0], res[1])
    info("接任务")
    move_left_click(274, 415)
    info("关闭对话框")
    move_left_click(456, 445)
    miss_text = mission.read_mission()
    if miss_text.__contains__("大唐官"):
        info("接到任务地点：大唐官府")
        bag.right_click(1, 2)
        move_left_click(445, 224)
        mission.click_mission()
    elif miss_text.__contains__("化生"):
        info("接到任务地点：化生寺")
        bag.right_click(1, 2)
        move_left_click(638, 224)
        mission.click_mission()
    elif miss_text.__contains__("女儿"):
        info("接到任务地点：女儿村")
        bag.right_click(4, 1)
        move_left_click(220, 237)
        mission.click_mission()
    elif miss_text.__contains__("盘丝"):
        info("接到任务地点：盘丝洞")
        bag.right_click(1, 1)
        move_left_click(416, 457)
        yz_transfer()
        mission.click_mission()
    elif miss_text.__contains__("方寸"):
        info("接到任务地点：方寸山")
        bag.right_click(2, 1)
        move_left_click(453, 190)
        mission.click_mission()
    elif miss_text.__contains__("五庄"):
        info("接到任务地点：五庄观")
        bag.right_click(1, 1)
        move_left_click(416, 457)
        yz_transfer()
        mission.click_mission()
    elif miss_text.__contains__("普陀"):
        info("接到任务地点：普陀山")
        bag.right_click(1, 1)
        move_left_click(146, 493)
        yz_transfer()
        mission.click_mission()
    elif miss_text.__contains__("狮驼"):
        info("接到任务地点：狮驼岭")
        bag.right_click(3, 1)
        move_left_click(146, 493)
        mission.click_mission()
    elif miss_text.__contains__("东海"):
        info("接到任务地点：东海龙宫")
        bag.right_click(4, 1)
        move_left_click(502, 468)
        mission.click_mission()

