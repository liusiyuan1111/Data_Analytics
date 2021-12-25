#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Matplotlib
File Name: 作业.py
Author: lsy
Create Date: 2021-12-7
-------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 作业一
highest = [26,21,26,26,22,20,17,19,22,28,30,28,24,28,25,26,25,26,25,23,24,30,32,31,30,27,26,27,29,25,25]
lowest =  [17,13,17,18,18,17,14,15,16,18,19,20,18,18,20,20,20,20,20,16,17,19,21,24,24,23,20,18,19,18,19]
plt.figure(figsize=(15,5))

# 绘制最高温度折线
plt.plot(highest,color='r',marker='o')
# 绘制最低温度折线
plt.plot(lowest,color='b',marker='o')
# 设置x轴的坐标和标题
plt.xticks(range(31),range(1,32))
plt.xlabel("日期（天)")
# 设置y轴的坐标和文本
plt.yticks(range(10,40,5),range(10,40,5))
plt.ylabel("温度（℃）")
# 设置标题
plt.title("长沙5月份气温走势")
# 添加最高温度注释文字
for x in range(0,31):
    temp = highest[x]
    plt.annotate(temp,xy=(x,temp),xytext=(x-0.2,temp+0.5))
# 添加最低温度注释文字
for x in range(0,31):
    temp = lowest[x]
    plt.annotate(temp,xy=(x,temp),xytext=(x-0.2,temp+0.5))
# 绘制网格
plt.grid()
plt.show()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime



guazi_bj = pd.read_csv("res/guazi_bj.csv")
now = datetime.now()
buy_time = pd.to_datetime(guazi_bj['buy_time'])

year = (now-buy_time)/np.timedelta64(1,'Y')



