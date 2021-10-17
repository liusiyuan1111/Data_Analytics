#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Numpy
File Name: 06numpy其他.py
Author: lsy
Create Date: 2021-10-17
-------------------------------------------------
"""

import numpy as np

#NAN值
print(np.NAN == np.NAN)
print(np.NAN-1)
print(np.isnan(np.NAN))
print(type(np.NAN))

#删除缺失值
#1.删除所有NAN的值
data = np.random.randint(0,10,size=(3,5)).astype(float)
data[[0,1]] = np.NAN
data = data[~np.isnan(data)] #此时会删除所有NAN值，并且返回一个一维数组

#2.删除NAN值所在的行
data = np.random.randint(0,10,size=(5,3)).astype(float)
data[[0,1],[1,2]] = np.NAN
lines = np.where(np.isnan(data))[1]
data = np.delete(data,lines,axis=1)

#3.替换NAN值
data = np.random.randint(0,10,size=(5,3)).astype(float)
data[[0,1],[1,2]] = np.NAN
data[np.isnan(data)] = 0. #通过不二索引将NAN值替换成0

# random
#1.random.seed
#不使用seed
print(np.random.random()) # 打印一个随机值
print(np.random.random()) # 打印一个不同的随机值

np.random.seed(1)
print(np.random.random()) # 打印一个随机值
np.random.seed(1)
print(np.random.random()) # 打印和之前相同的随机值

#2.random.randn
data = np.random.randn(2,3)

#3.random.randint
data1 = np.random.randint(10,size=(3,5)) #生成值在0-10之间，3行5列的数组
data2 = np.random.randint(1,20,size=(3,6)) #生成值在1-20之间，3行6列的数组

#4.random.choice
data = [4,65,6,3,5,73,23,5,6]
result1 = np.random.choice(data,size=(2,3)) #从data中随机采样，生成2行3列的数组
result2 = np.random.choice(data,3) #从data中随机采样3个数据形成一个一维数组
result3 = np.random.choice(10,3) #从0-10之间随机取3个值

#5.random.shuffle
a = np.arange(10)
np.random.shuffle(a) #将a的元素的位置都会进行随机更换
