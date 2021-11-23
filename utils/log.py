import time


def info(msg, *args):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(now, "[Info]", msg, *args)


def warn(msg, *args):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(now, "[Warn]", msg, *args)


def error(msg, *args):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(now, "[Error]", msg, *args)