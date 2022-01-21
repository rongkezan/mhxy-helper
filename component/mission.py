import utils.log as log
from component.factory import camera


class Mission:
    def __init__(self):
        self.path = ""
        self.shape = (0, 0, 0, 0)  # 任务追踪栏的shape

    def read(self):
        log.info("开始读取任务")
        self.__shot_mission()
        text = camera.read_text_basic(self.path)
        log.info("任务的内容是:", text)
        return text

    def click_target(self):
        pass

    def __shot_mission(self):
        """
        任务截图
        """
        camera.game_shot(self.shape, self.path)
