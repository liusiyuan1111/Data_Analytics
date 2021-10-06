#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Data_Analytics
File Name: 案例01_图片数组的索引和切片.py
Author: lsy
Create Date: 2021-10-6
-------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt

img_path = "res/guido.jpg"
guido_img = plt.imread(img_path)
print(guido_img)   #输出数组
print(type(guido_img)) #获取到的类型
print(guido_img.shape)  #数组形状
print(guido_img.dtype)  #数组的数据类型
print(guido_img.ndim)  #数组的维度
print(guido_img.size)  #数组的大小

plt.imshow(guido_img)  #显示图像
plt.show()
plt.imshow(guido_img[20:450,100:400])  #把头切出来
plt.show()
plt.imshow(guido_img[::-1])  #垂直翻转(行反向切片)
plt.show()
plt.imshow(guido_img[:,::-1])  #水平翻转(列反向切片)
plt.show()
plt.imshow(guido_img[:,:,::-1])  #反色(RGB反向切片)
plt.show()


