import torch
import torchvision
from PIL import Image

image_path = 'dataset/valid/front/2020_03_13_0313212710_1.jpg'
image = Image.open(image_path)
image = image.convert('RGB')
print(image)
transform = torchvision.transforms.Compose([torchvision.transforms.Resize((90, 120)),
                                            torchvision.transforms.ToTensor()])
image = transform(image)
print(image.shape)

model = torch.load("model/net_0.pth")
print(model)

image = torch.reshape(image, (1, 3, 90, 120))

model.eval()
with torch.no_grad():
    output = model(image)
    print(output)

print(output.argmax(1).item())
