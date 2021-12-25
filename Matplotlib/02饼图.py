#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Data_Analytics
File Name: 02饼图.py
Author: lsy
Create Date: 2021-12-7
-------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

oses = {
'windows7':60.86,
'windows10': 18.46,
'windows8': 3.61,
'windows xp': 10.3,
'mac os': 6.78,
'其他': 1.12
}
names = oses.keys()
percents = oses.values()
plt.pie(percents,labels=names,autopct="%.2f%%",explode=(0,0.05,0,0,0,0))
plt.show()


avenger = [17974.4,50918.4,30033.0,40329.1,52330.2,19833.3,11902.0,24322.6,47521.8,32262.0,22841.9,12938.7,4835.1,3118.1,2570.9,2267.9,1902.8,2548.9,5046.6,3600.8]
plt.figure(figsize=(20,10))
plt.plot(avenger,marker="o")
plt.xticks(range(20),["第%d天"%x for x in range(1,21)])
plt.xlabel("天数")
plt.ylabel("票房数(万)")

for x in range(20):
    y = avenger[x]
    plt.annotate(y, xy=(x,y), xytext=(x-0.5, y + 1000))
plt.grid()
plt.savefig("./abc.png")
plt.show()