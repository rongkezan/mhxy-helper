import os
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
import numpy as np
import torch
from torch import nn
import torch.optim as optim
import torchvision
from torchvision import transforms, models, datasets
import imageio
import time
import warnings
import random
import sys
import copy
import json
from PIL import Image

import util
import model
from train_model import train_model

data_dir = './dataset/'
train_dir = data_dir + '/train'
valid_dir = data_dir + '/valid'

data_transforms = {
    'train': transforms.Compose([
        transforms.CenterCrop(224),  # 从中心开始裁剪
        transforms.ColorJitter(brightness=0.2, contrast=0.1, saturation=0.1, hue=0.1),  # 参数1为亮度，参数2为对比度，参数3为饱和度，参数4为色相
        transforms.RandomGrayscale(p=0.025),  # 概率转换成灰度率，3通道就是R=G=B
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])  # 均值，标准差
    ]),
    'valid': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

# 数据集
image_datasets = {x: ImageFolder(os.path.join(data_dir, x), data_transforms[x]) for x in ['train', 'valid']}
dataloaders = {x: DataLoader(image_datasets[x], batch_size=8, shuffle=True) for x in ['train', 'valid']}
dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'valid']}
class_names = image_datasets['train'].classes

# 展示数据
# util.show_img(dataloaders['valid'], class_names)

# 是否用GPU训练
train_on_gpu = torch.cuda.is_available()

if not train_on_gpu:
    print('CUDA is not available.  Training on CPU ...')
else:
    print('CUDA is available!  Training on GPU ...')

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model_ft, input_size = model.initialize_model('resnet', 2, feature_extract=True, use_pretrained=True)

params_to_update = []
for name, param in model_ft.named_parameters():
    if param.requires_grad:
        params_to_update.append(param)
        print("\t", name)

# 优化器设置
optimizer_ft = optim.Adam(params_to_update, lr=1e-2)
scheduler = optim.lr_scheduler.StepLR(optimizer_ft, step_size=7, gamma=0.1)  # 学习率每7个epoch衰减成原来的1/10
# 最后一层已经LogSoftmax()了，所以不能nn.CrossEntropyLoss()来计算了，nn.CrossEntropyLoss()相当于logSoftmax()和nn.NLLLoss()整合
criterion = nn.NLLLoss()

model_ft, val_acc_history, train_acc_history, valid_losses, train_losses, LRs = \
    train_model(model_ft, dataloaders, criterion, optimizer_ft, 'checkpoint.pth', device, scheduler, num_epochs=20)


















# 利用DataLoader加载数据集
# data_loaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=batch_size, shuffle=True) for x in
#                 ['train', 'valid']}
# train_data_loader = DataLoader(train_data, batch_size=64)
# test_data_loader = DataLoader(test_data, batch_size=64)

# # 创建网络模型
# net = model.Net()
#
# # 创建损失函数
# loss_fn = nn.CrossEntropyLoss()
#
# # 优化器
# optimizer = torch.optim.SGD(net.parameters(), lr=0.01)
#
# # 设置训练网络的一些参数
# # 记录训练次数
# total_train_step = 0
# # 记录测试的次数
# total_test_step = 0
# # 记录训练的轮数
# epoch = 10
# # 添加Tensor Board
# writer = SummaryWriter("logs")
#
# for i in range(epoch):
#     print("--- 第 {} 轮训练开始 ---".format(i + 1))
#     # 训练步骤开始
#     total_train_loss = 0
#     total_train_accuracy = 0
#     for data in train_data_loader:
#         imgs, target = data
#         output = net(imgs)
#         loss = loss_fn(output, target)
#         total_train_loss += loss.item()
#         accuracy = (output.argmax(1) == target).sum().item()
#         total_train_accuracy += accuracy
#
#         # 优化器优化模型
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()
#
#         total_train_step += 1
#         if total_train_step % 10 == 0:
#             print("训练次数: {}, Loss: {}".format(total_train_step, loss.item()))
#             writer.add_scalar("train_loss", loss.item(), total_train_step)
#
#     print("整体训练集上的loss: {}".format(total_train_loss))
#     print("整体训练集上的准确率:{}".format(total_train_accuracy / train_data_size))
#     writer.add_scalar("train_loss", total_train_loss, total_test_step)
#     writer.add_scalar("train_accuracy", total_train_accuracy / train_data_size, total_test_step)
#
#     # 测试步骤开始
#     total_test_loss = 0
#     total_test_accuracy = 0
#     with torch.no_grad():
#         for data in test_data_loader:
#             imgs, target = data
#             output = net(imgs)
#             loss = loss_fn(output, target)
#             total_test_loss += loss.item()
#             accuracy = (output.argmax(1) == target).sum().item()
#             total_test_accuracy += accuracy
#     print("整体测试集上的loss: {}".format(total_test_loss))
#     print("整体测试集上的准确率:{}".format(total_test_accuracy / test_data_size))
#     writer.add_scalar("test_loss", total_test_loss, total_test_step)
#     writer.add_scalar("test_accuracy", total_test_accuracy / test_data_size, total_test_step)
#     total_test_step += 1
#     torch.save(net, "model/net_{}.pth".format(i))
#
# writer.close()
