import os

# 截图存档目录
flag_dir = "img/flag/"
temp_dir = "img/temp/"
ch_temp_dir = "img/temp/ch/"
temp_crop_dir = "img/temp/crop"
data_dir = "img/data/"
driver_dir = "driver/"

# 截图名称
temp_game = os.path.join(temp_dir, 'temp_game.jpg')
temp_desktop = os.path.join(temp_dir, 'temp_desktop.jpg')
temp_popup = os.path.join(temp_dir, 'temp_popup.jpg')
temp_fight = os.path.join(temp_dir, 'temp_fight.jpg')
temp_crop4 = [os.path.join(temp_crop_dir, name) for name in ['1.jpg', '2.jpg', '3.jpg', '4.jpg']]
flag_fight = os.path.join(flag_dir, 'fight_bar.png')
flag_auto_fight = os.path.join(flag_dir, 'fight_auto.png')
flag_popup = os.path.join(flag_dir, 'popup.png')
flag_mouse = os.path.join(flag_dir, 'mouse.png')
ch_temp_img = os.path.join(ch_temp_dir, "ch.png")
ch_dict = {
    'ch1': ((0, 0, 145, 20), os.path.join(ch_temp_dir, 'ch1.png'), (80, 40)),
    'ch2': ((154, 0, 299, 20), os.path.join(ch_temp_dir, 'ch2.png'), (234, 40)),
    'ch3': ((308, 0, 453, 20), os.path.join(ch_temp_dir, 'ch3.png'), (388, 40)),
    'ch4': ((462, 0, 607, 20), os.path.join(ch_temp_dir, 'ch4.png'), (542, 40)),
    'ch5': ((615, 0, 760, 20), os.path.join(ch_temp_dir, 'ch5.png'), (696, 40))
}
# 尺寸及偏移
fight_shape = (795, 190, 805, 430)  # 战斗截图Shape
screen_size = (812, 663)  # 屏幕尺寸
position = [(310, 340), (430, 340), (550, 340), (670, 340)]
sub_size = (360, 134)  # 四小人大小
popup_move_shape = (-56, 16, 118, 130)  # 弹框偏移
mouse_move_shape = (16, 15)  # 鼠标偏移

# Driver
dd_dll_path = os.path.abspath(driver_dir + 'DD94687.64.dll')
