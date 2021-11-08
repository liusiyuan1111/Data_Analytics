#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Pandas
File Name: 04数据统计与处理.py
Author: lsy
Create Date: 2021-11-9
-------------------------------------------------
"""

import pandas as pd

df = pd.read_csv('res/beijing_tianqi_2018.csv')
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

# 一、汇总类统计
# 1.直接计算所有数字列统计结果
df.describe()
# 2.单个Series的数据
df["bWendu"].mean()
df["bWendu"].max()
df["bWendu"].min()

# 二、去重和按值计数
# 1.唯一性去重
df["fengxiang"].unique()
df["tianqi"].unique()
df["fengli"].unique()
# 2.按值计数
df["fengxiang"].value_counts()
df["tianqi"].value_counts()
df["fengli"].value_counts()

# 3.相关系数和协方差
df.cov() # 协方差矩阵
df.corr() # 相关系数矩阵
df["aqi"].corr(df["bWendu"]) #空气质量和最高温度的相关系数

# 二、新增数据列
# 1.直接赋值
df.loc[:, "wencha"] = df["bWendu"] - df["yWendu"]

# 2.apply方法
def get_wendu_type(x):
    if x["bWendu"] > 33:
        return '高温'
    if x["yWendu"] < -10:
        return '低温'
    return '常温'
# 注意需要设置axis==1，这是series的index是columns
df.loc[:, "wendu_type"] = df.apply(get_wendu_type, axis=1)
# 查看温度类型的计数
df["wendu_type"].value_counts()

# 3.assign方法
# 可以同时添加多个新的列
# 摄氏度转华氏度
df.assign(
    yWendu_huashi = lambda x : x["yWendu"] * 9 / 5 + 32,
    bWendu_huashi = lambda x : x["bWendu"] * 9 / 5 + 32
)

# 4.条件选择
# 先创建空列（这是第一种创建新列的方法）
df['wencha_type'] = ''

df.loc[df["bWendu"]-df["yWendu"]>10, "wencha_type"] = "温差大"

df.loc[df["bWendu"]-df["yWendu"]<=10, "wencha_type"] = "温差正常"

# 三、缺失值处理
# 1.读取数据
df = pd.read_excel('res/student_excel.xlsx',skiprows=2)
# 2.检测空值
df.isnull()
df['分数'].isnull()
df['分数'].notnull()
df.loc[df['分数'].notnull()] # 筛选没有空分数的所有行
# 3.删除全是空值的列
df.dropna(axis=1,how='all',inplace=True)
# 4.删除全是空值的行
df.dropna(axis=0,how='all',inplace=True)
# 6.将分数列为空的填充为0分
df.fillna({'分数':0},inplace=True)
# 等同于
df.loc[:,'分数'] = df['分数'].fillna(0)
# 7.填充姓名的缺失值
# 使用前面的有效值填充，用ffill：forward fill
df.loc[:, '姓名'] = df['姓名'].fillna(method="ffill")
# 8.将清洗好的数据保存
df.to_excel('res/student_excel_clean.xlsx',index=False)