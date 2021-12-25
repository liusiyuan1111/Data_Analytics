#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Matplotlib
File Name: 03散点图.py
Author: lsy
Create Date: 2021-12-7
-------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# 0 读取数据
athletes = pd.read_csv('res/new_athlete.csv').dropna()

# 1 筛选数据
male_athletes = athletes[athletes['Sex'] == 'M']
female_athletes = athletes[athletes['Sex'] == 'F']
# 计算男生和女生的平均身高和平均体重
male_mean_height = male_athletes['Height'].mean()
female_mean_height = female_athletes['Height'].mean()
male_mean_weight = male_athletes['Weight'].mean()
female_mean_weight = female_athletes['Weight'].mean()

# 2 画图
plt.figure(figsize=(10,5))
# 散点图
plt.scatter(male_athletes['Height'],male_athletes['Weight'],color='g',label='男性',alpha=0.5,s=male_athletes['Age'],marker='^')
plt.scatter(female_athletes['Height'],female_athletes['Weight'],color='r',alpha=0.5,label='女性',s=female_athletes['Age'])

# 刻度
plt.xticks(np.arange(140,220,5))
plt.yticks(np.arange(0,180,10))
# 图例
plt.legend(loc='best',ncol=2)
# 坐标轴
plt.xlabel("身高(cm)")
plt.ylabel("体重(kg)")
#标题
plt.title("运动员身高和体重散点图")
# 辅助线
plt.axvline(male_mean_height,color="g",linewidth=1)
plt.axhline(male_mean_weight,color="g",linewidth=1)
plt.axvline(female_mean_height,color="r",linewidth=1)
plt.axhline(female_mean_weight,color="r",linewidth=1)

plt.grid()
plt.show()

