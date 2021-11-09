from auto import *
from DataCollector import *
from window import *
from txt import *
from pynput.keyboard import Listener, Key
import cv2 as cv
import _thread

hwnd_title = dict()
rect = None
move_around_count = 0
launch = 1


def need_heal():
    shot_status()
    img = cv.imread("img/temp/status.png")
    print(img[15][15])
    if not (img[15][15][0] == 255):
        return True
    return False


def is_notify():
    shot_tag()
    for k in c.ch_dict:
        img = cv.imread(c.ch_dict[k][1])
        if (img[10][115] == [155, 202, 254]).all():
            return c.ch_dict[k][2]
    return False


def is_auto_fight():
    shape, score = template_match(c.flag_auto_fight, c.temp_game)
    if score >= 4:
        return True
    else:
        return False


def leader_is_active():
    shot_tag()
    img = cv.imread(c.ch_dict['ch1'][1])
    return (img[10][115] == [221, 221, 221]).all()


def move_around():
    global move_around_count
    tab()
    if move_around_count == 0:
        move_left_click(rect, 429, 301)
        move_around_count = 1
    elif move_around_count == 1:
        move_left_click(rect, 210, 398)
        move_around_count = 2
    elif move_around_count == 2:
        move_left_click(rect, 393, 500)
        move_around_count = 3
    else:
        move_left_click(rect, 399, 366)
        move_around_count = 1
    tab()
    time.sleep(3)


def ready_fight():
    shot_fight_tool()
    score = compare_image("img/flag/fight_tool.png", "img/temp/fight_tool.png")
    if score > 0.95:
        return True
    return False


def task():
    load_driver()
    rect = get_rect()
    heal_flag = 0
    while True:
        print(">>> 状态判断 >>>")
        time.sleep(2)

        while not leader_is_active():
            print(">>> 选择队长 >>>")
            move_left_click(rect, c.ch_dict['ch1'][2][0], c.ch_dict['ch1'][2][1], True)

        need_shot_monster = 0
        need_shot_popup1 = 0
        need_shot_popup2 = 0
        while is_fight():
            print(">>> 战斗状态 >>>")
            time.sleep(1)

            # 识别怪物
            pause_flag = 0
            if need_shot_monster == 0:
                need_shot_monster = 1
                shot_monster()
                words = read_text_basic("img/temp/monster.png")
                print("识别怪物:", words)
                for word in words:
                    if word.__contains__("宝宝"):
                        print(">>> 需要抓捕召唤兽:", word, " >>>")
                        pause_flag = 1
                        # break
                        sys.exit()

            # 识别队长是否有4小人弹窗
            if need_shot_popup1 == 0:
                if is_popup():
                    need_shot_popup1 = 1
                    print(">>> 战斗出现弹框，保存4小人图片 >>>")
                    if is_not_same_fight():
                        shutil.copy(c.temp_popup,
                                    os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".jpg"))
                    # break
                    sys.exit()

            # 识别队员是否有4小人弹窗
            if need_shot_popup2 == 0:
                need_shot_popup2 = 1
                notify = is_notify()
                while notify:
                    time.sleep(1)
                    print(">>> 有通知, 坐标:", notify, " >>>")
                    move_left_click(rect, notify[0], notify[1], True)
                    if is_popup():
                        print(">>> 战斗出现弹框，保存4小人图片 >>>")
                        if is_not_same_fight():
                            shutil.copy(c.temp_popup,
                                        os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".jpg"))
                        # break
                        sys.exit()

            # 攻击施法
            if pause_flag == 0:
                if ready_fight():
                    for k in c.ch_dict:
                        move_left_click(rect, c.ch_dict[k][2][0], c.ch_dict[k][2][1], True)
                        print(">>> 攻击/施法 >>>")
                        alt_q()
                        alt_d()

        while not is_fight():
            if heal_flag % 10 == 0:
                print(">>> 10轮战斗定期检查人物血蓝 >>>")
                heal_flag += 1
                for k in c.ch_dict:
                    move_left_click(rect, c.ch_dict[k][2][0], c.ch_dict[k][2][1], True)
                    if need_heal():
                        f6()
                        move_left_click(rect, 183, 447)

            print(">>> 非战斗状态，晃悠晃悠 >>>")
            move_left_click(rect, c.ch_dict['ch1'][2][0], c.ch_dict['ch1'][2][1], True)
            move_around()


def press(key):
    global launch
    if key == Key.f12:
        if launch == 1:
            print("---- 启动脚本 ----")
            task()
            launch = 0
        else:
            print("---- 关闭脚本 ----")
            sys.exit()


if __name__ == '__main__':
    print("--- 程序启动，按F12开始运行 ---")
    with Listener(on_press=press) as listener:
        listener.join()


