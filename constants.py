import os

# 截图存档目录
flag_dir = "img/flag/"
temp_dir = "img/temp/"
temp_crop_dir = "img/temp/crop"
data_dir = "img/data/"
driver_dir = "driver/"

# 截图名称
temp_game = os.path.join(temp_dir, 'temp_game.jpg')
temp_desktop = os.path.join(temp_dir, 'temp_desktop.jpg')
temp_popup = os.path.join(temp_dir, 'temp_popup.jpg')
temp_fight = os.path.join(temp_dir, 'temp_fight.jpg')
temp_crop4 = [os.path.join(temp_crop_dir, name) for name in ['1.jpg', '2.jpg', '3.jpg', '4.jpg']]
flag_fight = os.path.join(flag_dir, 'fight_flag.jpg')
flag_popup = os.path.join(flag_dir, 'popup_flag.jpg')
flag_mouse = os.path.join(flag_dir, 'mouse_flag.jpg')

# 尺寸及偏移
fight_shape = (795, 179, 805, 438)      # 战斗截图Shape
screen_size = (812, 663)                # 屏幕尺寸
sub_size = (360, 134)                   # 四小人大小
popup_move_shape = (-56, 16, 118, 130)  # 弹框偏移
mouse_move_shape = (16, 15)             # 鼠标偏移

# Driver
driver_name = 'kmclass'
kmclass_dll_path = os.path.abspath(driver_dir + 'kmclassdll.dll').replace('\\', '\\\\')
kmclass_driver_path = os.path.abspath(driver_dir + 'kmclass.sys').replace('\\', '\\\\')
