#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Matplotlib
File Name: 01条形图.py
Author: lsy
Create Date: 2021-11-29
-------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

movies = {
    "流浪地球":40.78,
    "飞驰人生":15.77,
    "疯狂的外星人":20.83,
    "新喜剧之王":6.10,
    "廉政风云":1.10,
    "神探蒲松龄":1.49,
    "小猪佩奇过大年":1.22,
    "熊出没·原始时代":6.71
}
x = list(movies.keys())
y = list(movies.values())
plt.figure(figsize=(10,10))
plt.bar(x,y)
plt.xticks(rotation=60)
plt.yticks(range(0,45,5),["%d亿"%x for x in range(0,45,5)])
plt.grid()
plt.show()

x = list(movies.keys())
y = list(movies.values())
plt.figure(figsize=(10,10))
plt.barh(x,y)
plt.xticks(range(0,45,5),["%d亿"%x for x in range(0,45,5)])
plt.grid()
plt.show()

menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
groupNames = ('G1','G2','G3','G4','G5')
xs = np.arange(len(menMeans))
plt.bar(xs,menMeans,facecolor='#9999ff',edgecolor='w')
plt.bar(xs,womenMeans,bottom=menMeans,facecolor='#ff9999')
plt.xticks(xs,groupNames)
plt.show()