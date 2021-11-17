import os
import utils.constants as c
from utils.game_action import move_right_click, alt_e
from utils.window import template_match, shot


class Bag:
    def __init__(self):
        self.bag_title_path = os.path.join(c.flag_dir, "bag_title.png")
        self.stride = 53
        self.x0 = 0     # 背包第一个格子的x坐标
        self.y0 = 0     # 背包第一个格子的y坐标

    def right_click(self, bx, by):
        if bx > 5 | bx < 1 | by > 4 | by < 1:
            print("背包格子的范围是x∈[1,5] y∈[1,4]")
            return
        if not self.bag_is_open():
            alt_e()
        self.init_bag()
        move_x = self.x0 + self.stride * (bx - 1)
        move_y = self.y0 + self.stride * (by - 1)
        print(self.x0, self.y0)
        print(move_x, move_y)
        move_right_click(move_x, move_y)
        if self.bag_is_open():
            alt_e()

    def init_bag(self):
        shot()
        shape, score = template_match(self.bag_title_path, c.temp_game)
        if score >= 5:
            offset = (25, 217)
            self.x0 = shape[0] + offset[0]
            self.y0 = shape[1] + offset[1]
        else:
            print("[Error] 背包未打开")

    def bag_is_open(self):
        shot()
        _, score = template_match(self.bag_title_path, c.temp_game)
        if score >= 5:
            return True
        return False
