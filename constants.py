import os

# 截图存档目录
flag_dir = "img/flag/"
data_dir = "img/data/"
temp_dir = "img/temp/"

sc_img = os.path.join(temp_dir, 'temp_game.jpg')
desktop_img = os.path.join(temp_dir, 'temp_desktop.jpg')
popup_img = os.path.join(temp_dir, 'popup_sub.jpg')
fight_img = os.path.join(flag_dir, 'fight_flag.jpg')
fighting_flag_img_path = os.path.join(flag_dir, 'fight_flag.jpg')
popup_flag_img = os.path.join(flag_dir, 'popup_flag.jpg')
mouse_flag_img = os.path.join(flag_dir, 'mouse_flag.jpg')
fight_shape = (795, 179, 805, 438)  # 战斗截图Shape
screen_size = (812, 663)
sub_size = (360, 134)  # 四小人大小
popup_move_shape = (-56, 16, 118, 130)  # 弹框偏移
mouse_move_shape = (16, 15)  # 鼠标偏移
