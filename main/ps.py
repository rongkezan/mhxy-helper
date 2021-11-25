from utils.action import *
from utils.watcher import *
from utils.component import Bag, Map, Mission
from utils.txt import *
from main.pb import yz_transfer
import re

bag = Bag()
map = Map()
mission = Mission()
balance = 42000


class Cargo:
    def __init__(self, name, pic, max_price, price1=0, price2=0):
        self.name = name
        self.pic = pic
        self.max_price = max_price
        self.price1 = price1
        self.price2 = price2


ca_cargo_list = [
    Cargo("棉布", "", 3500),
    Cargo("扇子", "", 3800),
    Cargo("武器", "", 4000),
    Cargo("佛珠", "", 7000),
]

cs_cargo_dict = [
    Cargo("面粉", "", 3000),
    Cargo("木材", "", 4400),
    Cargo("商品符", "", 5300),
    Cargo("鹿茸", "", 7500),
]


def get_price():
    shape = (0, 0, 0, 0)
    path = os.path.join(c.temp_dir, "price.png")
    game_shot(shape, path)
    text = read_text_basic(path)
    price = re.sub("\D", "", text)
    return int(price)


def get_amount():
    shape = (0, 0, 0, 0)
    path = os.path.join(c.temp_dir, "amount.png")
    game_shot(shape, path)
    text = read_text_basic(path)
    amount = re.sub("\D", "", text)
    return int(amount)


def get_mission():
    pass


def buy(price, amount):
    global balance
    balance -= price * amount


def mission_not_finished():
    path = os.path.join(c.flag_dir, "ticket.png")
    bag.is_item_exist(path)


def is_place(place_name):
    return True


if __name__ == '__main__':
    info("开始跑商")
    get_mission()
    info("帮派 -> 长安商人1")
    map.click_cac(0, 0)
    info("点击长安商人1")
    move_left_click(0, 0)
    info("查询长安商人1物品价格")
    for cargo in ca_cargo_list:
        res = find_xy_in_game(cargo.pic)
        if res is not None:
            move_left_click(res[0], res[1])
            cargo.price1 = get_price()
            info(cargo.name, "的价格是: ", cargo.price1)
            if cargo.price1 <= cargo.max_price - 500 and balance >= cargo.price1:
                info(cargo.name, "小于推荐价格500", "直接购买")
                amount = get_amount()
                buy(cargo.price1, amount)
                info("购买", amount, "个", cargo.name, "，当前余额:", balance)
    if balance >= 5000:
        info("当前余额:", balance, "，准备去长安商人2")
        map.click_cac(0, 0)
        info("点击长安商人2")
        move_left_click(0, 0)
        info("查询长安商人2物品价格")
        for cargo in ca_cargo_list:
            res = find_xy_in_game(cargo.pic)
            if res is not None:
                move_left_click(res[0], res[1])
                cargo.price2 = get_price()
                info(cargo.name, "的价格是: ", cargo.price2)
                if cargo.price2 <= cargo.max_price and balance >= cargo.price2:
                    info(cargo.name, "小于推荐价格", "直接购买")
                    amount = get_amount()
                    buy(cargo.price2, amount)
                    info("购买", amount, "个", cargo.name, "，当前余额:", balance)
    info("当前余额:", balance, "，准备去驿站")
    map.click_cac(0, 0)
    yz_transfer()
    info("大唐国境 -> 大唐境外")
    map.click_dtgj(0, 0)
    while is_arrived():
        info("进入大唐境外")
        move_left_click(0, 0)
    info("大唐境外 -> 长寿郊外")
    map.click_dtjw(0, 0)
    while is_arrived():
        info("进入长寿郊外")
        move_left_click(0, 0)
    info("长寿郊外 -> 长寿村")
    while is_arrived():
        info("进入长寿村")
        move_left_click(0, 0)
    info("长寿村 -> 长寿货商")
    map.click_csc(0, 0)
