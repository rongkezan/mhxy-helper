from utils.mouse import *
from utils.action import *
from utils.component import Bag, Map, Mission
import re

bag = Bag()
map = Map()
mission = Mission()
balance = 42000
syx_timestamp = 0
best_npc = 1


class Cargo:
    def __init__(self, name, pic, max_price, price=0, profit=0):
        self.name = name
        self.pic = pic
        self.max_price = max_price
        self.price = price
        self.profit = profit


cargo_dict = {
    "ca": [
        Cargo("棉布", "", 3500),
        Cargo("扇子", "", 3800),
        Cargo("武器", "", 4000),
        Cargo("佛珠", "", 7000),
    ],
    "cs": [
        Cargo("面粉", "", 3000),
        Cargo("木材", "", 4400),
        Cargo("商品符", "", 5300),
        Cargo("鹿茸", "", 7500),
    ]
}


def get_price():
    """
    获取购买价格
    """
    shape = (0, 0, 0, 0)
    path = os.path.join(c.temp_dir, "price.png")
    game_shot(shape, path)
    text = read_text_basic(path)
    price = re.sub("\D", "", text)
    return int(price)


def get_amount():
    """
    获取购买数量
    """
    shape = (0, 0, 0, 0)
    path = os.path.join(c.temp_dir, "amount.png")
    game_shot(shape, path)
    text = read_text_basic(path)
    amount = re.sub("\D", "", text)
    return int(amount)


def get_mission():
    info("获取任务")
    pass


def check_syx():
    """
    检查摄妖香, 如果时间小于2分钟，则使用
    """
    global syx_timestamp
    now = int(time.time())
    if now - syx_timestamp <= 120:
        bag.right_click(5, 4)
        syx_timestamp = int(time.time())


def buy(cargo):
    """
    购买商品
    """
    global balance
    res = find_xy_in_game(cargo.pic)
    if res is not None:
        move_left_click(res[0], res[1])
        price = get_price()
        amount = get_amount()
        balance -= price * amount
        info("购买%d个%s，单价:%d，剩余余额:%d", amount, cargo.name, cargo.price, balance)


def hide_all():
    info("隐藏人物")
    f9()
    info("隐藏摊位")
    alt_h()


def find_npc(paths, npc_name="npc"):
    """
    根据npc图片寻找npc
    paths: npc图片列表
    """
    do_hide()
    while True:
        time.sleep(0.1)
        info("寻找" + npc_name + "中...")
        found = False
        for path in paths:
            result = find_xy_in_game(path)
            if result is not None:
                found = True
                x, y = result[0], result[1]
                info("找到" + npc_name + "，位置:", x, y)
                move_left_click(x, y)
                break
        if found:
            info("已找到" + npc_name + "，退出寻找")
            break
        else:
            info("未找到" + npc_name + "，继续寻找")
            time.sleep(5)
            do_hide()


def find_npc_yz():
    find_npc(c.flag_yz, "驿站车夫")


def mission_not_finished():
    path = os.path.join(c.flag_dir, "ticket.png")
    return bag.is_item_exist(path)


def is_place(place_name):
    return True


def ps_move(x, y, log=None):
    if log is not None:
        info(log)
    move_left_click(x, y)


def ps_move_map(x, y, place, log=None):
    if log is not None:
        info(log)
    map.click(place, x, y)


def ca_to_cs():
    check_syx()

    ps_move_map(0, 0, "cac", "长安城 -> 驿站")
    if is_arrived():
        while not is_place("大唐国境"):
            find_npc_yz()

    ps_move_map(0, 0, "dtgj", "大唐国境 -> 大唐境外")
    map.click_dtgj(0, 0)
    if is_arrived():
        while not is_place("大唐境外"):
            ps_move(0, 0, "进入大唐境外")

    ps_move_map(0, 0, "dtjw", "大唐境外 -> 长寿郊外")
    if is_arrived():
        while not is_place("长寿郊外"):
            find_npc([os.path.join(c.flag_ch_dir, "dtjw_csjw_npc.png")], "大唐境外传送长寿郊外土地")

    ps_move_map(0, 0, "csjw", "长寿郊外 -> 长寿村")
    if is_arrived():
        while not is_place("长寿村"):
            ps_move(0, 0, "进入长寿村")


