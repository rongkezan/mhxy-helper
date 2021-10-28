import torch
import torchvision
import os
import constants as c
from PIL import Image


def recognize():
    path = "img/temp/crop/"
    files = os.listdir(path)
    n = 0
    for file in files:
        image = Image.open(path + file)
        image = image.convert('RGB')
        class_names = ['front', 'others']
        transform = torchvision.transforms.Compose([
            torchvision.transforms.Resize((120, 90)),
            torchvision.transforms.ToTensor()
        ])
        image = transform(image)
        model = torch.load("model/checkpoint.pth")
        image = torch.reshape(image, (1, 3, 120, 90))
        outputs = model(image)
        index = outputs.argmax(1)
        percentage = torch.nn.functional.softmax(outputs, dim=1)[0][int(index)].item()
        result = class_names[index]
        print('predicted:', result, ', percentage:', percentage)
        if index == 0:
            return c.position[n]
        n += 1
        return -1


if __name__ == '__main__':
    recognize()