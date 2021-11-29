#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Matplotlib
File Name: 00基本使用.py
Author: lsy
Create Date: 2021-11-29
-------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
y = np.random.randint(0,10,size=(10,))
plt.figure()
plt.plot(x,y)
plt.show()