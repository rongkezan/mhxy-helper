import auto.utils.log as log
from auto.component.camera import camera
import constants.path as p
import os
import shutil
import time
import keyboard
import neural.target.detect as td


class Mission:
    def __init__(self):
        self.path = os.path.join(p.temp_common_dir, "mission.png")
        self.shape = (645, 195, 810, 405)  # 任务追踪栏的shape

    def read(self):
        log.info("开始读取任务")
        self.__shot_mission()
        text = camera.read_text_basic(self.path)
        log.info("任务的内容是:", text)
        return text

    def click_target(self):
        self.__shot_mission()
        res = td.run()
        if res is not None:
            return res

    def __shot_mission(self):
        """
        任务截图
        """
        camera.game_shot(self.shape, self.path)

    def save_mission(self):
        log.info("保存任务截图")
        self.__shot_mission()
        shutil.copy(self.path, os.path.join(p.data_mission_dir, str(int(round(time.time() * 1000))) + ".jpg"))


mission = Mission()


if __name__ == '__main__':
    keyboard.add_hotkey('f12', mission.save_mission)
    keyboard.wait()
