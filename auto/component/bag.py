import os
import auto.utils.log as log
from auto.component.action import action
from auto.component.camera import camera
import constants.path as p


class Bag:
    def __init__(self):
        self.title_pic = os.path.join(p.flag_common_dir, "bag_title.png")
        self.content_pic = os.path.join(p.temp_common_dir, "bag_content.png")
        self.stride = 50  # 步长
        self.x0 = 0  # 背包第一个格子的x坐标
        self.y0 = 0  # 背包第一个格子的y坐标
        self.left_top = (0, 0)  # 背包的左上坐标

    def right_click(self, bx, by):
        if bx > 5 | bx < 1 | by > 4 | by < 1:
            log.info("背包格子的范围是x∈[1,5] y∈[1,4]")
            return
        if not self.__is_bag_open():
            action.alt_e()
        self.__init_bag()

        move_x = self.x0 + self.stride * (bx - 1)
        move_y = self.y0 + self.stride * (by - 1)
        action.move_right_click(move_x, move_y)
        action.alt_e()

    def is_item_exist(self, item_path):
        """
        判断背包物品是否存在
        """
        if not self.__is_bag_open():
            action.alt_e()
        self.__shot_bag()
        _, score = camera.template_match(item_path, self.content_pic)
        if self.__is_bag_open():
            action.alt_e()
        if score >= 3:
            return True
        return False

    def __init_bag(self):
        camera.shot()
        shape, score = camera.template_match(self.title_pic, p.temp_game)
        if score >= 3:
            offset = (25, 217)
            self.x0 = shape[0] + offset[0]
            self.y0 = shape[1] + offset[1]
            self.left_top = (shape[0], shape[1])
        else:
            log.error("背包未打开")

    def __is_bag_open(self):
        camera.shot()
        _, score = camera.template_match(self.title_pic, p.temp_game)
        print(score)
        return score >= 3

    def __shot_bag(self):
        camera.game_shot((0, 0, 0, 0), self.content_pic)


bag = Bag()
