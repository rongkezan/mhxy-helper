from auto.component.camera import camera
import shutil
import constants.path as p
import os
import time
import keyboard


def save():
    print("保存图片")
    camera.shot()
    shutil.copy(p.temp_game, os.path.join(p.data_game_dir, str(int(round(time.time() * 1000))) + ".png"))


if __name__ == '__main__':
    print("程序运行")
    keyboard.add_hotkey('f12', save)
    keyboard.wait()
