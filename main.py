import util
import auto
import ImgOperation
import test
import constants as c

if __name__ == '__main__':
    util.log_title("开始")
    auto.open_driver()
    while True:
        util.log_title("开始")
        if ImgOperation.crop4():
            n = test.recognize()
            if n == -1:
                util.log_title("未找到面向你的角色")
                break
            else:
                x, y = ImgOperation.find_xy_desktop(c.temp_crop4[n])
                auto.move_to(x, y)
                if ImgOperation.shot():
                    now_x, now_y = ImgOperation.find_mouse_in_desktop()
                    move_x = x - now_x + c.mouse_move_shape[0]
                    move_y = y - now_y + c.mouse_move_shape[1]
                    auto.move_rel_click(move_x, move_y)
        util.log_title("结束")
