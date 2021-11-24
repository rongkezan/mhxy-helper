import os

# 截图存档目录
flag_dir = "../resources/img/flag/"
flag_character_dir = "../resources/img/flag/character/"
temp_dir = "../resources/img/temp/"
temp_ch_dir = "../resources/img/temp/ch/"
temp_crop_dir = "../resources/img/temp/crop"
data_dir = "../resources/img/data/"
driver_dir = "../resources/"

# 截图名称
temp_game = os.path.join(temp_dir, 'game.png')
temp_desktop = os.path.join(temp_dir, 'desktop.png')
temp_popup = os.path.join(temp_dir, 'popup.png')
temp_crop4 = [os.path.join(temp_crop_dir, name) for name in ['1.png', '2.png', '3.png', '4.png']]
flag_fight = os.path.join(flag_dir, 'fight_bar.png')
flag_auto_fight = os.path.join(flag_dir, 'fight_auto.png')
flag_popup = os.path.join(flag_dir, 'popup.png')
flag_mouse = os.path.join(flag_dir, 'mouse.png')
flag_yz = [os.path.join(flag_character_dir, name) for name in ['yz1.png', 'yz2.png', 'yz3.png', 'yz4.png']]
ch_temp_img = os.path.join(temp_ch_dir, "ch.png")
ch_dict = {
    'ch1': ((0, 0, 145, 20), os.path.join(temp_ch_dir, 'ch1.png'), (80, 40)),
    'ch2': ((154, 0, 299, 20), os.path.join(temp_ch_dir, 'ch2.png'), (234, 40)),
    'ch3': ((308, 0, 453, 20), os.path.join(temp_ch_dir, 'ch3.png'), (388, 40)),
    'ch4': ((462, 0, 607, 20), os.path.join(temp_ch_dir, 'ch4.png'), (542, 40)),
    'ch5': ((615, 0, 760, 20), os.path.join(temp_ch_dir, 'ch5.png'), (696, 40))
}
# Driver
dd_dll_path = os.path.abspath(driver_dir + 'DD94687.64.dll')