def cs_to_ca():
    check_syx()

    ps_move_map(0, 0, "csc", "长寿村 -> 长寿郊外")
    if is_arrived():
        while not is_place("长寿郊外"):
            ps_move(0, 0, "进入长寿郊外")

    ps_move_map(0, 0, "csjw", "长寿郊外 -> 北俱芦洲")
    if is_arrived():
        while not is_place("北俱芦洲"):
            find_npc([os.path.join(c.flag_ch_dir, "csjw_bjlz_npc.png")], "长寿郊外传送北俱芦洲车夫")

    ps_move_map(0, 0, "bjlz", "北俱芦洲 -> 长安城")
    if is_arrived():
        while not is_place("北俱芦洲"):
            find_npc([os.path.join(c.flag_ch_dir, "csjw_bjlz_npc.png")], "北俱芦洲传送长安城车夫")


def move_query_cargo(x, y, place, flag, msg=None, save=False):
    """
    移动到NPC，打开界面，搜索商品，保存商品信息
    x, y: 移动的坐标
    place: ca 长安城 , cs 长寿村
    flag: 1 商人 , 2 货商
    msg: 日志
    """
    global best_npc
    if msg is not None:
        info(msg)
    map.click(place, x, y)
    if is_arrived():
        filename = "hs_" + place + "_" + str(flag) + ".png"
        res = find_xy_in_game(os.path.join(c.flag_ch_dir, filename))
        if res is not None:
            x, y = res[0], res[1]
            info("找到货商", flag, ",进行点击:", x, y)
            move_left_click(x, y)
            info("打开商品界面")
            move_left_click(0, 0)
        if save:
            # 保存商品的最优价格
            info("保存", place, "货商的价格")
            cg_list = cargo_dict[place]
            for cg in cg_list:
                res = find_xy_in_game(cg.pic)
                if res is not None:
                    move_left_click(res[0], res[1])  # 点击商品
                    if cg.price > get_price():
                        best_npc = flag  # 购买的NPC
                        cg.price = get_price()  # 价格
                        cg.profit = cg.max_price - cg.price  # 利润
                        info("商品:%s, 价格:%d, 预估利润:%d", cg.name, cg.price, cg.profit)
                else:
                    info("商品:%s未找到，可能已卖完", cg.name)


if __name__ == '__main__':
    # 获取任务
    get_mission()
    # 跑到最优价格的商人处打开界面
    move_query_cargo(0, 0, "ca", 1, "帮派 -> 长安商人", True)
    move_query_cargo(0, 0, "ca", 2, "长安商人 -> 长安货商", True)
    if best_npc == 1:
        move_query_cargo(0, 0, "ca", 1, "长安货商 -> 长安商人")
    # 将商品利润从大到小排序，依次购买直到余额不足
    cargo_list = sorted(cargo_dict["ca"], key=lambda x: getattr(x, 'profit'), reverse=True)
    for cargo in cargo_list:
        if balance >= cargo.price:
            buy(cargo)
    # 长安城到长寿村
    ca_to_cs()
    # 购买长寿村商品
    move_query_cargo(0, 0, "cs", 1, "长寿村 -> 长寿货商", True)
    move_query_cargo(0, 0, "cs", 1, "长寿货商 -> 长寿商人", True)
    if best_npc == 1:
        move_query_cargo(0, 0, "cs", 1, "长寿商人 -> 长寿货商")
    cargo_list = sorted(cargo_dict["cs"], key=lambda x: getattr(x, 'profit'), reverse=True)
    for cargo in cargo_list:
        if balance >= cargo.price:
            buy(cargo)
    # 长寿村到长安城
    cs_to_ca()
    # TODO 循环


