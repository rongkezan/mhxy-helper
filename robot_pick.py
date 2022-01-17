"""
宝图分拣
"""
from utils.action import *


class Warehouse:
    def __init__(self):
        self.treasure_map_pic = os.path.join(c.flag_dir, "treasure_map.png")  # TODO 截图
        self.house_x0 = 0  # TODO
        self.house_y0 = 0  # TODO
        self.bag_x0 = 0  # TODO
        self.bag_y0 = 0  # TODO
        self.house_nums = {  # TODO
            1: (0, 0), 2: (0, 0), 3: (0, 0), 4: (0, 0), 5: (0, 0),
            6: (0, 0), 7: (0, 0), 8: (0, 0), 9: (0, 0), 10: (0, 0),
            11: (0, 0), 12: (0, 0), 13: (0, 0), 14: (0, 0), 15: (0, 0),
            16: (0, 0), 17: (0, 0), 18: (0, 0), 19: (0, 0), 20: (0, 0),
            21: (0, 0), 22: (0, 0), 23: (0, 0), 24: (0, 0), 25: (0, 0)}
        self.treasure_house = {
            "建邺": 8, "长寿村": 9, "傲来": 10, "朱紫": 11, "东海": 12, "野外": 13, "国境": 14, "境外": 15, "郊外": 16,
            "麒麟": 17, "花果": 18, "北俱": 19, "墨家": 20, "普陀": 21, "狮驼": 22, "女儿": 23, "五庄": 24}

    def switch(self, num):
        x, y = self.house_nums[num]
        info("切换到仓库:", num)
        move_left_click(x, y)

    def get_all(self, pic):
        path = shot_warehouse()
        for i in range(20):
            result = template_match(pic, path)
            if result is not None:
                x, y = result[0], result[1]
                move_right_click(self.house_x0 + x, self.house_y0 + y)
            else:
                info("该仓库不存在物品:", pic)
                break

    def treasure_pick(self):
        for i in range(20):
            result = find_xy_in_warehouse_bag(self.treasure_map_pic)
            if result is not None:
                x, y = result[0], result[1]
                move_x, move_y = self.bag_x0 + x, self.bag_y0 + y
                move(move_x, move_y)
                path = shot_warehouse_bag()
                text = read_text_basic(path)
                places = self.treasure_house.keys()
                for place in places:
                    if text.__contains__(place):
                        self.switch(self.treasure_house[place])
                        move_left_click(move_x, move_y)
            else:
                break


if __name__ == '__main__':
    warehouse = Warehouse()
    buffer = [2, 3, 4, 5, 6, 7]
    for b in buffer:
        warehouse.switch(b)
        warehouse.get_all(warehouse.treasure_map_pic)
        warehouse.treasure_pick()