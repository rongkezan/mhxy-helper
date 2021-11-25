import os
from utils.window import *
from utils.log import *


def is_not_same_crop4():
    # 得到最新的一张保存的四小人截图
    files = os.listdir(c.data_dir)
    recent_file = None
    for file in files:
        if recent_file is None:
            recent_file = file
        elif int(str(file).split('.')[0]) > int(str(recent_file).split('.')[0]):
            recent_file = file
    if recent_file is None:
        return True
    # 确认刚截的图不是已经保存过的
    score = compare_image(os.path.join(c.data_dir, recent_file), c.temp_popup)
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
    return score >= 5


def is_popup():
    offset_shape = [(-107, 28, 97, 130), (-86, 28, 174, 130)]
    i = 0
    for popup in c.flag_popup:
        shape, score = game_template_match(popup)
        info("4小人模板识别模板, ", popup, "，分数：", score)
        if score >= 5:
            sub_shape = (
                shape[0] + offset_shape[i][0],
                shape[1] + offset_shape[i][1],
                shape[2] + offset_shape[i][2],
                shape[3] + offset_shape[i][3]
            )
            game_shot(sub_shape, c.temp_popup)
            return True
        i += 1
    return False


def is_auto_fight():
    path = os.path.join(c.flag_dir, 'fight_auto.png')
    shape, score = game_template_match(path)
    info("自动状态标识标识模板匹配分数:", score)
    return score >= 4


def is_need_heal():
    path = os.path.join(c.temp_dir, "status.png")
    game_shot((740, 60, 800, 80), path)
    img = cv.imread(path)
    print(img[15][15])
    if not (img[15][15][0] == 248):
        return True
    return False


def is_leader():
    __shot_tab()
    img = cv.imread(c.temp_ch_dict['ch1'][1])
    return (img[10][115] == [221, 221, 221]).all()


def is_notify():
    """
    是否有通知(Tab变红)
    """
    __shot_tab()
    for k in c.temp_ch_dict:
        img = cv.imread(c.temp_ch_dict[k][1])
        if (img[10][115] == [149, 203, 253]).all():
            return c.temp_ch_dict[k][2]
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


def shot_monster():
    """
    怪物截图
    """
    path = os.path.join(c.temp_dir, "monster.png")
    game_shot((100, 100, 510, 415), path)
    return path


def __shot_tab():
    """
    人物标签截图
    """
    game_shot((20, 33, 780, 53), c.temp_ch)
    Image.open(c.temp_ch).crop(c.temp_ch_dict['ch1'][0]).save(c.temp_ch_dict['ch1'][1])
    Image.open(c.temp_ch).crop(c.temp_ch_dict['ch2'][0]).save(c.temp_ch_dict['ch2'][1])
    Image.open(c.temp_ch).crop(c.temp_ch_dict['ch3'][0]).save(c.temp_ch_dict['ch3'][1])
    Image.open(c.temp_ch).crop(c.temp_ch_dict['ch4'][0]).save(c.temp_ch_dict['ch4'][1])
    Image.open(c.temp_ch).crop(c.temp_ch_dict['ch5'][0]).save(c.temp_ch_dict['ch5'][1])


if __name__ == '__main__':
    # 左 + 30 ；右 - 56
    # Image.open(os.path.join(c.flag_dir, "popup2.png")).crop((30, 0, 130, 20)).save(os.path.join(c.temp_dir, "popup2.png"))
    offset_shape = [(-107, 28, 97, 130), (-86, 28, 174, 130)]
    shape, score = template_match(os.path.join(c.flag_dir, "popup1.png"), c.temp_game)
    sub_shape = (
        shape[0] + offset_shape[0][0],
        shape[1] + offset_shape[0][1],
        shape[2] + offset_shape[0][2],
        shape[3] + offset_shape[0][3]
    )
    Image.open(c.temp_game).crop(sub_shape).save(os.path.join(c.temp_dir, "popup.png"))
