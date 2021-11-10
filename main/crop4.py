import shutil
import time
from utils.game_watcher import *


def task():
    if is_fight():
        if is_popup():
            if is_not_same_crop4():
                shutil.copy(c.temp_popup, os.path.join(c.data_dir, str(int(round(time.time() * 1000))) + ".jpg"))


if __name__ == '__main__':
    while True:
        print(">>> 运行中 >>>")
        time.sleep(3)
        task()
