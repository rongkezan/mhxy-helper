import shutil
from utils.watcher import *


def task():
    if is_fight() and is_popup() and is_not_same_crop4():
        shutil.copy(c.temp_popup, os.path.join(c.data_crop_dir, str(int(round(time.time() * 1000))) + ".png"))


if __name__ == '__main__':
    while True:
        info("图像收集程序运行中")
        time.sleep(1)
        task()
