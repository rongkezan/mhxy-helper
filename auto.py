from ctypes import *
import time
from ImgOperation import *
import pyautogui

driver = windll.LoadLibrary(c.dd_dll_path)


def load_driver():
    global driver
    driver = windll.LoadLibrary(c.dd_dll_path)
    # 初始化DD鼠键模拟
    st = driver.DD_btn(0)
    if st == 1:
        print("DD loaded")
    else:
        print("Error")
        exit(101)


def left_click():
    driver.DD_btn(1)
    time.sleep(0.1)
    driver.DD_btn(2)


def right_click():
    driver.DD_btn(4)
    time.sleep(0.1)
    driver.DD_btn(8)


def keyboard(code):
    driver.DD_key(code, 1)
    time.sleep(0.1)
    driver.DD_key(code, 2)


def keyboard2(code1, code2):
    driver.DD_key(code1, 1)
    driver.DD_key(code2, 1)
    time.sleep(0.1)
    driver.DD_key(code2, 2)
    time.sleep(0.1)
    driver.DD_key(code1, 2)


def move(rect, x, y):
    # 最终需要移动到的坐标
    x_target, y_target = direct_move(rect, x, y)
    # 实际移动到的坐标
    time.sleep(0.2)
    shot()
    xy_mouse = find_mouse_desktop()
    if xy_mouse is not None:
        time.sleep(0.5)
        # 需要相对移动的坐标
        x_rel = x_target - xy_mouse[0]
        y_rel = y_target - xy_mouse[1]
        pyautogui.moveRel(x_rel, y_rel, 0.1)


def direct_move(rect, x, y):
    x_target = rect[0] + x
    y_target = rect[1] + y
    pyautogui.moveTo(x_target, y_target, 0.1)
    return x_target, y_target


def move_left_click(rect, x, y, direct=False):
    if direct:
        direct_move(rect, x, y)
    else:
        move(rect, x, y)
    left_click()
    time.sleep(0.5)


def move_right_click(rect, x, y, direct=False):
    if direct:
        direct_move(rect, x, y)
    else:
        move(rect, x, y)
    right_click()
    time.sleep(0.2)


def alt_q():
    keyboard2(604, 301)
    time.sleep(0.1)


def alt_a():
    keyboard2(604, 401)
    time.sleep(0.1)


def alt_e():
    keyboard2(604, 303)
    time.sleep(0.1)


def alt_d():
    keyboard2(604, 403)
    time.sleep(0.1)


def tab():
    keyboard(300)
    time.sleep(0.1)


def f9():
    keyboard(109)
    time.sleep(0.1)


def f6():
    keyboard(106)
    time.sleep(0.1)
