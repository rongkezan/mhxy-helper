import shutil
import time
from utils.game_watcher import *


def task():
    if is_fight() and is_popup() and is_not_same_crop4():
        shutil.copy(c.temp_popup, os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".png"))


if __name__ == '__main__':
    while True:
        print(">>> 运行中 >>>")
        time.sleep(3)
        task()
