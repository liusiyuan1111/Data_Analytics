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

# 4.查看类型
type(df2)
type(gdp)

# 二、Series
#1.创建
data = np.arange(3)
s = pd.Series(data,name='data',dtype=float,index=[1,2,3])

#2.数据
# 列表和元组
pd.Series(['a', 'b', 'c', 'd', 'e'])
pd.Series(('a', 'b', 'c', 'd', 'e'))

#ndarray
# 由索引为 a、b.. ， 五个随机浮点数数组组成
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s.index # 查看索引
s = pd.Series(np.random.randn(5)) # 未指定索引

# 字典
d = {'b': 1, 'a': 0, 'c': 2}
s = pd.Series(d)
pd.Series(d, index=['b', 'c', 'd', 'a'])

# 标量
pd.Series(5.)

# 指定索引
pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])

# 3.Series操作

# 类似ndarray的操作
s = pd.Series([1,2,3,4,5,6,7,8])
s[3] # 类似列表切片
s[2:]
s.median() # 平均值，包括其他的数学函数
s[s > s.median()] # 筛选大于平均值的内容
s[[1, 2, 1]] # 指定索引的内容，括号的列表是索引
s.dtype # 数据类型
s.array # 返回值的数列
s.to_numpy() # 转为 numpy 的 ndarray
3 in s # 逻辑运算，检测索引

# 类似字典的操作
s = pd.Series([14.22, 21.34, 5.18],
              index=['中国', '美国', '日本'],
              name='人口')

s['中国'] # 14.22 # 根 key 进行取值，如果没有报 KeyError
s['印度'] = 13.54 # 类似字典一样增加一个数据
'法国' in s # False 逻辑运算，检测索引

# 向量计算
s = pd.Series([1,2,3,4])
s + s # 同索引相加，无索引位用 NaN 补齐
s * s # 同索引相乘
s[1:] + s[:-1] # 选取部分进行计算
np.exp(s) # 求e的幂次方

# 名称属性
s = pd.Series([1,2,3,4], name='数字')
s.name # '数字'
s = s.rename("number") # 修改名称
s2 = s.rename("number") # 修改名称并赋值给一个新变量

# 其他方法
s = pd.Series([1,2,3,4], name='数字')
s.add(1) # 每个元素加1
s.add_prefix(3) # 给索引前加个3，升位
s.add_suffix(4) # 同上，在后增加
s.sum() # 总和
s.count() # 数量，长度
s.agg('std') # 聚合，仅返回标准差, 与 s.std() 相同
s.agg(['min', 'max']) # 聚合，返回最大最小值
s.any() # 是否有为假的
s.all() # 是否全是真
s2 = pd.Series([5,6,7])
s.append(s2) # 追加另外一个 Series
s.apply(lambda x:x+1) # 应用方法,lambda冒号前面是传入的数据，后面是要进行的运算
s.empty # 是否为空
s3 = s.copy() # 深拷贝


# 三、DataFrame
# 1.数据
# 字典
d = {'国家': ['中国', '美国', '日本'],
     '人口': [14.33, 3.29, 1.26]}
df = pd.DataFrame(d)
df = pd.DataFrame(d, index=['a', 'b', 'c'])

# Series
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)

# ndarray或列表
d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}

pd.DataFrame(d)

# 同构的数组
data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
pd.DataFrame(data)

# 字典和列表
# 定义一个字典列表
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

# 生成 DataFrame 对象
pd.DataFrame(data2)

# Series
s1 = pd.Series(['a', 'b', 'c', 'd', 'e'])
pd.DataFrame(s1)

# 四、特有的数据类型
d = pd.DatetimeTZDtype("ns", tz='Asia/Shanghai')
pd.Series(['20200501 22:23:22.3432'], dtype=d)
pd.Series(['20200501 22:23:22.3432'], dtype='datetime64[ns, Asia/Shanghai]')
pd.Series(['20200501 22:23:22.3432'], dtype='datetime64[ns]') # 无时区

# 用字符形式
pd.Timestamp('2017-01-01T12')
# Timestamp('2017-01-01 12:00:00')

# Unix epoch 指定时间单和时区
pd.Timestamp(1513393355.5, unit='s')
# Timestamp('2017-12-16 03:02:35.500000')
pd.Timestamp(1513393355, unit='s', tz='US/Pacific')
# Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')

# 用 datetime.datetime 的方法
pd.Timestamp(2017, 1, 1, 12)
# Timestamp('2017-01-01 12:00:00')
pd.Timestamp(year=2017, month=1, day=1, hour=10)
# Timestamp('2017-01-01 12:00:00')

t = pd.CategoricalDtype(categories=['b', 'a'], ordered=True)
pd.Series(['a', 'b', 'a', 'c'], dtype=t) # 'c' 不在列表是值会为 NaN

pd.Categorical([1, 2, 3, 1, 2, 3])

pd.PeriodDtype(freq='D') # 按天
# period[D]
pd.PeriodDtype(freq=pd.offsets.MonthEnd()) # 按月，最后

pd.Series(['a','b','c'], dtype=pd.StringDtype())

