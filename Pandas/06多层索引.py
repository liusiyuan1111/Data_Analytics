#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Pandas
File Name: 06多层索引.py
Author: lsy
Create Date: 2021-11-23
-------------------------------------------------
"""
import numpy as np
import pandas as pd


# 0.读取数据
stocks = pd.read_excel('res/互联网公司股票.xlsx')
stocks.shape
stocks['公司'].unique()
stocks.groupby('公司')["收盘"].mean() # 分组聚合

# 1.Series的多层索引
ser = stocks.groupby(['公司', '日期'])['收盘'].mean()
ser.reset_index()
ser.loc['BABA']
ser.loc[('BIDU', '2019-10-02')]
ser.loc[:, '2019-10-02']

# 2.DataFrame的多层索引
stocks.head()
stocks.set_index(['公司', '日期'], inplace=True)
stocks.index
stocks.sort_index(inplace=True) #排序
stocks.loc['BIDU']
stocks.loc[('BIDU', '2019-10-02'),:]
stocks.loc[('BIDU', '2019-10-02'),'开盘']
stocks.loc[['BIDU', 'JD']]
stocks.loc[(['BIDU', 'JD'],'2019-10-03'),:]
stocks.loc[(['BIDU', 'JD'], '2019-10-03'), '收盘']
stocks.loc[('BIDU', ['2019-10-02', '2019-10-03']), '收盘']
stocks.loc[(slice(None), ['2019-10-02', '2019-10-03']), :]