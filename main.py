from robot_scene import Scene
from robot_pick import Pick
from robot_xf import Xf

mode = 1

if __name__ == "__main__":
    if mode == 1:
        Scene().run()
    elif mode == 2:
        Pick().run()
    elif mode == 3:
        Xf().run()
