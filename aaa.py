import cv2
import numpy


def locate(screen, wanted, show=0):
    loc_pos = []
    wanted, treshold, c_name = wanted
    result = cv2.matchTemplate(screen, wanted, cv2.TM_CCOEFF_NORMED)
    location = numpy.where(result >= treshold)

    h, w = wanted.shape[:-1]

    n, ex, ey = 1, 0, 0
    for pt in zip(*location[::-1]):
        x, y = pt[0] + int(w / 2), pt[1] + int(h / 2)
        if (x - ex) + (y - ey) < 15:  # 去掉邻近重复的点
            continue
        ex, ey = x, y

        cv2.circle(screen, (x, y), 10, (0, 0, 255), 3)

        x, y = int(x), int(y)
        loc_pos.append([x, y])

    if show:  # 在图上显示寻找的结果，调试时开启
        cv2.imshow('we get', screen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return loc_pos


if __name__ == '__main__':
    locate("")