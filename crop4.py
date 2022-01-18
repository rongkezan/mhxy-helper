import shutil
import utils.log as log
import constants as c
import os
import time
from utils.action import Action
from utils.camera import Camera

action = Action()
camera = Camera()


def task():
    if camera.is_fight() and camera.is_popup() and camera.is_not_same_crop4():
        shutil.copy(c.temp_popup, os.path.join(c.data_crop_dir, str(int(round(time.time() * 1000))) + ".png"))


if __name__ == '__main__':
    while True:
        log.info("图像收集程序运行中")
        time.sleep(1)
        task()
