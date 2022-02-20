import torch
import os
import shutil
import constants.path as p
import auto.utils.log as log
import time
from PIL import Image
from torchvision import transforms
from auto.component.action import action
from auto.component.camera import camera

model_path = os.path.join(p.model_dir, "checkpoint.pth")


def handle_popup():
    popup_result = camera.is_popup1()
    if popup_result is not None:
        save_crop4()
        verify_result = verify()
        if verify_result != -1:
            x, y = popup_result[0] + verify_result[0], popup_result[1] + verify_result[1]
            action.move_left_click(x, y)


def save_crop4():
    log.info("战斗出现弹框，保存4小人图片")
    shutil.copy(p.temp_popup, os.path.join(p.data_crop_dir, str(int(round(time.time() * 1000))) + ".png"))


def verify():
    # 将4小人切分存到 path.temp_crop_dir 下，名为: 1.png 2.png 3.png 4.png
    img = Image.open(p.temp_popup)
    for i in range(4):
        img_crop = img.crop((i * 90, img.size[1] - 120, (i + 1) * 90, img.size[1]))
        img_crop.save(p.temp_crop4[i])

    # 定义神经网络参数
    class_names = ['front', 'others']
    model = torch.load(model_path)
    transform = transforms.Compose([
        transforms.Resize((120, 90)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    # 使用模型识别
    per_dict = dict()
    files = os.listdir(p.temp_crop_dir)
    for i in range(4):
        image = Image.open(os.path.join(p.temp_crop_dir, files[i]))
        image = transform(image)
        image = torch.reshape(image, (1, 3, 120, 90))
        tensor = image.cuda()
        outputs = model(tensor)
        index = outputs.argmax(1)
        percentage = torch.nn.functional.softmax(outputs, dim=1)[0][int(index)].item()
        result = class_names[index]
        log.info(i, "张图片识别结果:", result, "准确率:", percentage)
        per_dict[i] = percentage
        if index == 0:
            return p.crop4_verify_offset[i]
    return p.crop4_verify_offset[min(per_dict)]
