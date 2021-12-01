from utils.action import *
from utils.watcher import *
from utils.component import Bag, Map, Mission
from utils.txt import *
from main.pb import find_npc_yz
import re

bag = Bag()
map = Map()
mission = Mission()
balance = 42000


class Cargo:
    def __init__(self, name, pic, max_price, price1=0, price2=0, profit1=0, profit2=0):
        self.name = name
        self.pic = pic
        self.max_price = max_price
        self.price1 = price1
        self.price2 = price2
        self.profit1 = profit1
        self.profit2 = profit2


cargo_dict = {
    "长安": [
        Cargo("棉布", "", 3500),
        Cargo("扇子", "", 3800),
        Cargo("武器", "", 4000),
        Cargo("佛珠", "", 7000),
    ],
    "长寿": [
        Cargo("面粉", "", 3000),
        Cargo("木材", "", 4400),
        Cargo("商品符", "", 5300),
        Cargo("鹿茸", "", 7500),
    ]
}


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


def buy(cargo):
    global balance
    res = find_xy_in_game(cargo.pic)
    if res is not None:
        move_left_click(res[0], res[1])
        price = get_price()
        amount = get_amount()
        balance -= price * amount
        info("购买商品成功, 当前余额:", balance)


def mission_not_finished():
    path = os.path.join(c.flag_dir, "ticket.png")
    return bag.is_item_exist(path)


def is_place(place_name):
    return True


def ca_to_cs():
    info("长安城 -> 驿站")
    map.click_cac(0, 0)
    find_npc_yz()
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
    info("长寿村 -> 长寿货商1")
    map.click_csc(0, 0)


def init_cargo_price(place, trader):
    cargo_list = cargo_dict[place]
    for cargo in cargo_list:
        res = find_xy_in_game(cargo.pic)
        if res is not None:
            move_left_click(res[0], res[1])
            if trader == 1:
                cargo.price1 = get_price()
                cargo.profit1 = cargo.max_price - cargo.price1
                info("%s商人1, 商品:%s, 价格:%d, 预估利润:%d", place, cargo.name, cargo.price1, cargo.profit1)
            elif trader == 2:
                cargo.price2 = get_price()
                cargo.profit2 = cargo.max_price - cargo.price2
                info("%s商人2, 商品:%s, 价格:%d, 预估利润:%d", place, cargo.name, cargo.price2, cargo.profit2)


if __name__ == '__main__':
    info("开始跑商")
    get_mission()
    info("帮派 -> 长安商人1")
    map.click_cac(0, 0)
    info("点击长安商人1")
    move_left_click(0, 0)
    info("查询长安商人1物品价格")
    init_cargo_price("长安", 1)
    ca_cargo_list = sorted(cargo_dict["长安"], key=lambda x: getattr(x, 'profit1'), reverse=True)
    for cargo in ca_cargo_list:
        if cargo.profit1 >= 500:
            info("长安商人1, 商品:%s, 预估利润:%d, 直接购买", cargo.name, cargo.profit1)
            buy(cargo)

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
    info("当前余额:", balance, "，长安城购买完毕")
