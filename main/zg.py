# from utils.mission import Mission
# from utils.map import *
# from utils.game_watcher import *
# from utils.game_action import *
# from utils.bag import Bag
from utils.txt import *
import re

places1 = [("jy", "建邺", 1000, 1000),
           ("al", "傲来", 223, 150),
           ("zz", "朱紫", 163, 191),
           ("cs", "长寿村", 1000, 1000),
           ("xl", "西凉", 163, 123),
           ("bx", "象国", 159, 119),
           ("yw", "南野外", 159, 119),
           ("jw", "唐境外", 638, 110),
           ("pt", "普陀山", 1000, 1000),
           ("wz", "庄观", 1000, 1000)]
places2 = [
    ("花果山", 159, 119),
    ("北俱芦洲", 227, 169),
    ("女娲神迹", 1000, 1000),
    ("麒麟山", 190, 141),
    ("海底迷宫一层", 1000, 1000),
    ("地狱迷宫三层", 1000, 1000)]


# def find_yz():
#     for yz in c.flag_yz:
#         res = find_xy_in_game(yz)
#         if res is not None:
#             return res
#     return None


def get_mission(path):
    words = read_text_basic(path)
    words = words.split('分钟效果')
    syx_time = words[0].split("摄妖香还有")[1]
    words = words[1]
    words1 = words.split('去')[1]
    words1 = words1.split('处抓')[0]
    words2 = words.split('去')[2]
    words2 = words2.split('降服')[0]

    place1 = None
    place2 = None

    for place in places1:
        if words1.__contains__(place[0]):
            place1 = place
            words1 = words1.replace(place1[0], "")
            break

    for place in places2:
        if words2.__contains__(place[0]):
            place2 = place
            words2 = words2.replace(place2[0], "")
            break
    pos1 = get_position(words1)
    pos2 = get_position(words2)
    print(pos1, pos2)
    # if len(pos1) > 1:
    #     for p in pos1:
    #         if p[0] <= place1[1] and p[1] <= place1[2]:
    #             pos1 = (p[0], p[1])
    #             break
    # else:
    #     pos1 = pos1[0][0], pos1[0][1]
    # if len(pos2) > 1:
    #     for p in pos2:
    #         if p[0] <= place2[1] and p[1] <= place2[2]:
    #             pos2 = (p[0], p[1])
    #             break
    # else:
    #     pos2 = pos2[0][0], pos2[0][1]
    # print(('摄妖香', syx_time), (place1[0], pos1), (place2[0], pos2))


def get_position(text_list):
    text_list = text_list.split(",")
    if len(text_list) == 2:
        return tuple([int(text_list[0]), int(text_list[1])])
    elif len(text_list) > 2:
        pos = []
        for t in text_list:
            if is_number(t):
                pos.append(int(t))
        return tuple([pos])
    else:
        text = ""
        for t in text_list:
            text += t
        text = re.sub("\D", "", text)
        if len(text) == 2:
            return int(text[0]), int(text[1])
        elif len(text) == 3:
            t0 = int(text[0])
            t1 = int(text[1])
            t2 = int(text[2])
            return (t0 * 10 + t1), (t0, t1 * 10 + t2)
        elif len(text) == 4:
            t0 = int(text[0])
            t1 = int(text[1])
            t2 = int(text[2])
            t3 = int(text[3])
            return (t0, t1 * 100 + t2 * 10 + t3), (t0 * 10 + t1, t2 * 10 + t3), (t0 * 100 + t1 * 10 + t2, t3)
        elif len(text) == 5:
            t0 = int(text[0])
            t1 = int(text[1])
            t2 = int(text[2])
            t3 = int(text[3])
            t4 = int(text[4])
            return (t0 * 10 + t1, t2 * 100 + t3 * 10 + t4), (t0 * 100 + t1 * 10 + t2, t3 * 10 + t4)
        elif len(text) == 6:
            return int(text[0]) * 100 + int(text[1]) * 10 + int(text[2]), int(text[3]) * 100 + int(text[4]) * 10 + int(
                text[5])


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


if __name__ == '__main__':
    for i in range(10):
        get_mission("../resources/img/mission/" + str(i + 1) + ".png")
        print()
    # map = Map()
    # mission = Mission()
    # bag = Bag()
    # load_driver()
    # print(">>> 点击长安导标旗")
    # bag.right_click(1, 1)
    # move_left_click(521, 539)
    #
    # while True:
    #     time.sleep(1)
    #     print("检查摄妖香")
    #     alt_q()
    #     mission.shot_mission()
    #     alt_q()
    #     words = read_text_basic(mission.content_path)
    #     if not words.__contains__("摄妖香"):
    #         print("补充摄妖香")
    #         alt_e()
    #         move_right_click(263, 597)
    #         alt_e()
    #     f9()
    #     print("寻找驿站车夫")
    #     res = find_yz()
    #     if res is not None:
    #         print("点击驿站车夫")
    #         move_left_click(res[0], res[1])
    #         break
    #
    # move_left_click(268, 472)
    # map.click_dtgj(48, 332)
    # if arrived():
    #     move_left_click(485, 127)
    # map.click_df(50, 55)
    # if arrived():
    #     f9()
    #     while True:
    #         time.sleep(1)
    #         res = find_xy_in_game(os.path.join(c.flag_character_dir, "zk.png"))
    #         if res is not None:
    #             move_left_click(res[0], res[1])
    #             break
    # move_left_click(276, 476)
