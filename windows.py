from Auto import *
import random

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
    shot1()
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
    print("自动状态得分:", score)
    if score >= 4:
        return True
    else:
        return False


def leader_is_active():
    img = cv.imread(c.ch_dict['ch1'][1])
    return (img[10][115] == [221, 221, 221]).all()


def click_auto_fight():
    shot()
    while is_fight():
        if is_auto_fight():
            print(">>> 已经处于自动状态 >>>")
            return
        elif is_popup():
            # TODO 利用模型训练
            print("出现弹框 Pass")
            pass
        else:
            print(">>> 点击自动 >>>")
            move_left_click(rect, 705, 439)  # 点击自动


def switch_map():
    keyboard(300)
    time.sleep(0.5)


def move_around():
    print(">>> 晃悠中 >>>")
    switch_map()
    rd = int(random.random() * 10)
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
        print(">>> 检测人物框通知 >>>")
        time.sleep(2)
        save_temp_ch()
        for k in c.ch_dict:
            if is_notify():
                print(">>> 通知点击坐标: ", c.ch_dict[k][2], " >>>")
                move_left_click(rect, c.ch_dict[k][2][0], c.ch_dict[k][2][1], True)
                click_auto_fight()

        print(">>> 队员没通知，选择队长 >>>")
        shot()
        if not leader_is_active():
            move_left_click(rect, c.ch_dict['ch1'][2][0], c.ch_dict['ch1'][2][1], True)
            shot()
        click_auto_fight()
        if not is_fight():
            while True:
                move_around()
                if is_fight():
                    break
