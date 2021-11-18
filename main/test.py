# from utils.mission import Mission
# from utils.map import *
# from utils.game_watcher import *
# from utils.game_action import *
# from utils.bag import Bag
from utils.txt import *
import os
import utils.constants as c
import re


if __name__ == '__main__':
    # mission = Mission()
    # mission.shot_mission()
    words = read_text_basic(os.path.join(c.temp_dir, "7.png"))
    print(words)
    words = words.split('(')[0]
    print(words)
    number = re.sub("\D", "_", words)
    print(number)
    list = number.split('_')
    print(list)
    result = []
    for item in list:
        if item != "":
            result.append(item)
    print(result)