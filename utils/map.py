from utils.auto import *


class Ca:
    def __init__(self):
        self.shape = (245, 310, 790, 587)
        self.x0 = 244
        self.y0 = 586
        self.width = 545
        self.height = 277

    def click(self, x, y):
        if x > self.width | y > self.height:
            print("坐标超出地图范围:", x, y)
        else:
            move_x = self.x0 + x
            move_y = self.y0 - y
            move_left_click(move_x, move_y)
