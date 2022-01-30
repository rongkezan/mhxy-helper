import os
from constants import path as p
from auto.component import action, camera


class Maps:
    def __init__(self):
        self.map_open_flag = os.path.join(p.flag_common_dir, "map_open.png")
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
        _, score = camera.template_match(self.map_open_flag, path.temp_game)
        return score >= 3

maps = Maps()