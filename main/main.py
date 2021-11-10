import sys
from scene.main import task
from pynput.keyboard import Listener, Key

launch = 1


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
