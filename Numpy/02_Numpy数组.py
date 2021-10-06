#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Data_Analytics
File Name: 02_Numpy数组.py
Author: lsy
Create Date: 2021-10-4
-------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt

a = [1,2,3,'4']
a = [1,2,3,4.0]

# numpy数组的创建
# 1.通过python列表生成数组
a1 = np.array(a)

# 2.从头开始创建数组
# 通过np.arange生成数组（用法和python的range类似）
a2 = np.arange(2,10,2)
#通过np.linspace生成数组
a3 = np.linspace(0,1,6)

# 3.通过np.random生成随机数的数组
a3 = np.random.random()  #返回一个0-1的数
a3 = np.random.random((2,2))  # 返回一个2行2列的数组
a3 = np.random.randint(0,10,size=(2,2))  # 从0-10之间随机生成一个2行2列的数组

# 4.使用函数生成特殊的数组
a4_z = np.zeros((3,3))  #返回一个元素全为0的3行3列的数组
a4_o = np.ones((4,4))   #返回一个元素全为1的4行4列的数组
a4_f = np.full((3,3),8)  #返回一个元素全为8的3行3列的数组
a4_e = np.eye(4)    #返回一个4行4列的单位矩阵
a4_em = np.empty((3,3))  #返回一个3行3列的数组，数组元素内容初始化为随机值，取决于内存的状态

# 5.使用图片生成三维数组
import matplotlib.pyplot as plt
img_path = "Numpy/res/guido.jpg"
a5_img = plt.imread(img_path)


# 总结
'''
1.数组的数据类型都是一致的，不能同时出现多种数据类型
2.创建数组的四种方式：
    np.array
    np.arange  np.linspace
    np.random
    特殊函数
    文件获取
'''

# 数组的数据类型
# 1.查看数组的数据类型
a = [1,2,3,4]
a1 = np.array(a)
print(a1)
print(a1.dtype)   # 默认是int32

# 2.指定数组的数据类型
a2 = np.array(a,dtype=np.float16)
a2 = np.array(a,dtype='f8')  #也可以通过标识符指定
print(a2)
print(a2.dtype)

# 3.修改数组的数据类型
print(a1.dtype)  #得到a1数组当前的数据类型是int32
a3 = a1.astype(np.int8)
print(a3)
print(a3.dtype)
a3 = a1.astype('f2')  #同样可以通过标识符修改为float16
print(a3)
print(a3.dtype)

# 数组的属性
# 1.数组的维数np.ndim
a1 = np.array([1,2,3])
print(a1.ndim)  #一维数组
a2 = np.array([[1,2,3],[4,5,6]])
print(a2.ndim)
a3 = np.array(
    [
        [
            [1,2,3],[4,5,6]
        ],
        [
            [7,8,9],[10,11,12]
        ]

    ]
)
print(a3)
print(a3.ndim)

a4 = np.array([[1,2,3],[4,5]])
print(a4)  # 输出[list([1, 2, 3]) list([4, 5])]，其中最外面层是数组，里面是Python列表
print(a4.ndim)  # 输出1，表明a4是一个一维数组

# 2.数组的形状np.shape
print(a1.shape) # 输出(3,)，意思是一维数组，有3个数据
print(a2.shape) # 输出(2,3)，意思是二维数组，2行3列
print(a3.shape) # 输出(2,2,3)，意思是三维数组，总共有2个元素，每个元素是2行3列的
print(a4.shape) # 输出(2,)，意思是a4是一个一维数组，总共有2列

# 修改数组的形状np.reshape
a1 = np.arange(12)  #一维数组，有12个元素
a2 = a1.reshape((3,4))  #变成3行4列的二维数组
a3 = a1.reshape((2,3,2)) #变成一个3维数组，总共有2块，每一块是3行2列的
a4 = a3.reshape((12,))  #将a3的三维数组重新变回12个元素的一维数组
a5 = a3.flatten()   #不管a3是几维数组，都变回一维数组

# 注意：reshape不会修改原数组本身，而是将修改结果返回

# 3.数组的个数
a1 = np.array([[1,2,3],[4,5,6]])
print(a1.size) #打印的是6，因为总共有6个元素

# 4.数组每个元素占的大小
a1 = np.array([1,2,3],dtype=np.int32)
print(a1.itemsize) # 打印4，因为每个字节是8位，32位/8=4个字节

# 5.数组元素消耗的总字节数
a1 = np.array([1, 2, 3], dtype=np.int32)
print(a1.nbytes)  # 打印12，因为总共有3个元素。每个元素占4个字节

