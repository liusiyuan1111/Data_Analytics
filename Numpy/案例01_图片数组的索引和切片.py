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
print(guido_img)
print(guido_img.shape)
print(guido_img.dtype)
print(guido_img.ndim)
print(guido_img.size)
print(type(guido_img))
plt.imshow(guido_img)
plt.show()
plt.imshow(guido_img[::-1])
plt.show()
plt.imshow(guido_img[:,::-1])
plt.show()
plt.imshow(guido_img[20:450,100:400])
plt.show()
plt.imshow(guido_img[:,:,::-1])
plt.show()
plt.imshow(guido_img[:-1])
plt.show()

