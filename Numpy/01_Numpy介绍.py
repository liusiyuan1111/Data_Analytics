#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Data_Analytics
File Name: 01_Numpy介绍.py
Author: lsy
Create Date: 2021-10-4
-------------------------------------------------
"""

import numpy as np
import time

# python列表
t1 = time.time()
a = []
for x in range(1000000):
    a.append(x**2)
t2 = time.time()
print(t2-t1)

# Numpy数组
t3 = time.time()
b = np.arange(1000000,dtype='i8')**2
t4 = time.time()
print(t4-t3)