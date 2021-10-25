import torch
import torchvision
import os
from PIL import Image

path = "dataset/test/"
files = os.listdir(path)
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

    _, indices = torch.max(outputs,1)
    percentage = torch.nn.functional.softmax(outputs, dim=1)[0]
    perc = percentage[int(indices)].item()
    result = class_names[indices]
    print('predicted:', result, ', percentage:', perc)
