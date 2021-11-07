import os
import shutil
import constants as c
import time
from ImgOperation import shot1, is_fight, is_popup, compare_image


def is_not_same_fight():
    # 得到最新的一张保存的四小人截图
    files = os.listdir(c.data_dir)
    recent_file = None
    for file in files:
        if recent_file is None:
            recent_file = file
        elif convert_to_int(file) > convert_to_int(recent_file):
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


def convert_to_int(file_name):
    return int(str(file_name).split('.')[0])


def task():
    if shot1():
        if is_fight():
            if is_popup():
                if is_not_same_fight():
                    shutil.copy(c.temp_popup, os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".jpg"))


if __name__ == '__main__':
    while True:
        time.sleep(3)
        task()
