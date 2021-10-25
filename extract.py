import numpy as np
import shutil
import os
from PIL import Image

path = "dataset/old/train/others/"
target_path = "dataset/train/others/"
files = os.listdir(path)
for file in files:
    if not file.startswith('.'):
        img = Image.open(path + file)
        if (np.array(img)[0][0] == [23, 34, 52]).all()\
                & (np.array(img)[0][1] == [23, 34, 52]).all()\
                & (np.array(img)[0][2] == [23, 34, 52]).all():
            pass
        else:
            shutil.copy(path + file, target_path + file)
