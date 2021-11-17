from utils.mission import Mission
from utils.map import *
from utils.game_watcher import *
from utils.game_action import *
from utils.bag import Bag

def find_yz():
    for yz in c.flag_yz:
        res = find_xy_in_game(yz)
        if res is not None:
            return res
    return None


if __name__ == '__main__':
    mission = Mission()
    bag = Bag()
    load_driver()
    print(">>> 点击长安导标旗")
    bag.right_click(1, 1)
    move_left_click(521, 539)

    while True:
        time.sleep(1)
        print("检查摄妖香")
        alt_q()
        mission.shot_mission()
        alt_q()
        words = read_text_basic(mission.content_path)
        if not words.__contains__("摄妖香"):
            print("补充摄妖香")
            alt_e()
            move_right_click(263, 597)
            alt_e()
        f9()
        print("寻找驿站车夫")
        res = find_yz()
        if res is not None:
            print("点击驿站车夫")
            move_left_click(res[0], res[1])
            break

    move_left_click(268, 472)
    MapDTGJ().click(48, 332)
    if arrived():
        move_left_click(485, 127)
    MapDF().click(50, 55)
    if arrived():
        f9()
        while True:
            time.sleep(1)
            res = find_xy_in_game(os.path.join(c.flag_character_dir, "zk.png"))
            if res is not None:
                move_left_click(res[0], res[1])
                break
    move_left_click(276, 476)