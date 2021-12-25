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

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = np.arange(10)
y = np.random.randint(0,10,size=(10,))
plt.plot(x,y)
plt.show()
plt.plot(x,y,"r:")
plt.show()
plt.plot(x,y,"rp")
plt.show()

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.plot(x, y, linewidth=10, color='red',alpha=0.2)
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.show()

plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
x = np.linspace(0,20,50)
y = np.sin(x)
plt.plot(x,y)
plt.show()

x = np.arange(0,20,2)
y = x*2
xticks = ["%d坐标"%i for i in x]
plt.xticks(x,xticks) #在x轴上的刻度是0坐标,2坐标...20坐标
plt.plot(x,y)
plt.show()

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
plt.figure(num=3, figsize=(8, 5),dpi=80,facecolor='y')
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.xlim((-1, 2))
plt.ylim((-2, 3))
new_ticks = np.linspace(-1, 2, 5)
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
plt.xticks(new_ticks)
plt.legend(labels=['y1','y2'],loc='best',ncol=2)
plt.show()

avenger = [17974.4,50918.4,30033.0,40329.1,52330.2,19833.3,11902.0,24322.6,47521.8,32262.0,22841.9,12938.7,4835.1,3118.1,2570.9,2267.9,1902.8,2548.9,5046.6,3600.8]
plt.figure(figsize=(15,5))
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

x = np.linspace(0,20)
y = np.sin(x)
plt.plot(x,y,marker="o",color='r',markerfacecolor='k',markersize=10)
plt.show()


x = np.linspace(0,20)
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.show()



x = np.arange(0.0, 5.0, 0.01)
y = np.cos(2*np.pi*x)
plt.plot(x, y,linewidth=2)
for x in range(6):
    y = np.cos(2 * np.pi * x)
    plt.annotate(y, xy=(x,y), xytext=(x-0.05, y+0.1))
plt.ylim(-2, 2)
plt.show()

values = np.arange(20)
plt.subplot(221)
plt.plot(values)
plt.plot(values**2)
plt.subplot(222)
plt.plot(np.sin(values),'r')
plt.subplot(223)
plt.plot(np.cos(values),'b')
plt.subplot(224)
plt.plot(np.tan(values),'y')
plt.style.use("dark_background")
plt.show()

plt.style.use("fivethirtyeight")
figure,axes = plt.subplots(2,2,sharex=True,sharey=True)
axes[0,0].plot(np.sin(np.arange(10)),c='r')
axes[0,1].plot(np.cos(np.arange(10)),c='b')
axes[1,0].plot(np.tan(np.arange(10)),c='y')
axes[1,1].plot(np.arange(10),c='g')
plt.show()

plt.style.available