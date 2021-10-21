import numpy as np
import matplotlib.pyplot as plt
import os
import uuid
from PIL import Image


def img_convert(tensor):
    image = tensor.to("cpu").clone().detach()
    image = image.numpy().squeeze()
    image = image.transpose(1, 2, 0)
    image = image * np.array((0.229, 0.224, 0.225)) + np.array((0.485, 0.456, 0.406))
    image = image.clip(0, 1)
    return image


def show_img(dataloader, class_names):
    """ 展示数据"""
    fig = plt.figure(figsize=(20, 12))
    columns = 4
    rows = 2
    dataiter = iter(dataloader)
    inputs, classes = dataiter.next()

    for idx in range(columns * rows):
        ax = fig.add_subplot(rows, columns, idx + 1, xticks=[], yticks=[])
        ax.set_title(class_names[classes[idx]])
        plt.imshow(img_convert(inputs[idx]))
    plt.show()


def crop(source_dir, target_dir):
    files = os.listdir(source_dir)
    for file in files:
        img = Image.open(source_dir + file)
        uid = str(uuid.uuid1())
        for i in range(4):
            img_crop = img.crop((i * 90, img.size[1] - 120, (i + 1) * 90, img.size[1]))
            img_crop.save(target_dir + uid + "-" + str(i + 1) + ".jpg")


# -*- coding: utf-8 -*-
##########################
####    工具类        ####
##########################
def log_title(title):
    print()
    print(f'--------   {title}    ----------')
    print()


def log_h1(h1):
    print()
    print()
    print(f'==========    {h1}    =============')
    print()
    print()


def log_h1_start(h1):
    print_newLine(8)
    print('=============================================================')
    print(f'====================    {h1}    =========================')
    print()


def log_h1_end(h1):
    print()
    print(f'================    {h1}    ===================')
    print('=============================================================')
    print_newLine(8)


def print_newLine(n):
    for i in range(n):
        print()
