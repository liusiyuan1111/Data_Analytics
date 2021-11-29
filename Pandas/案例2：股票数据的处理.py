#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Pandas
File Name: 案例2：股票数据的处理.py
Author: lsy
Create Date: 2021-11-23
-------------------------------------------------
"""
import pandas as pd
# 读取数据
df = pd.read_csv('res/00700.HK.csv')
# 数据统计
df.describe()
# 添加月份
df["Date"] = pd.to_datetime(df["Date"])
df["Date"].dt.month
df["月份"] = df["Date"].dt.month
#添加年份
df["年份"] = df["Date"].dt.year
# 计算每年平均收盘价
result = df.groupby("年份")["Close"].mean()
print(result)
# 收盘价最低的数据行
df.loc[df["Close"].argmin()]
# 筛选部分列
df[["Date","Open","Close"]]
# 设置日期为索引列
df.set_index("Date",inplace=True)
df.head()
# 删除high和low
df.drop(columns=["High","Low"],inplace=True)
# 重命名
df.rename(columns={"Open":"liu","Close":"si","Volume":"yuan"},inplace=True)