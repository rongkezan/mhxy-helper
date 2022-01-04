from enum import Enum


class CITY(Enum):
    JY = "建邺"
    CA = "长安"
    CS = "长寿"
    AL = "傲来"
    ZZ = "朱紫"
    BX = "宝象"
    XL = "西凉"
    GJ = "国境"
    HW = "海湾"
    YW = "野外"
    CSJW = "郊外"
    DTJW = "境外"


class SCHOOL(Enum):
    # 人族
    DT = "大唐"
    HS = "化生"
    FC = "方寸"
    SM = "神木"
    NE = "女儿"
    TJ = "天机"
    # 仙族
    PT = "普陀"
    TG = "天宫"
    LG = "龙宫"
    WZ = "五庄"
    LB = "凌波"
    HG = "花果"
    # 魔族
    DF = "地府"
    PS = "盘丝"
    ST = "狮驼"
    MW = "魔王"
    NB = "女魃"
    WD = "无底"


def get_all_city():
    return [e.value for e in CITY]


def get_all_school():
    return [e.value for e in SCHOOL]


def appear_city(text):
    places = get_all_city()
    for place in places:
        if text.__contains__(place):
            return place
    return None


def appear_school(text):
    places = get_all_school()
    for place in places:
        if text.__contains__(place):
            return place
    return None
