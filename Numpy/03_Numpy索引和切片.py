#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Data_Analytics
File Name: 03_Numpy索引和切片.py
Author: lsy
Create Date: 2021-10-5
-------------------------------------------------
"""
import numpy as np

# 一、获取某行的数据
# 1. 如果是一维数组
a = np.arange(12)
print(a[1])  #获取下标为1的元素

# 2. 如果是二维数组
a1 = a.reshape(3,4)
print(a1[1])   #获取第1行的元素（和下标一样，从0开始计数）

# 3. 如果是三维数组
a2 = a.reshape(2,3,2)
print(a2[1])  #获取第1块的元素

# 二、获取某几行的数据
a = np.arange(0,24).reshape(4,6)  #创建一个4行6列的数组

# 1. 获取连续几行
print(a[1:3])  #获取第1-2行的数据（左闭右开）

# 2. 获取不连续的几行
print(a[[0,2,3]])  #获取第0、2、3行的数据

# 3. 使用负数索引(从后往前)
print(a[[-1,-2]])  #获取倒数第1行、倒数第2行的数据

# 4.数据翻转
print(a[::-1])  #行翻转
print(a[:,::-1])  #列翻转
print(a[::-1,::-1]) #数组所有元素翻转

# 三、获取某行某列的数据
print(a[1,1])  #获取第1行1列的数据
print(a[0:2,0:2]) #获取第0-1行、0-1列的数据
print(a[[1,2],[2,3]])  #花式索引，获取到第1行2列、第2行3列的两个数据

# 四、获取某列的数据
print(a[:,1])  #获取第1列的数据(注意冒号不能省略)


#小结
'''
1.如果数组是一维的，那么与Python列表的索引和切片完全一致
2.如果数组是多维的，那么使用逗号分隔，逗号前面的是行，逗号后面的是列，如果只有一个值，那么代表的是行
'''
