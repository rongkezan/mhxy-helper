from utils.game_action import *
from utils.game_watcher import *
from utils.txt import *


class Map:
    def __init__(self):
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
            print("[Error] 未找到地点:", place)

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
        if not map_is_open():
            tab()
        move_left_click(self.move_x, self.move_y)
        if map_is_open():
            tab()


def shot_place(index):
    shot()
    path = os.path.join(c.temp_dir, "place" + str(index) + ".png")
    Image.open(c.temp_game).crop((38, 83, 143, 98)).save(path)
    return path


def map_is_open():
    shot()
    _, score = template_match(os.path.join(c.flag_dir, "map_open.png"), c.temp_game)
    if score >= 5:
        return True
    return False


def arrived():
    while True:
        path1 = shot_place(1)
        time.sleep(0.5)
        path2 = shot_place(2)
        score = compare_image(path1, path2)
        if score > 0.99:
            return True