import os

# 目录
base_dir = os.path.abspath(os.path.dirname(__file__)) + "/resources"
flag_dir = os.path.join(base_dir, "/img/flag")
temp_dir = os.path.join(base_dir, "/img/temp")
data_dir = os.path.join(base_dir, "/img/data")

flag_ch_dir = os.path.join(flag_dir, "/ch")
temp_ch_dir = os.path.join(temp_dir, "/ch")
temp_crop_dir = os.path.join(temp_dir, "/crop")
data_monster_dir = os.path.join(data_dir, "/monster")
data_crop_dir = os.path.join(data_dir, "/crop")

# 文件路径
flag_fight = os.path.join(flag_dir, 'fight_bar.png')
flag_auto_fight = os.path.join(flag_dir, 'fight_auto.png')
flag_popup = [os.path.join(flag_dir, name) for name in ['popup1.png', 'popup2.png']]
flag_cargo = os.path.join(flag_dir, 'cargo.png')
flag_mouse = os.path.join(flag_dir, 'mouse.png')
flag_yz = [os.path.join(flag_ch_dir, name) for name in ['yz1.png', 'yz2.png', 'yz3.png', 'yz4.png']]
temp_game = os.path.join(temp_dir, 'game.png')
temp_desktop = os.path.join(temp_dir, 'desktop.png')
temp_popup = os.path.join(temp_dir, 'popup.png')
temp_crop4 = [os.path.join(temp_crop_dir, name) for name in ['1.png', '2.png', '3.png', '4.png']]
temp_place1 = os.path.join(temp_dir, "place1.png")
temp_place2 = os.path.join(temp_dir, "place2.png")
temp_tab_group = os.path.join(temp_ch_dir, "ch.png")
model_path = os.path.join(base_dir, "checkpoint.pth")


class Tab:
    def __init__(self, shape, path, position):
        self.shape = shape
        self.path = path
        self.position = position


temp_tabs = [
    Tab((0, 0, 145, 20), os.path.join(temp_ch_dir, 'ch1.png'), (80, 40)),
    Tab((154, 0, 299, 20), os.path.join(temp_ch_dir, 'ch2.png'), (234, 40)),
    Tab((308, 0, 453, 20), os.path.join(temp_ch_dir, 'ch3.png'), (388, 40)),
    Tab((462, 0, 607, 20), os.path.join(temp_ch_dir, 'ch4.png'), (542, 40)),
    Tab((615, 0, 760, 20), os.path.join(temp_ch_dir, 'ch5.png'), (696, 40)),
]

# 四小人识别图片距离截图左上角的偏移
crop4_verify_offset = [(-60, 100), (30, 100), (120, 100), (210, 100)]

# DD 驱动
dd_dll_path = os.path.abspath(base_dir + 'DD94687.64.dll')