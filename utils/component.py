from utils.action import Action
from utils.camera import Camera
import os
import constants as c
import utils.log as log


class Bag:
    def __init__(self):
        self.title_pic = os.path.join(c.flag_dir, "bag_title.png")
        self.content_pic = os.path.join(c.temp_dir, "bag_content.png")
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
        action.move_left_click(move_x, move_y)
        if self.__is_bag_open():
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
        shape, score = camera.template_match(self.title_pic, c.temp_game)
        if score >= 3:
            offset = (25, 217)
            self.x0 = shape[0] + offset[0]
            self.y0 = shape[1] + offset[1]
            self.left_top = (shape[0], shape[1])
        else:
            log.error("背包未打开")

    def __is_bag_open(self):
        _, score = camera.template_match(self.title_pic, c.temp_game)
        return score >= 3

    def __shot_bag(self):
        camera.game_shot((0, 0, 0, 0), self.content_pic)


class Mission:
    def __init__(self):
        self.path = ""
        self.shape = (0, 0, 0, 0)  # 任务追踪栏的shape

    def read(self):
        log.info("开始读取任务")
        self.__shot_mission()
        text = camera.read_text_basic(self.content_path)
        log.info("任务的内容是:", text)
        return text

    def click_target(self):
        pass

    def __shot_mission(self):
        """
        任务截图
        """
        camera.game_shot(self.shape, self.path)


class Map:
    def __init__(self):
        self.map_open_flag = os.path.join(c.flag_dir, "map_open.png")
        self.move_x = 0
        self.move_y = 0

    def click_cac(self, x, y):
        self.move_x = 133 + x
        self.move_y = 502 - y
        self.__open_map_click()

    def click_jyc(self, x, y):
        self.move_x = 127 + round(x * 556 / 287)
        self.move_y = 502 - round(y * 277 / 143)
        self.__open_map_click()

    def click_csc(self, x, y):
        self.move_x = 235 + round(x * 5 / 3)
        self.move_y = 555 - round(y * 5 / 3)
        self.__open_map_click()

    def click_alg(self, x, y):
        self.move_x = 163 + round(x * 412 / 223)
        self.move_y = 517 - round(y * 278 / 150)
        self.__open_map_click()

    def click_xlng(self, x, y):
        self.move_x = 184 + round(x * 372 / 163)
        self.move_y = 520 - round(y * 282 / 123)
        self.__open_map_click()

    def click_zzg(self, x, y):
        self.move_x = 149 + round(x * 372 / 163)
        self.move_y = 517 - round(y * 439 / 191)
        self.__open_map_click()

    def click_bxg(self, x, y):
        self.move_x = 149 + round(x * 440 / 159)
        self.move_y = 545 - round(y * 331 / 119)
        self.__open_map_click()

    def click_dtgj(self, x, y):
        self.move_x = 180 + round(x * 377 / 351)
        self.move_y = 559 - round(y * 361 / 335)
        self.__open_map_click()

    def click_dtjw(self, x, y):
        self.move_x = 113 + round(x * 583 / 638)
        self.move_y = 419 - round(y * 109 / 118)
        self.__open_map_click()

    def click_jnyw(self, x, y):
        self.move_x = 185 + round(x * 369 / 159)
        self.move_y = 516 - round(y * 274 / 119)
        self.__open_map_click()

    def click_csjw(self, x, y):
        self.move_x = 211 + round(x * 316 / 191)
        self.move_y = 517 - round(y * 277 / 167)
        self.__open_map_click()

    def click_bjlz(self, x, y):
        self.move_x = 186 + round(x * 367 / 227)
        self.move_y = 517 - round(y * 277 / 169)
        self.__open_map_click()

    def click_hgs(self, x, y):
        self.move_x = 185 + round(x * 369 / 159)
        self.move_y = 518 - round(y * 277 / 119)
        self.__open_map_click()

    def click_dhw(self, x, y):
        self.move_x = 231 + round(x * 276 / 119)
        self.move_y = 517 - round(y * 276 / 119)
        self.__open_map_click()

    def click_qls(self, x, y):
        self.move_x = 185 + round(x * 369 / 190)
        self.move_y = 517 - round(y * 276 / 141)
        self.__open_map_click()

    def click_df(self, x, y):
        self.move_x = 185 + round(x * 364 / 159)
        self.move_y = 517 - round(y * 279 / 119)
        self.__open_map_click()

    def click_stl(self, x, y):
        self.move_x = 185 + round(x * 369 / 131)
        self.move_y = 517 - round(y * 279 / 98)
        self.__open_map_click()

    def click_mwz(self, x, y):
        self.move_x = 185 + round(x * 371 / 119)
        self.move_y = 517 - round(y * 277 / 89)
        self.__open_map_click()

    def click_fcs(self, x, y):
        self.move_x = 214 + round(x * 311 / 187)
        self.move_y = 517 - round(y * 277 / 167)
        self.__open_map_click()

    def click_hss(self, x, y):
        self.move_x = 182 + round(x * 371 / 127)
        self.move_y = 517 - round(y * 278 / 95)
        self.__open_map_click()

    def click_dtgf(self, x, y):
        self.move_x = 149 + round(x * 440 / 164)
        self.move_y = 518 - round(y * 277 / 103)
        self.__open_map_click()

    def click_lg(self, x, y):
        self.move_x = 115 + round(x * 508 / 212)
        self.move_y = 518 - round(y * 278 / 115)
        self.__open_map_click()

    def click_nec(self, x, y):
        self.move_x = 208 + round(x * 322 / 127)
        self.move_y = 559 - round(y * 361 / 143)
        self.__open_map_click()

    def __open_map_click(self):
        if not self.__is_map_open():
            action.tab()
        action.move_left_click(self.move_x, self.move_y)
        if self.__is_map_open():
            action.tab()

    def __is_map_open(self):
        _, score = camera.template_match(self.map_open_flag, c.temp_game)
        return score >= 3


action = Action()
camera = Camera()
bag = Bag()
mission = Mission()
map = Map()
