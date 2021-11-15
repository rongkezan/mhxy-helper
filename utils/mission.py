from PIL import Image
from utils.window import *
from utils.auto import *


class Mission:
    def __init__(self):
        self.shape = (501, 343, 705, 580)
        self.path = os.path.join(c.temp_dir, "mission.png")
        self.red = [1, 1, 255]

    def __shot_mission(self):
        """
        任务截图
        """
        shot()
        Image.open(c.temp_game).crop(self.shape).save(self.path)

    def __location(self, path):
        """
        定位红色任务字体坐标
        """
        img = cv.imread(path)
        for i in range(len(img)):
            for j in range(len(img[0])):
                if (img[i][j] == self.red).all():
                    return j, i

    def click_mission(self):
        # TODO 需要判断任务栏是否打开和关闭
        alt_q()
        self.__shot_mission()
        x, y = self.__location(self.path)
        move_x = self.shape[0] + x
        move_y = self.shape[1] + y
        move_left_click(move_x, move_y)
        alt_q()
