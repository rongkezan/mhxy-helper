from enum import Enum


class PLACE(Enum):
    JY = "建邺"
    CA = "长安"
    CS = "长寿"
    AL = "傲来"
    BX = "宝象"
    XL = "西凉"
    ZZ = "朱紫"
    GJ = "国境"
    HW = "海湾"
    YW = "野外"
    CSJW = "郊外"
    DTJW = "境外"
    DT = "大唐"
    HS = "化生"
    PT = "普陀"
    DF = "地府"
    LG = "龙宫"
    NE = "女儿"
    PS = "盘丝"
    WZ = "五庄"
    ST = "狮驼"
    MW = "魔王"
    FC = "方寸"


def get_all_place():
    return [e.value for e in PLACE]


def appear_place(text):
    places = get_all_place()
    for place in places:
        if text.__contains__(place):
            return place
    return None