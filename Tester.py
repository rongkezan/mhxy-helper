from ImgOperation import *
import time

if __name__ == '__main__':
    image1 = cv.imread("img/ch/init/ch1.png")
    image2 = cv.imread("img/ch/init/ch2.png")
    image3 = cv.imread("img/ch/init/ch3.png")
    print(image1[10][115])
    print(image2[10][115])
    print((image3[10][115] == [155, 202, 254]).all())
