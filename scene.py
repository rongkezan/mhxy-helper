from auto import *
import random
from DataCollector import *
from window import *

hwnd_title = dict()
rect = None


def save_temp_ch():
    shot()
    Image.open(c.temp_game).crop((20, 33, 780, 53)).save(c.ch_temp_img)
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch1'][0]).save(c.ch_dict['ch1'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch2'][0]).save(c.ch_dict['ch2'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch3'][0]).save(c.ch_dict['ch3'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch4'][0]).save(c.ch_dict['ch4'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch5'][0]).save(c.ch_dict['ch5'][1])


def is_notify():
    shot()
    save_temp_ch()
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
    shot()
    save_temp_ch()
    img = cv.imread(c.ch_dict['ch1'][1])
    return (img[10][115] == [221, 221, 221]).all()


def move_around():
    tab()
    rd = int(random.random() * 10)
    print(rect)
    if rd < 3:
        move_left_click(rect, 429, 301)
    elif rd < 5:
        move_left_click(rect, 210, 398)
    elif rd < 8:
        move_left_click(rect, 393, 500)
    else:
        move_left_click(rect, 399, 366)
    tab()
    time.sleep(3)


def ready_fight():
    Image.open(c.temp_game).crop((673, 220, 735, 500)).save("img/temp/temp_fight_tool.png")
    score = compare_image("img/flag/flag_fight_tool.png", "img/temp/temp_fight_tool.png")
    if score > 0.95:
        return True
    return False


if __name__ == '__main__':
    load_driver()
    while True:
        print(">>> 状态判断 >>>")
        time.sleep(2)

        notify = is_notify()
        while notify:
            print(">>> 有通知, 坐标" + notify + " >>>")
            move_left_click(rect, notify[0], notify[1], True)
            if is_fight() & is_popup():
                print(">>> 战斗出现弹框，保存4小人图片 >>>")
                if is_not_same_fight():
                    shutil.copy(c.temp_popup, os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".jpg"))
                break

        while not leader_is_active():
            print(">>> 选择队长 >>>")
            move_left_click(rect, c.ch_dict['ch1'][2][0], c.ch_dict['ch1'][2][1], True)

        while is_fight():
            print(">>> 战斗状态 >>>")
            for k in c.ch_dict:
                move_left_click(rect, c.ch_dict[k][2][0], c.ch_dict[k][2][1], True)
                if ready_fight():
                    print(">>> 攻击/施法 >>>")
                    alt_q()
                    alt_a()
            break

        while not is_fight():
            print(">>> 非战斗状态，晃悠晃悠 >>>")
            move_around()
