"""
厢房
"""
from utils.component import Map, Bag, Mission
from utils.mouse import *

map = Map()
bag = Bag()
mission = Mission()

if __name__ == '__main__':
    bag.right_click(1, 5)  # 点击旗子
    move_left_click(0, 0)  # TODO 点击帮派坐标

