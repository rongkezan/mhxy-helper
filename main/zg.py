# from utils.mission import Mission
# from utils.map import *
# from utils.game_watcher import *
# from utils.game_action import *
# from utils.bag import Bag
from utils.txt import *
import re

places1 = [("建邺城", 0, 0),
           ("傲来国", 223, 150),
           ("朱紫国", 163, 191),
           ("长寿村", 0, 0),
           ("西凉女国", 163, 123),
           ("宝象国", 159, 119),
           ("江南野外", 159, 119),
           ("大唐境外", 638, 110),
           ("普陀山", 0, 0),
           ("五庄观", 0, 0)]
places2 = [
    ("花果山", 159, 119),
    ("北俱芦洲", 227, 169),
    ("女娲神迹", 0, 0),
    ("麒麟山", 190, 141),
    ("海底迷宫一层", 0, 0),
    ("地狱迷宫三层", 0, 0)]


# def find_yz():
#     for yz in c.flag_yz:
#         res = find_xy_in_game(yz)
#         if res is not None:
#             return res
#     return None


def get_mission():
    words = read_text_basic('../resources/img/mission/1.png')
    words = words.split('分钟效果')
    syx_time = words[0].split("摄妖香还有")[1]
    print("摄妖香时间:", syx_time)
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
    print(place1, place2)
    pos1 = get_position(words1)
    pos2 = get_position(words2)

    if len(pos1) > 1:
        for p in pos1:
            print(p)
            if p[0] <= place1[1]:
                if p[1] <= place1[2]:
                    pos1 = (p[0], p[1])
                break
    else:
        pos1 = pos1[0][0], pos1[0][1]
    if len(pos2) > 1:
        for p in pos2:
            if p[0] <= place2[1] & p[1] <= place2[2]:
                pos2 = (p[0], p[1])
                break
    else:
        pos2 = pos2[0][0], pos2[0][1]
    print(pos1, pos2)


def get_position(text_list):
    text_list = text_list.split(",")
    if len(text_list) == 2:
        return tuple([text_list[0], text_list[1]])
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
            return int(text[0]) * 10 + int(text[1]), int(text[2])
        elif len(text) == 4:
            return (int(text[0]) * 10 + int(text[1]), int(text[2]) * 10 + int(text[3])), \
                   (int(text[0]), int(text[1]) * 100 + int(text[2]) * 10 + int(text[3])), \
                   (int(text[0]) * 100 + int(text[1]) * 10 + int(text[2]), int(text[3]))
        elif len(text) == 5:
            return (int(text[0]) * 100 + int(text[1]) * 10 + int(text[2], int(text[3]) * 10 + int(text[4]))), \
                   (int(text[0]) * 10 + int(text[1]), int(text[2]) * 100 + int(text[3]) * 10 + int(text[4]))
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
    get_mission()
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
