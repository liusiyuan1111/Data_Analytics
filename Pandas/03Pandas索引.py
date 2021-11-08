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


