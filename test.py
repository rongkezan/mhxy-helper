def func_a(a, func1, *args, **kwargs):
    print(1, func1(*args, **kwargs))


def func_b(*args, **kwargs):
    return args, kwargs


if __name__ == '__main__':
    # func_a(1, func_b, 1, 2, 3)
    res = func_b(1, 2, 3, a=1)
    print(type(res[1]))