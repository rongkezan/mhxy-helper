from PIL import Image
from utils.window import *
from utils.txt import *
import time


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


def is_ready_fight():
    shot()
    path = os.path.join(c.temp_dir, "fight_tool.png")
    Image.open(c.temp_game).crop((673, 220, 735, 300)).save(path)
    score = compare_tf_image("fight_tool.png")
    if score > 0.95:
        return True
    return False


def is_popup():
    shot()
    shape, score = template_match(c.flag_popup, c.temp_game)
    if score >= 4:
        sub_shape = (
            shape[0] - 56,
            shape[1] + 16,
            shape[2] + 118,
            shape[3] + 130
        )
        Image.open(c.temp_game).crop(sub_shape).save(c.temp_popup)
        return True
    return False


def is_fight():
    shot()
    Image.open(c.temp_game).crop((1017, 188, 1028, 438)).save(os.path.join(c.temp_dir, 'fight_bar.png'))
    score = compare_tf_image("fight_bar.png")
    if score > 0.95:
        return True
    else:
        return False


def is_need_heal():
    shot()
    path = os.path.join(c.temp_dir, "status.png")
    Image.open(c.temp_game).crop((966, 60, 1020, 83)).save(path)
    img = cv.imread(path)
    print(img[15][15])
    if not (img[15][15][0] == 248):
        return True
    return False


def leader_is_active():
    __shot_tag()
    img = cv.imread(c.ch_dict['ch1'][1])
    return (img[10][115] == [221, 221, 221]).all()


def is_auto_fight():
    shape, score = template_match(c.flag_auto_fight, c.temp_game)
    if score >= 4:
        return True
    else:
        return False


def is_notify():
    __shot_tag()
    for k in c.ch_dict:
        img = cv.imread(c.ch_dict[k][1])
        if (img[10][115] == [155, 202, 254]).all():
            return c.ch_dict[k][2]
    return False


def __shot_tag():
    """
    人物标签截图
    """
    shot()
    Image.open(c.temp_game).crop((20, 33, 780, 53)).save(c.ch_temp_img)
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch1'][0]).save(c.ch_dict['ch1'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch2'][0]).save(c.ch_dict['ch2'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch3'][0]).save(c.ch_dict['ch3'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch4'][0]).save(c.ch_dict['ch4'][1])
    Image.open(c.ch_temp_img).crop(c.ch_dict['ch5'][0]).save(c.ch_dict['ch5'][1])


def is_kw_monster(kw):
    """
    识别出指定目标
    """
    shot()
    path = os.path.join(c.temp_dir, "monster.png")
    Image.open(c.temp_game).crop((0, 100, 550, 400)).save(path)
    words = read_text_basic(path)
    print("识别怪物:", words)
    for word in words:
        if word.__contains__(kw):
            return True
    return False
