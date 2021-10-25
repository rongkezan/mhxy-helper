import util
import auto
import snap_4 as snap
import test


if __name__ == '__main__':
    util.log_title("开始")
    auto.open_driver()
    while True:
        util.log_h1_start(f'开始')
        if snap.task():
            result = test.recognize()
            if result == -1:
                util.log_title("未找到面向你的角色")
                break



