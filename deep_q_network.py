import os
import torch
import torch.nn as nn


class DeepQNetwork(nn.Module):
    def __init__(self, path):
        super(DeepQNetwork, self).__init__()
        self.conv1 = nn.Sequential(nn.Linear(4, 64), nn.ReLU(inplace=True))
        self.conv2 = nn.Sequential(nn.Linear(64, 64), nn.ReLU(inplace=True))
        self.conv3 = nn.Sequential(nn.Linear(64, 1))
        self.epoch = 0

        self._create_weights()
        if os.path.isfile(path):
            self.load_existing_data_loader(path)

    def load_existing_data_loader(self, path):
        old_data_loader = torch.load(path)

        self.epoch = old_data_loader.epoch
        for attr in self.__dict__.keys():
            if attr not in old_data_loader.__dict__.keys():
                continue
            setattr(self, attr, getattr(old_data_loader, attr))
    def _create_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)
                nn.init.constant_(m.bias, 0)
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)

        return x
