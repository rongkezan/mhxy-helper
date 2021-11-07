from Auto import *
import random
from DataCollector import *

hwnd_title = dict()
rect = None


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def shot():
    global rect
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t.startswith('梦幻西游 ONLINE'):
            app = QApplication(sys.argv)
            desktop_id = app.desktop().winId()
            screen = QApplication.primaryScreen()
            temp_desktop = screen.grabWindow(desktop_id).toImage()
            temp_game = screen.grabWindow(h).toImage()
            temp_desktop.save(c.temp_desktop)
            temp_game.save(c.temp_game)
            rect = win32gui.GetWindowRect(h)


def save_temp_ch():
    shot()
    Image.open(c.temp_game).crop((20, 33, 780, 53)).save(c.ch_temp_img)
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch1'][0]).save(c.ch_dict['ch1'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch2'][0]).save(c.ch_dict['ch2'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch3'][0]).save(c.ch_dict['ch3'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch4'][0]).save(c.ch_dict['ch4'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch5'][0]).save(c.ch_dict['ch5'][1])


def is_notify():
    img = cv.imread(c.ch_dict[k][1])
    return (img[10][115] == [155, 202, 254]).all()


def is_auto_fight():
    shape, score = template_match(c.flag_auto_fight, c.temp_game)
    if score >= 4:
        return True
    else:
        return False


def leader_is_active():
    img = cv.imread(c.ch_dict['ch1'][1])
    return (img[10][115] == [221, 221, 221]).all()


def alt_q_a():
    keyboard2(604, 301)
    time.sleep(0.1)
    keyboard2(604, 301)
    time.sleep(0.1)
    keyboard2(604, 401)
    time.sleep(0.1)
    keyboard2(604, 401)
    time.sleep(0.1)


def click_auto_fight():
    shot()
    while is_fight():
        print(">>> 战斗状态 >>>")
        time.sleep(1)
        if is_auto_fight():
            print(">>> 已经处于自动状态 >>>")
            return
        if is_popup():
            print(">>> 出现弹框 >>>")
            # 保存4小人图片
            if is_not_same_fight():
                shutil.copy(c.temp_popup, os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".jpg"))
            break
        else:
            for k in c.ch_dict:
                shape = (673, 220, 735, 500)
                Image.open(c.temp_game).crop(shape).save("img/temp/temp_fight_tool.png")
                score = compare_image("img/flag/flag_fight_tool.png", "img/temp/temp_fight_tool.png")
                if score > 0.95:
                    print(">>> 攻击/施法 >>>")
                    move_left_click(rect, c.ch_dict[k][2][0], c.ch_dict[k][2][1], True)
                    alt_q_a()
            break
            # print(">>> 点击自动 >>>")
            # move_left_click(rect, 705, 439)  # 点击自动


def switch_map():
    keyboard(300)
    time.sleep(0.5)


def move_around():
    print(">>> 晃悠中 >>>")
    switch_map()
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
    switch_map()
    time.sleep(3)


if __name__ == '__main__':
    load_driver()
    while True:
        print(">>> 状态判断 >>>")
        time.sleep(2)
        save_temp_ch()
        # for k in c.ch_dict:
        #     if is_notify():
        #         print(">>> 通知点击坐标: ", c.ch_dict[k][2], " >>>")
        #         move_left_click(rect, c.ch_dict[k][2][0], c.ch_dict[k][2][1], True)
        #         click_auto_fight()

        shot()
        if not leader_is_active():
            print(">>> 选择队长 >>>")
            move_left_click(rect, c.ch_dict['ch1'][2][0], c.ch_dict['ch1'][2][1], True)
            shot()
        click_auto_fight()
        if not is_fight():
            print(">>> 非战斗状态 >>>")
            while True:
                move_around()
                if is_fight():
                    break
