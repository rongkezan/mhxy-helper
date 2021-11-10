import torch
import os
from PIL import Image
from torchvision import transforms


def recognize():
    path = "resources/img/temp_crop/"
    files = os.listdir(path)
    n = 0
    for file in files:
        image = Image.open(path + file)
        class_names = ['front', 'others']
        transform = transforms.Compose([
            transforms.Resize((120, 90)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        image = transform(image)
        image = torch.reshape(image, (1, 3, 120, 90))

        model = torch.load("model/checkpoint.pth")
        tensor = image.cuda()
        outputs = model(tensor)
        index = outputs.argmax(1)
        percentage = torch.nn.functional.softmax(outputs, dim=1)[0][int(index)].item()
        result = class_names[index]
        print('index:', index, 'predicted:', result, ', percentage:', percentage)
        position = [(310, 340), (430, 340), (550, 340), (670, 340)]
        if index == 0:
            return position[n]
        n += 1
    return -1


if __name__ == '__main__':
    print(recognize())