#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: 05文件操作.py
File Name: numpy第一次作业.py
Author: lsy
Create Date: 2021-10-18
-------------------------------------------------
"""

import numpy as np

# 一、自己创建一个一维数组，将数组中的奇数全部替换成-1
a1 = np.arange(10)
a1[a1%2 != 0] = -1
print(a1)

# 二、创建一个`4行4列`的随机数组（比如：`np.random.randint(0,10,size=(4,4))`），请将其中对角线的数取出来形成一个一维数组。提示（使用`np.eye`）。
a2 = np.random.randint(0,10,size=(4,4))
eye = np.eye(4,dtype=bool)
print(a2)
print(a2[eye])


# 三、创建一个`4行4列`的随机数组，请取出其中`(0,0),(1,2),(3,2)`的点
a3 = np.random.randint(0,10,size=(4,4))
points = a3[[0,1,3],[0,2,2]]
print(a3)
print(points)

# 四、创建一个`4行4列`的随机数组，请取出其中`2-3`行（`包括第3行`）的所有数据
a4 = np.random.randint(0,10,size=(4,4))
lines = a4[2:4]
print(a4)
print(lines)

# 五、创建一个`8行9列`的随机数组，请将其中`1-5`行（`包含第5行`）的`第8列大于3`的数全部都取出来
a5 = np.random.randint(0,10,size=(8,9))
# 先获取指定部分的数据条件的数组
conditions = a5[1:6,8] > 3
print(conditions)
# 再获取指定部分的数据
datas = a5[1:6,8]
print(datas)
# 再从数组中提取符合条件的数据
result = datas[conditions]
print(result)
