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

a = [1,2,3,'4']
a = [1,2,3,4.0]

# numpy数组的创建
# 1.通过python列表生成数组
a1 = np.array(a)

# 2.通过np.arange生成数组（用法和python的range类似）
a2 = np.arange(2,10,2)

# 3.通过np.random生成随机数的数组
a3 = np.random.random()  #返回一个0-1的数
a3 = np.random.random((2,2))  # 返回一个2行2列的数组
a3 = np.random.randint(0,10,size=(2,2))  # 从0-10之间随机生成一个2行2列的数组

# 4.使用函数生成特殊的数组
a4_z = np.zeros((3,3))  #返回一个元素全为0的3行3列的数组
a4_o = np.ones((4,4))   #返回一个元素全为1的4行4列的数组
a4_f = np.full((3,3),8)  #返回一个元素全为8的3行3列的数组
a4_e = np.eye(4)    #返回一个4行4列的单位矩阵


# 总结
'''
1.数组的数据类型都是一致的，不能同时出现多种数据类型
2.创建数组的四种方式：
    np.array
    np.arange
    np.random
    特殊函数
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

# 多维数组
# 1.获取数组的维数np.ndim
a1 = np.array([1,2,3])
print(a1.ndim)  #一维数组
a2 = np.array([1,2,3],[4,5,6])
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