#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Data_Analytics
File Name: 01Panda基本.py
Author: lsy
Create Date: 2021-10-19
-------------------------------------------------
"""
import pandas as pd
import numpy as np

# 一、快速入门
# 1.创建DataFrame
df = pd.DataFrame(
    {'国家':['中国','美国','日本'],
     '地区':['亚洲','北美','亚洲'],
     '人口': [14.33, 3.29, 1.26],
     'GDP': [14.22, 21.34, 5.18],
     }
)
df2 = pd.DataFrame(
    {'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'
     }
)

# 2.生成Series
df['人口']  #从上述df中取出‘人口’这一列，并生成一个Series
gdp = pd.Series([14.22, 21.34, 5.18], name='gdp')  #创建一个名叫GDP的Series，并自动帮我们补上0-2的索引


# 3.对象的操作
df.describe()  #自动帮我们计算常用的数据统计方法
gdp.describe()  #Series对象也适用
df.max()   #求最大值
gdp.max()  #Series对象也适用

