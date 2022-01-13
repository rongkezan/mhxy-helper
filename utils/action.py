import os
from utils.mouse import *


def find_xy_in_game(template_path):
    shape, score = game_template_match(template_path)
    info("模板匹配相似度分数:", score)
    if score >= 3:
        x = (shape[0] + shape[2]) // 2
        y = (shape[1] + shape[3]) // 2
        return x, y
    else:
        return None


def shot_monster():
    """
    怪物截图
    """
    path = os.path.join(c.temp_dir, "monster.png")
    game_shot((100, 100, 510, 415), path)
    return path


def shot_tab():
    """
    人物标签截图
    """
    game_shot((20, 33, 780, 53), c.temp_tab_group)
    for t in c.temp_tabs:
        Image.open(c.temp_tab_group).crop(t.shape).save(t.path)


def is_not_same_crop4():
    # 得到最新的一张保存的四小人截图
    files = os.listdir(c.data_crop_dir)
    recent_file = None
    for file in files:
        if recent_file is None:
            recent_file = file
        elif int(str(file).split('.')[0]) > int(str(recent_file).split('.')[0]):
            recent_file = file
    if recent_file is None:
        return True
    # 确认刚截的图不是已经保存过的
    score = compare_image(os.path.join(c.data_crop_dir, recent_file), c.temp_popup)
    if score > 0.8:
        print("弹框已保存过，Score:", score)
        return False
    else:
        print("保存弹框，Score:", score)
    return True


def is_fight():
    path1 = os.path.join(c.temp_dir, 'fight_bar.png')
    path2 = os.path.join(c.flag_dir, 'fight_bar.png')
    game_shot((795, 190, 805, 430), path1)
    score = compare_image(path1, path2)
    return score > 0.95


def is_ready_fight():
    path = os.path.join(c.flag_dir, "fight_tool.png")
    _, score = game_template_match(path)
    return score >= 3


def is_popup():
    offset_shape = [(-107, 28, 97, 130), (-46, 29, 174, 130)]
    i = 0
    for popup in c.flag_popup:
        shape, score = game_template_match(popup)
        info("4小人模板识别模板, ", popup, "，分数：", score, shape)
        if score >= 5:
            sub_shape = (
                shape[0] + offset_shape[i][0],
                shape[1] + offset_shape[i][1],
                shape[0] + offset_shape[i][0] + 360,
                shape[1] + offset_shape[i][1] + 120
            )
            game_shot(sub_shape, c.temp_popup)
            return shape[0], shape[1]
        i += 1
    return None


def is_auto_fight():
    path = os.path.join(c.flag_dir, 'fight_auto.png')
    shape, score = game_template_match(path)
    return score >= 3


def is_need_heal():
    path = os.path.join(c.temp_dir, "status.png")
    game_shot((740, 60, 800, 80), path)
    img = cv.imread(path)
    if not (img[15][15][0] == 248):
        return True
    return False


def is_leader():
    shot_tab()
    img = cv.imread(c.temp_tabs[0].path)
    return (img[10][115] == [221, 221, 221]).all()


def is_notify():
    """
    是否有通知(Tab变红)
    """
    shot_tab()
    for t in c.temp_tabs:
        img = cv.imread(t.path)
        if (img[10][115] == [149, 203, 253]).all():
            return t.position
    return False


def is_arrived():
    while True:
        shape = (38, 83, 143, 98)
        game_shot(shape, c.temp_place1)
        time.sleep(0.5)
        game_shot(shape, c.temp_place2)
        score = compare_image(c.temp_place1, c.temp_place2)
        info("是否到达目的地匹配分数:", score)
        if score > 0.99:
            return True


def do_find_npc(npc):
    print(npc)
    name, paths = npc[0], npc[1]
    do_hide()
    while True:
        time.sleep(0.1)
        info("寻找" + name + "中...")
        found = False
        for path in paths:
            result = find_xy_in_game(path)
            if result is not None:
                found = True
                x, y = result[0], result[1]
                info("找到" + name + "，位置:", x, y)
                move_left_click(x, y)
                break
        if found:
            info("已找到" + name + "，退出寻找")
            break
        else:
            info("未找到" + name + "，继续寻找")
            time.sleep(5)
            do_hide()


def do_hide():
    info("隐藏人物和摊位")
    f9()
    alt_h()


def do_heal():
    info("酒肆")
    f6()
    move_left_click(194, 452)


def do_fight5(action1=alt_q, action2=alt_q):
    """
    action1: 人物操作 q-施法 a-攻击 d-防御
    action2: 宠物操作 q-施法 a-攻击 d-防御
    """
    for t in c.temp_tabs:
        move_left_click(t.position[0], t.position[1], True)
        info("攻击/施法")
        action1()
        action2()