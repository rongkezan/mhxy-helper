from utils.game_action import *
from utils.game_watcher import *
from utils.txt import *


class Map:
    def __init__(self):
        self.move_x = 0
        self.move_y = 0

    def click_cac(self, x, y):
        self.move_x = 243 + x
        self.move_y = 286 - y
        self.__open_map_click()

    def click_jyc(self, x, y):
        self.move_x = 229 + x * 2
        self.move_y = 593 - y * 2
        self.__open_map_click()

    def click_csc(self, x, y):
        self.move_x = 347 + round(x * 5 / 3)
        self.move_y = 638 - round(y * 5 / 3)
        self.__open_map_click()

    def click_alg(self, x, y):
        self.move_x = 274 + round(x * 412 / 223)
        self.move_y = 601 - round(y * 278 / 150)
        self.__open_map_click()

    def click_xlng(self, x, y):
        self.move_x = 293 + round(x * 372 / 163)
        self.move_y = 635 - round(y * 282 / 123)
        self.__open_map_click()

    def click_zzg(self, x, y):
        self.move_x = 261 + round(x * 372 / 163)
        self.move_y = 602 - round(y * 439 / 191)
        self.__open_map_click()

    def click_bxg(self, x, y):
        self.move_x = 259 + round(x * 440 / 159)
        self.move_y = 629 - round(y * 331 / 119)
        self.__open_map_click()

    def click_dtgj(self, x, y):
        self.move_x = 293 + round(x * 377 / 351)
        self.move_y = 643 - round(y * 361 / 335)
        self.__open_map_click()

    def click_dtjw(self, x, y):
        self.move_x = 226 + round(x * 583 / 638)
        self.move_y = 503 - round(y * 109 / 118)
        self.__open_map_click()

    def click_jnyw(self, x, y):
        self.move_x = 232 + round(x * 369 / 159)
        self.move_y = 614 - round(y * 274 / 119)
        self.__open_map_click()

    def click_csjw(self, x, y):
        self.move_x = 323 + round(x * 316 / 191)
        self.move_y = 601 - round(y * 277 / 167)
        self.__open_map_click()

    def click_bjlz(self, x, y):
        self.move_x = 297 + round(x * 367 / 227)
        self.move_y = 601 - round(y * 277 / 169)
        self.__open_map_click()

    def click_hgs(self, x, y):
        self.move_x = 297 + round(x * 369 / 159)
        self.move_y = 601 - round(y * 277 / 119)
        self.__open_map_click()

    def click_dhw(self, x, y):
        self.move_x = 343 + round(x * 276 / 119)
        self.move_y = 601 - round(y * 276 / 119)
        self.__open_map_click()

    def click_qls(self, x, y):
        self.move_x = 297 + round(x * 369 / 190)
        self.move_y = 601 - round(y * 276 / 141)
        self.__open_map_click()

    def click_df(self, x, y):
        self.move_x = 297 + round(x * 364 / 159)
        self.move_y = 601 - round(y * 279 / 119)
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
        time.sleep(1)
        path2 = shot_place(2)
        score = compare_image(path1, path2)
        if score > 0.99:
            return True
