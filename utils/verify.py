import torch
import os
import utils.constants as c
from utils.log import *
from PIL import Image
from torchvision import transforms


def verify():
    # 将4小人切分存到 c.temp_crop_dir 下，名为: 1.png 2.png 3.png 4.png
    img = Image.open(c.temp_popup)
    for i in range(4):
        img_crop = img.crop((i * 90, img.size[1] - 120, (i + 1) * 90, img.size[1]))
        img_crop.save(c.temp_crop4[i])

    # 定义神经网络参数
    class_names = ['front', 'others']
    model = torch.load("model/checkpoint.pth")
    transform = transforms.Compose([
        transforms.Resize((120, 90)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    # 使用模型识别
    files = os.listdir(c.temp_crop_dir)
    for i in range(4):
        image = Image.open(c.temp_crop_dir + files[i])
        image = transform(image)
        image = torch.reshape(image, (1, 3, 120, 90))
        tensor = image.cuda()
        outputs = model(tensor)
        index = outputs.argmax(1)
        percentage = torch.nn.functional.softmax(outputs, dim=1)[0][int(index)].item()
        result = class_names[index]
        if index == 0:
            info(i, "张图片识别结果:", result, "准确率:", percentage)
            return c.crop4_verify_offset[i]
    return -1
