import os
import utils.constants as c
from utils.game_action import move_right_click, alt_e
from utils.window import template_match


class Bag:
    def __init__(self):
        self.bag_title_path = os.path.join(c.flag_dir, "bag_title.png")
        self.stride = 50
        self.x0 = 0     # 背包第一个格子的x坐标
        self.y0 = 0     # 背包第一个格子的y坐标

    def right_click(self, bx, by):
        if not self.bag_is_open():
            alt_e()
            move_x = self.x0 + self.stride * bx
            move_y = self.x0 + self.stride * by
            move_right_click(move_x, move_y)
        if self.bag_is_open():
            alt_e()

    def bag_is_open(self):
        shape, score = template_match(self.bag_title_path, c.temp_game)
        if score >= 5:
            sub_shape = (0, 0, 0, 0)
            self.x0 = shape[0] + sub_shape[0]
            self.y0 = shape[1] + sub_shape[1]
            return True
        return False
