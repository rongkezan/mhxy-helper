import os
import time
import constants.path as p
from auto.component.action import action
from auto.component.camera import camera


class Trader:
    def __init__(self):
        self.yhl = os.path.join(p.item_dir, "yhl.png")
        self.item1 = os.path.join(p.temp_dir, "yhl.png")
        self.item2 = os.path.join(p.temp_dir, "item2.png")
        self.item3 = os.path.join(p.temp_dir, "item3.png")
        self.item_price = 70000

    def start(self):
        print("--- monitor started ---")
        while True:
            time.sleep(5)
            print("--- working ---")
            # 初始化数量
            count = 0
            # 获取3格交易窗口的物品
            camera.game_shot((125, 332, 175, 382), self.item1)
            camera.game_shot((181, 332, 231, 382), self.item2)
            camera.game_shot((237, 332, 287, 382), self.item3)
            # 比较物品是否为"月华露"
            score1 = camera.compare_image(self.yhl, self.item1)
            score2 = camera.compare_image(self.yhl, self.item2)
            score3 = camera.compare_image(self.yhl, self.item3)
            print("score: ", score1, score2, score3)
            if score1 >= 0.9:
                count = count + 1
            if score2 >= 0.9:
                count = count + 1
            if score3 >= 0.9:
                count = count + 1

            if count > 0:
                total_price = self.item_price * count
                # 输入价格 -> 点击确认 -> 点击交易
                action.input_num(total_price)
                time.sleep(1)
                action.move_left_click(310, 148)
                time.sleep(1)
                action.move_left_click(425, 410)
                print("bought %d items, cost %d" % (count, total_price))


Trader().start()