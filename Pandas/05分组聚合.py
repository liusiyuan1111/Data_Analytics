#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Pandas
File Name: 05分组聚合.py
Author: lsy
Create Date: 2021-11-16
-------------------------------------------------
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 定义一个df
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
# 一、分组聚合
# 单个列聚合
df.groupby('A').sum()
# 多个列聚合
df.groupby(['A','B']).mean()
# 去除二级索引
df.groupby(['A','B'], as_index=False).mean()
# 同时查看多种数据统计
df.groupby('A').agg([np.sum, np.mean, np.std])
# 查看单列的结果数据统计
# 方法1：预过滤，性能更好
df.groupby('A')['C'].agg([np.sum, np.mean, np.std])
# 方法2
df.groupby('A').agg([np.sum, np.mean, np.std])['C']
# 不同列使用不同的聚合函数
df.groupby('A').agg({"C":np.sum, "D":np.mean})

# 二、遍历分组
# 1.遍历单个列聚合的分组
g = df.groupby('A')
g.get_group('bar')
# 2.遍历多个列聚合的分组
g = df.groupby(['A', 'B'])
for name,group in g:
    print(name)
    print(group)
g.get_group(('foo','two'))

# 三、实例：分组探索天气数据
fpath = "res/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
df.head()
df['month'] = df['ymd'].str[:7]
df.head()
data = df.groupby('month')['bWendu'].max()
data
type(data)
data.plot()  # 画图
plt.show()
# 3.查看每个月的最高温度、最低温度、平均空气质量指数
group_data = df.groupby('month').agg({"bWendu":np.max, "yWendu":np.min, "aqi":np.mean})
group_data
group_data.plot()
plt.show()

# 四、分组聚合不同列
df = pd.read_csv(
    "res/ratings.dat",
    sep="::",
    engine='python',
    names="UserID::MovieID::Rating::Timestamp".split("::")
)

# 每个MovieID的平均评分
result = df.groupby("MovieID")["Rating"].mean()
result.head()
type(result)
# 方法1：agg函数传入多个结果列名=函数名形式
result = df.groupby("MovieID")["Rating"].agg(
    mean=np.mean, max=np.max, min=np.min
)
result.head()

# 方法2：agg函数传入字典，key是column名，value是函数列表
# 每个MoiveID的最高评分、最低评分、平均评分
result = df.groupby("MovieID").agg(
    {"Rating":['mean', 'max', np.min]}
)
result.head()
# 去除二级索引
result.columns = ['age_mean', 'age_min', 'age_max']
result.head()

# 聚合后多列-多指标统计
# 方法1：agg函数传入字典，key是原列名，value是原列名和函数元组
result = df.groupby("MovieID").agg(
    rating_mean=("Rating", "mean"),
    rating_min=("Rating", "min"),
    rating_max=("Rating", "max"),
    user_count=("UserID", lambda x: x.nunique())
)
result.head()

# 方法2：agg函数传入字典，key是原列名，value是函数列表
result = df.groupby("MovieID").agg(
    {
        "Rating": ['mean', 'min', 'max'],
        "UserID": lambda x: x.nunique()
    }
)
result.head()  # 结果是二级索引
# 去除二级索引
result.columns = ["rating_mean", "rating_min", "rating_max", "user_count"]
result.head()


# 方法3：使用groupby之后apply对每个子df单独统计
def agg_func(x):
    """注意，这个x是子DF"""

    # 这个Series会变成一行，字典KEY是列名
    return pd.Series({
        "rating_mean": x["Rating"].mean(),
        "rating_min": x["Rating"].min(),
        "rating_max": x["Rating"].max(),
        "user_count": x["UserID"].nunique()
    })


result = df.groupby("MovieID").apply(agg_func)
result.head()