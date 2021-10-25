import util
import auto
import torch
import snap_4 as snap
import torchvision


if __name__ == '__main__':
    util.log_title("开始")
    auto.open_driver()
    model = torch.load("model/checkpoint.pth")
    transform = torchvision.transforms.Compose([
        torchvision.transforms.Resize((120, 90)),
        torchvision.transforms.ToTensor()
    ])
    while True:
        util.log_h1_start(f'开始')
        if snap.task():
            image = torch.reshape(image, (4, 3, 120, 90))

