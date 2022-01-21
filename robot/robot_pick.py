"""
宝图分拣
"""
import os
import utils.log as log
import constants.path as path
from component.action import Action
from component.camera import Camera

action = Action()
camera = Camera()


class Pick:
    def __init__(self):
        self.treasure_map_pic = os.path.join(path.flag_dir, "treasure_map.png")
        self.warehouse_title = os.path.join(path.flag_dir, "warehouse_title.png")
        self.warehouse_left = os.path.join(path.temp_dir, "warehouse_left.png")
        self.warehouse_right = os.path.join(path.temp_dir, "warehouse_right.png")
        self.house_offset = (0, 80)
        self.bag_offset = (305, 80)
        self.bag_shape = (260, 210)
        self.house_nums = {
            1: (15, 20), 2: (35, 20), 3: (55, 20), 4: (75, 20), 5: (95, 20), 6: (115, 20), 7: (135, 20),
            8: (15, 57), 9: (35, 57), 10: (55, 57), 11: (75, 57), 12: (95, 57), 13: (115, 57), 14: (135, 57),
            15: (155, 57), 16: (175, 57), 17: (15, 85), 18: (35, 85), 19: (55, 85), 20: (75, 85), 21: (95, 85),
            22: (115, 85), 23: (135, 85), 24: (155, 85), 25: (175, 85)}
        self.treasure_house = {
            "建邺": 8, "长寿村": 9, "傲来": 10, "朱紫": 11, "东海": 12, "野外": 13, "国境": 14, "境外": 15, "郊外": 16,
            "麒麟": 17, "花果": 18, "北俱": 19, "墨家": 20, "普陀": 21, "狮驼": 22, "女儿": 23, "五庄": 24}

    def switch(self, num):
        camera.shot()
        shape, score = camera.template_match(self.warehouse_title, path.temp_game)
        if score >= 3:
            xt, yt = shape[0], shape[1]
            width, height = 195, 100
            x0, y0 = xt, yt + 290
            shape = (x0, y0, xt + width, y0 + height)
            camera.game_shot(shape, os.path.join(path.temp_dir, "warehouse_num.png"))
            log.info("切换到仓库:", num)
            action.move_left_click(x0 + self.house_nums[num][0], y0 + self.house_nums[num][1])

    def get_all_item(self, pic):
        camera.shot()
        shape, score = camera.template_match(self.warehouse_title, path.temp_game)
        if score >= 3:
            xt, yt = shape[0], shape[1]
            shape_left = (
                xt + self.house_offset[0], yt + self.house_offset[1], xt + self.house_offset[0] + self.bag_shape[0],
                yt + self.house_offset[1] + self.bag_shape[1])
            camera.game_shot(shape_left, self.warehouse_left)
            for i in range(20):
                camera.shot()
                shape, score = camera.template_match(pic, self.warehouse_left)
                if score >= 3:
                    x, y = shape[0], shape[1]
                    action.move_right_click(shape_left[0] + x, shape_left[1] + y)
                else:
                    log.info("该仓库不存在物品:", pic)
                    break

    def treasure_pick(self):
        camera.shot()
        shape, score = camera.template_match(self.warehouse_title, path.temp_game)
        if score >= 3:
            xt, yt = shape[0], shape[1]
            shape_right = (
                xt + self.bag_offset[0], yt + self.bag_offset[1], xt + self.bag_offset[0] + self.bag_shape[0],
                yt + self.bag_offset[1] + self.bag_shape[1])
            camera.game_shot(shape_right, self.warehouse_right)
            for i in range(20):
                result = camera.template_match(self.treasure_map_pic, self.warehouse_right)
                if result is not None:
                    x, y = shape_right[0] + result[0], shape_right[1] + result[1]
                    action.move_game(x, y)
                    text = camera.read_text_basic(self.warehouse_right)
                    places = self.treasure_house.keys()
                    for place in places:
                        if text.__contains__(place):
                            self.switch(self.treasure_house[place])
                            action.move_left_click(x, y)

    def run(self):
        buffer = [2, 3, 4, 5, 6, 7]
        for b in buffer:
            self.switch(b)
            self.get_all_item(self.treasure_map_pic)
            self.treasure_pick()


if __name__ == '__main__':
    pick = Pick()
    pick.run()
