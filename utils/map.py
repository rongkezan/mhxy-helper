from utils.game_action import *
from utils.game_watcher import *
from utils.txt import *


class MapCAC:
    """
    长安城
    """
    def __init__(self):
        self.x0 = 243
        self.y0 = 586

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + x
        move_y = self.y0 - y
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapJYC:
    """
    建邺城
    """
    def __init__(self):
        self.x0 = 229
        self.y0 = 593

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + x * 2
        move_y = self.y0 - y * 2
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapCSC:
    """
    长寿村
    """
    def __init__(self):
        self.x0 = 347
        self.y0 = 638

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + x * 5 / 3
        move_y = self.y0 - y * 5 / 3
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapALG:
    """
    傲来国
    """
    def __init__(self):
        self.x0 = 274
        self.y0 = 601

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 412 / 223)
        move_y = self.y0 - round(y * 278 / 150)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapXLNG:
    """
    西梁女国
    """
    def __init__(self):
        self.x0 = 293
        self.y0 = 635

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 372 / 163)
        move_y = self.y0 - round(y * 282 / 123)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapZZG:
    """
    朱紫国
    """
    def __init__(self):
        self.x0 = 261
        self.y0 = 602

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 372 / 163)
        move_y = self.y0 - round(y * 439 / 191)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapBXG:
    """
    宝象国
    """
    def __init__(self):
        self.x0 = 259
        self.y0 = 629

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 440 / 159)
        move_y = self.y0 - round(y * 331 / 119)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapDTGJ:
    """
    大唐国境
    """
    def __init__(self):
        self.x0 = 293
        self.y0 = 643

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 377 / 351)
        move_y = self.y0 - round(y * 361 / 335)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapDTJW:
    """
    大唐境外
    """
    def __init__(self):
        self.x0 = 226
        self.y0 = 503

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 583 / 638)
        move_y = self.y0 - round(y * 109 / 118)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapJNYW:
    """
    江南野外
    """
    def __init__(self):
        self.x0 = 232
        self.y0 = 614

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 369 / 159)
        move_y = self.y0 - round(y * 274 / 119)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapCSJW:
    """
    长寿郊外
    """
    def __init__(self):
        self.x0 = 323
        self.y0 = 601

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 316 / 191)
        move_y = self.y0 - round(y * 277 / 167)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapBJLZ:
    """
    北俱芦洲
    """
    def __init__(self):
        self.x0 = 297
        self.y0 = 601

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 367 / 227)
        move_y = self.y0 - round(y * 277 / 169)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapHGS:
    """
    花果山
    """
    def __init__(self):
        self.x0 = 297
        self.y0 = 601

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 369 / 159)
        move_y = self.y0 - round(y * 277 / 119)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapDHW:
    """
    东海湾
    """
    def __init__(self):
        self.x0 = 343
        self.y0 = 601

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 276 / 119)
        move_y = self.y0 - round(y * 276 / 119)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapQLS:
    """
    麒麟山
    """
    def __init__(self):
        self.x0 = 297
        self.y0 = 601

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 369 / 190)
        move_y = self.y0 - round(y * 276 / 141)
        move_left_click(move_x, move_y)
        if map_is_open():
            tab()


class MapDF:
    """
    地府
    """
    def __init__(self):
        self.x0 = 297
        self.y0 = 601

    def click(self, x, y):
        if not map_is_open():
            tab()
        move_x = self.x0 + round(x * 364 / 159)
        move_y = self.y0 - round(y * 279 / 119)
        move_left_click(move_x, move_y)
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
