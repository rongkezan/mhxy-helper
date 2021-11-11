from utils.auto import *
from utils.game_watcher import *


class MapCa:
    def __init__(self):
        self.shape = (245, 310, 790, 587)
        self.x0 = 243
        self.y0 = 586
        self.width = 545
        self.height = 277

    def click(self, x, y):
        if not map_is_open():
            tab()
        if x > self.width | y > self.height:
            print("坐标超出地图范围:", x, y)
        else:
            move_x = self.x0 + x
            move_y = self.y0 - y
            move_left_click(move_x, move_y)
        tab()


if __name__ == '__main__':
    map_ca = MapCa()
    map_ca.click(200,200)
