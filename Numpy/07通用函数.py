#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: 05文件操作.py
File Name: 07通用函数.py
Author: lsy
Create Date: 2021-10-18
-------------------------------------------------
"""
import numpy as np

# 布尔数组的函数
a = np.random.randint(100000)
np.all(a == 0)  #数组中是不是所有的元素都为0
np.any(a == 0)  #数组中是否有为0的元素

# 排序
# 1.np.sort()
a = np.random.randint(0,10,size=(3,5))
b = np.sort(a)   #默认按照最里面的括号元素进行排序
c = np.sort(a,axis=0)  #可以指定按照最外面括号的元素进行排序
a.sort()  #如果使用这种方式会改变原数组

# 2.np.argsort()
a = np.random.randint(0,10,size=(3,5))
np.argsort(a,axis=0)   #返回排序后的下标

# 3.降序
a = np.random.randint(0,10,size=(3,5))
-np.sort(-a)

