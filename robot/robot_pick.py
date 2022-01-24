"""
宝图分拣
"""
import os
import utils.log as log
import constants.path as p
from component.action import Action
from component.camera import Camera

action = Action()
camera = Camera()


class Pick:
    def __init__(self):
        self.treasure_map_pic = os.path.join(p.flag_common_dir, "treasure_map.png")
        self.treasure_map_info = os.path.join(p.temp_common_dir, "treasure_map_info.png")
        self.treasure_map_big = os.path.join(p.flag_common_dir, "treasure_map_big.png")
        self.warehouse_title = os.path.join(p.flag_common_dir, "warehouse_title.png")
        self.warehouse_left = os.path.join(p.temp_common_dir, "warehouse_left.png")
        self.warehouse_right = os.path.join(p.temp_common_dir, "warehouse_right.png")
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
        shape, score = camera.template_match(self.warehouse_title, p.temp_game)
        if score >= 3:
            xt, yt = shape[0], shape[1]
            width, height = 195, 100
            x0, y0 = xt, yt + 290
            shape = (x0, y0, xt + width, y0 + height)
            camera.game_shot(shape, os.path.join(p.temp_dir, "warehouse_num.png"))
            log.info("切换到仓库:", num)
            action.move_left_click(x0 + self.house_nums[num][0], y0 + self.house_nums[num][1])

    def get_all_item(self, pic):
        warehouse_shape = self.get_warehouse_shape(self.warehouse_left, (0, 80))
        if warehouse_shape is not None:
            for i in range(20):
                camera.shot()
                camera.game_shot(warehouse_shape, self.warehouse_left)
                result = camera.find_xy(self.treasure_map_pic, self.warehouse_left)
                if result is not None:
                    x, y = result[0] + warehouse_shape[0], result[1] + warehouse_shape[1]
                    action.move_right_click(x, y)
                else:
                    log.info("该仓库不存在物品:", pic)
                    break

    def treasure_pick(self):
        # 得到仓库右边界面的Shape
        warehouse_shape = self.get_warehouse_shape(self.warehouse_right, (305, 80))
        if warehouse_shape is not None:
            for i in range(20):
                camera.shot()
                camera.game_shot(warehouse_shape, self.warehouse_right)
                result = camera.find_xy(self.treasure_map_pic, self.warehouse_right)
                if result is not None:
                    x, y = result[0] + warehouse_shape[0], result[1] + warehouse_shape[1]
                    action.move_game(x, y)
                    camera.shot()
                    res = camera.find_left_top_in_game(self.treasure_map_big)
                    if res is not None:
                        camera.game_shot((res[0] + 70, res[1], res[0] + 250, res[1] + 70), self.treasure_map_info)
                        text = camera.read_text_basic(self.treasure_map_info)
                        places = self.treasure_house.keys()
                        success = False
                        for place in places:
                            if text.__contains__(place):
                                log.info("普通识别出藏宝图的位置为:", place)
                                self.switch(self.treasure_house[place])
                                action.move_right_click(x, y)
                                success = True
                        if not success:
                            text = camera.read_text_accurate(self.treasure_map_info)
                            for place in places:
                                if text.__contains__(place):
                                    log.info("精确识别出藏宝图的位置为:", place)
                                    self.switch(self.treasure_house[place])
                                    action.move_right_click(x, y)
                                    success = True
                        if not success:
                            log.error("未能识别的文本:\n", text)
                else:
                    log.info("该车图已分拣完成！")
                    break

    def get_warehouse_shape(self, save_path, offset):
        camera.shot()
        shape, score = camera.template_match(self.warehouse_title, p.temp_game)
        if score >= 3:
            width, height = 260, 210
            xt, yt = shape[0], shape[1]
            sub_shape = (
                xt + offset[0],
                yt + offset[1],
                xt + offset[0] + width,
                yt + offset[1] + height
            )
            camera.game_shot(sub_shape, save_path)
            return sub_shape
        return None

    def run(self):
        buffer = [6, 7]
        for b in buffer:
            self.switch(b)
            self.get_all_item(self.treasure_map_pic)
            self.treasure_pick()


if __name__ == '__main__':
    pick = Pick()
    pick.run()
