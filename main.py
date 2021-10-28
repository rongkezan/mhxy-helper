import util
import auto
import ImgOperation
import test
import constants as c
import time

if __name__ == '__main__':
    util.log_title("开始")
    auto.open_driver()
    while True:
        time.sleep(3)
        if ImgOperation.crop4():
            result = test.recognize()
            if result == -1:
                util.log_title("未找到面向你的角色")
                break
            else:
                x, y = result
                auto.move_to(x, y)
                if ImgOperation.shot():
                    now_x, now_y = ImgOperation.find_mouse_in_desktop()
                    move_x = x - now_x + c.mouse_move_shape[0]
                    move_y = y - now_y + c.mouse_move_shape[1]
                    auto.move_rel_click(move_x, move_y)
        util.log_title("结束")
