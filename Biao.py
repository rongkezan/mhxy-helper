from Auto import *
from ImgOperation import *
import pyautogui


if __name__ == '__main__':
    load_driver()
    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t.startswith('梦幻西游 ONLINE'):
            title = t
            hwnd = win32gui.FindWindow(None, title)
            rect = win32gui.GetWindowRect(hwnd)
            # 最终需要移动到的坐标
            x_target = rect[0] + 74
            y_target = rect[1] + 78
            pyautogui.moveTo(x_target, y_target, 0.5)
            print("目标坐标:", x_target, y_target)
            # # 实际移动到的坐标
            time.sleep(0.5)
            shot()
            x_mouse, y_mouse = find_mouse_in_desktop()
            print("当前鼠标坐标:", x_mouse, y_mouse)
            time.sleep(2)
            # 需要相对移动的坐标
            x_rel = x_target - x_mouse
            y_rel = y_target - y_mouse
            print(x_rel, y_rel)
            pyautogui.moveRel(x_rel, y_rel, 0.5)

            left_click()