from ctypes import *
import constants as c
import time

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
    time.sleep(0.05)
    driver.DD_btn(2)


def right_click():
    driver.DD_btn(4)
    time.sleep(0.05)
    driver.DD_btn(8)


def move_to(x, y):
    driver.DD_mov(x, y)


def move_to_r(x, y):
    driver.DD_movR(x, y)


def keyboard(code):
    driver.DD_key(code, 1)
    time.sleep(0.05)
    driver.DD_key(code, 2)


if __name__ == '__main__':
    load_driver()
