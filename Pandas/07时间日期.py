#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Pandas
File Name: 07时间日期.py
Author: lsy
Create Date: 2021-11-23
-------------------------------------------------
"""
import pandas as pd
import matplotlib.pyplot as plt

# 0.读取数据
fpath = "res/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
df.head()

# 1.转换日期格式
pd.to_datetime(df["ymd"])
df.set_index(pd.to_datetime(df["ymd"]), inplace=True)
df.head()
df.index[0]

# 2.查询
# 筛选固定的某一天
df.loc['2018-01-05']
# 日期区间
df.loc['2018-01-05':'2018-01-10']
# 按月份前缀筛选
df.loc['2018-03']
# 按月份前缀筛选
df.loc["2018-07":"2018-09"]
# 按年份前缀筛选
df.loc["2018"]

# 3.获取周、月、季度
# 周数字列表
df.index.week
# 月数字列表
df.index.month
# 季度数字列表
df.index.quarter

# 4.按照周、月、季度统计
# 统计每周的数据
df.groupby(df.index.week)["bWendu"].max()
# 统计每个月的数据
df.groupby(df.index.month)["bWendu"].max()
# 统计每个季度的数据
df.groupby(df.index.quarter)["bWendu"].max()

# 二、数据缺失
df = pd.DataFrame({
    "pdate": ["2019-12-01", "2019-12-02", "2019-12-04", "2019-12-05"],
    "pv": [100, 200, 400, 500],
    "uv": [10, 20, 40, 50],
})


df  # 缺失了2019-12-03的数据
df.set_index("pdate").plot()
plt.show()

# 方法1：reindex
df_date = df.set_index("pdate")
df_date
df_date.index
# 1.将df的索引设置为日期索引
df_date = df_date.set_index(pd.to_datetime(df_date.index))
df_date
df_date.index
# 2.使用pandas.reindex填充缺失的索引
# 生成完整的日期序列
pdates = pd.date_range(start="2019-12-01", end="2019-12-05")
pdates
# 填充0
df_date_new = df_date.reindex(pdates, fill_value=0)
df_date_new
df_date_new.plot() # 画图
plt.show()

# 方法2：resample
# 1.先将索引变成日期索引
df_new2 = df.set_index(pd.to_datetime(df["pdate"])).drop("pdate", axis=1)
df_new2
df_new2.index
# 2.使用resample的方法按照天重采样
# 由于采样会让区间变成一个值，所以需要指定mean等采样值的设定方法
df_new2 = df_new2.resample("D").mean().fillna(0)
df_new2
# resample的使用方式
df_new2.resample("2D").mean()