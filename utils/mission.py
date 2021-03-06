from PIL import Image
from utils.window import *
from utils.game_action import *
from utils.txt import *


class Mission:
    def __init__(self):
        self.content_shape = (397, 263, 592, 494)
        self.title_shape = (341, 180, 483, 196)
        self.content_path = os.path.join(c.temp_dir, "mission_content.png")
        self.title_path = os.path.join(c.temp_dir, "mission_title.png")
        self.red = [1, 1, 255]

    def shot_mission(self):
        """
        任务截图
        """
        shot()
        Image.open(c.temp_game).crop(self.content_shape).save(self.content_path)
        Image.open(c.temp_game).crop(self.title_shape).save(self.title_path)

    def mission_is_open(self):
        """
        任务栏是否打开
        """
        score = compare_tf_image("mission_title.png")
        print(score)
        if score >= 0.99:
            return True
        return False

    def location(self, path):
        """
        定位红色任务字体坐标
        """
        img = cv.imread(path)
        for i in range(len(img)):
            for j in range(len(img[0])):
                if (img[i][j] == self.red).all():
                    return j, i

    def click_mission(self):
        if not self.mission_is_open():
            alt_q()
        self.shot_mission()
        x, y = self.location(self.content_path)
        move_x = self.content_shape[0] + x
        move_y = self.content_shape[1] + y
        move_left_click(move_x, move_y)
        if self.mission_is_open():
            alt_q()

    def read_mission(self):
        print("开始读取任务")
        if not self.mission_is_open():
            alt_q()
        self.shot_mission()
        text = read_text_basic(self.content_path)
        print("任务的内容是:", text)
        if self.mission_is_open():
            alt_q()
        return text

    def get_mission_xy(self):
        text_list = self.read_mission()
        for text in text_list:
            print(text_list)
        """
        获取任务栏中的坐标，如果有多个坐标，仅返回第一个
        """
        return None


if __name__ == '__main__':
    load_driver()
    text = Mission().read_mission()
