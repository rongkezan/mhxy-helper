from utils.action import *
from utils.watcher import *
from utils.txt import *


class Bag:
    def __init__(self):
        self.bag_title_path = os.path.join(c.flag_dir, "bag_title.png")
        self.bag_content_path = os.path.join(c.temp_dir, "bag_content.png")
        self.stride = 50  # 步长
        self.x0 = 0  # 背包第一个格子的x坐标
        self.y0 = 0  # 背包第一个格子的y坐标

    def right_click(self, bx, by):
        if bx > 5 | bx < 1 | by > 4 | by < 1:
            info("背包格子的范围是x∈[1,5] y∈[1,4]")
            return
        if not self.__is_bag_open():
            alt_e()
        self.__init_bag()
        move_x = self.x0 + self.stride * (bx - 1)
        move_y = self.y0 + self.stride * (by - 1)
        move_right_click(move_x, move_y)
        if self.__is_bag_open():
            alt_e()

    def is_item_exist(self, item_path):
        """
        判断背包物品是否存在
        """
        if not self.__is_bag_open():
            alt_e()
        self.__shot_bag()
        _, score = template_match(item_path, self.bag_content_path)
        if self.__is_bag_open():
            alt_e()
        if score >= 4:
            return True
        return False

    def __init_bag(self):
        shape, score = game_template_match(self.bag_title_path)
        if score >= 5:
            offset = (25, 217)
            self.x0 = shape[0] + offset[0]
            self.y0 = shape[1] + offset[1]
        else:
            error("背包未打开")

    def __is_bag_open(self):
        _, score = game_template_match(self.bag_title_path)
        return score >= 5

    def __shot_bag(self):
        # TODO 背包的Shape
        game_shot((0, 0, 0, 0), self.bag_content_path)


class Mission:
    def __init__(self):
        self.content_shape = (397, 263, 592, 494)
        self.title_shape = (341, 180, 483, 196)
        self.title_path = os.path.join(c.flag_dir, "mission_title.png")
        self.content_path = os.path.join(c.temp_dir, "mission_content.png")
        self.red = [1, 1, 255]

    def location(self, path):
        """
        定位红色任务字体坐标
        """
        img = cv.imread(path)
        for i in range(len(img)):
            for j in range(len(img[0])):
                if (img[i][j] == self.red).all():
                    return j, i

    def click_mission(self):
        if not self.__is_mission_open():
            alt_q()
        self.__shot_mission()
        x, y = self.location(self.content_path)
        move_x = self.content_shape[0] + x
        move_y = self.content_shape[1] + y
        move_left_click(move_x, move_y)
        if self.__is_mission_open():
            alt_q()

    def read_mission(self):
        info("开始读取任务")
        if not self.__is_mission_open():
            alt_q()
        self.__shot_mission()
        text = read_text_basic(self.content_path)
        info("任务的内容是:", text)
        if self.__is_mission_open():
            alt_q()
        return text

    def __shot_mission(self):
        """
        任务截图
        """
        game_shot(self.content_shape, self.content_path)

    def __is_mission_open(self):
        """
        任务栏是否打开
        """
        _, score = game_template_match(self.title_path)
        info("任务栏打开标识分数:", score)
        return score >= 5


class Map:
    def __init__(self):
        self.map_open_flag = os.path.join(c.flag_dir, "map_open.png")
        self.move_x = 0
        self.move_y = 0

    def click(self, place, x, y):
        if place == "cac":
            self.click_cac(x, y)
        elif place == "jyc":
            self.click_jyc(x, y)
        elif place == "csc":
            self.click_csc(x, y)
        elif place == "alg":
            self.click_alg(x, y)
        elif place == "xlng":
            self.click_xlng(x, y)
        elif place == "zzg":
            self.click_zzg(x, y)
        elif place == "bxg":
            self.click_bxg(x, y)
        elif place == "dtgj":
            self.click_dtgj(x, y)
        elif place == "dtjw":
            self.click_dtjw(x, y)
        elif place == "jnyw":
            self.click_jnyw(x, y)
        elif place == "csjw":
            self.click_csjw(x, y)
        elif place == "bjlz":
            self.click_bjlz(x, y)
        elif place == "hgs":
            self.click_hgs(x, y)
        elif place == "dhw":
            self.click_dhw(x, y)
        elif place == "qls":
            self.click_qls(x, y)
        elif place == "df":
            self.click_df(x, y)
        elif place == "stl":
            self.click_stl(x, y)
        elif place == "mwz":
            self.click_mwz(x, y)
        elif place == "fcs":
            self.click_fcs(x, y)
        elif place == "hss":
            self.click_hss(x, y)
        elif place == "dtgf":
            self.click_dtgf(x, y)
        elif place == "lg":
            self.click_lg(x, y)
        elif place == "nec":
            self.click_nec(x, y)
        else:
            error("未找到地点:", place)

    def click_cac(self, x, y):
        self.move_x = 133 + x
        self.move_y = 502 - y
        self.__open_map_click()

    def click_jyc(self, x, y):
        self.move_x = 127 + x * 2
        self.move_y = 502 - y * 2
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
            tab()
        move_left_click(self.move_x, self.move_y)
        if self.__is_map_open():
            tab()

    def __is_map_open(self):
        _, score = game_template_match(self.map_open_flag)
        info("地图打开标识模板匹配分数:", score)
        return score >= 5
