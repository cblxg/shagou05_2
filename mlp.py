# 全连接层的实现
import torch.nn as nn    # 导入torch.nn模块

class Net(nn.Module):    # 定义Net类，继承nn.Module类
    def __init__(self, input_size, hidden_size, num_classes):    # 定义Net类的初始化函数
        super(Net, self).__init__()    # 调用父类的初始化函数
        self.fc1 = nn.Linear(input_size, hidden_size)    # 定义全连接层1    

    
        self.relu = nn.ReLU()    # 定义激活函数ReLU
        self.fc2 = nn.Linear(hidden_size, num_classes)    # 定义全连接层2

    def forward(self, x):    # 定义Net类的前向传播函数
        out = self.fc1(x)    # 全连接层1的输出
        out = self.relu(out)    # 激活函数ReLU的输出
        out = self.fc2(out)    # 全连接层2的输出
        return out    # 返回输出