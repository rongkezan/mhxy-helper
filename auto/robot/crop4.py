import shutil
import os
import time
import auto.utils.log as log
import constants.path as p
from auto.component.camera import camera


def task():
    if camera.is_fight() and camera.is_popup1() and camera.is_not_same_crop4():
        shutil.copy(p.temp_popup, os.path.join(p.data_crop_dir, str(int(round(time.time() * 1000))) + ".png"))


if __name__ == '__main__':
    while True:
        log.info("图像收集程序运行中")
        time.sleep(1)
        task()
