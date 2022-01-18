import win32gui

hwnd_title = dict()


def get_mh_rect():
    h = get_mh_hwnd()
    return win32gui.GetWindowRect(h)


def get_mh_hwnd():
    win32gui.EnumWindows(__get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t.startswith('梦幻西游 ONLINE'):
            return h


def __get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
