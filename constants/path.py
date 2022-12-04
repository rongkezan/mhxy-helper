import os

# 目录
base_dir = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "resources/")
flag_dir = os.path.join(base_dir, "img/flag")
temp_dir = os.path.join(base_dir, "img/temp")
data_dir = os.path.join(base_dir, "img/data")
item_dir = os.path.join(base_dir, "img/item")
model_dir = os.path.join(base_dir, "model")

flag_common_dir = os.path.join(flag_dir, "common")
flag_npc_dir = os.path.join(flag_dir, "npc")

temp_common_dir = os.path.join(temp_dir, "common")
temp_crop_dir = os.path.join(temp_dir, "crop")
temp_mission_dir = os.path.join(temp_dir, "mission")
temp_npc_dir = os.path.join(temp_dir, "npc")
temp_tab_dir = os.path.join(temp_dir, "tab")

data_crop_dir = os.path.join(data_dir, "crop")
data_game_dir = os.path.join(data_dir, "game")
data_mission_dir = os.path.join(data_dir, "mission")

# 文件路径
flag_fight = os.path.join(flag_common_dir, 'fight_bar.png')
flag_auto_fight = os.path.join(flag_common_dir, 'fight_auto.png')
flag_popup1 = os.path.join(flag_common_dir, 'popup1.png')
flag_popup2 = os.path.join(flag_common_dir, 'popup2.png')
flag_mouse = os.path.join(flag_common_dir, 'mouse.png')
flag_yz = [os.path.join(flag_npc_dir, name) for name in ['yz1.png', 'yz2.png', 'yz3.png', 'yz4.png']]

temp_game = os.path.join(temp_common_dir, 'game.png')
temp_desktop = os.path.join(temp_common_dir, 'desktop.png')
temp_popup = os.path.join(temp_common_dir, 'popup.png')
temp_place1 = os.path.join(temp_common_dir, "place1.png")
temp_place2 = os.path.join(temp_common_dir, "place2.png")
temp_crop4 = [os.path.join(temp_crop_dir, name) for name in ['1.png', '2.png', '3.png', '4.png']]
temp_tab_group = os.path.join(temp_tab_dir, "tab.png")


class Tab:
    def __init__(self, shape, path, position):
        self.shape = shape
        self.path = path
        self.position = position


temp_tabs = [
    Tab((0, 0, 145, 20), os.path.join(temp_npc_dir, 'ch1.png'), (80, 40)),
    Tab((154, 0, 299, 20), os.path.join(temp_npc_dir, 'ch2.png'), (234, 40)),
    Tab((308, 0, 453, 20), os.path.join(temp_npc_dir, 'ch3.png'), (388, 40)),
    Tab((462, 0, 607, 20), os.path.join(temp_npc_dir, 'ch4.png'), (542, 40)),
    Tab((615, 0, 760, 20), os.path.join(temp_npc_dir, 'ch5.png'), (696, 40)),
]

# 四小人识别图片距离截图左上角的偏移
crop4_verify_offset = [(45, 75), (135, 75), (225, 75), (315, 75)]

# DD 驱动
dd_dll_path = os.path.abspath(base_dir + '/DD94687.64.dll')