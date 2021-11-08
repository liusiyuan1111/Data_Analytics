#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Pandas
File Name: 03Pandas索引.py
Author: lsy
Create Date: 2021-11-9
-------------------------------------------------
"""

import pandas as pd

#一、设置索引
data = 'res/team.xlsx'
df = pd.read_excel(data, index_col='name') # 设置索引为 name
df

#二、数据查询

#1.Series查询
s1 = pd.Series([1, 'a', 5.2, 7], index=['a','b','c','d'])
s1
s1['a']
type(s1['a'])
s1[['b','a']]
type(s1[['b','a']])

#2.DataFrame查询
data = 'res/team.xlsx'
df = pd.read_excel(data)
#查询一列，得到一个Series
df['Q1']
type(df['Q1'])
#查询多列，得到的是DataFrame
df[['Q1','Q2']]
type(df[['Q1','Q2']])
#查询一行，得到的是Series
df.loc[1]
#查询多行，得到的是DataFrame
df.loc[1:3]
type(df.loc[1:3])

#三、查询方法

# 0.读取数据
df = pd.read_csv('res/beijing_tianqi_2018.csv')
df.head()  #读取前几行，默认是前5行
# 设定索引为日期，方便按日期筛选
df.set_index('ymd', inplace=True)
df.index #后续会学习时间序列，先按字符串处理
df.head()

# 1.使用单个标签查询
df.loc['2018-01-03']

# 2.使用值列表查询
df.loc[['2018-01-03','2018-01-04','2018-01-05'],'bWendu'] #得到Series
df.loc[['2018-01-03','2018-01-04','2018-01-05'],['bWendu','yWendu']] #得到DataFrame

# 3.使用数值区间进行范围查询（注意：区间左右都包含）
# 行index按区间
df.loc['2018-01-03':'2018-01-08', 'bWendu']
# 列index按区间
df.loc['2018-01-03', 'bWendu':'fengxiang']
# 行和列都按区间查询
df.loc['2018-01-03':'2018-01-08', 'bWendu':'fengxiang']

# 4.使用布尔索引
# 简单条件查询，aqi<30
df.loc[df['aqi']<30]
# 查看以下这里的布尔条件
df['aqi']<30
# 复杂条件查询，最高气温小于30度，最低气温大于15度，晴天，空气质量等级一级
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
df.loc[(df["bWendu"]<=30) & (df["yWendu"]>=15) & (df["tianqi"]=='晴') & (df["aqiLevel"]==1)]

# 5.调用函数查询
# 直接写lambda表达式
df.loc[lambda df : (df["bWendu"]<=30) & (df["yWendu"]>=15)]
