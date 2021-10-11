#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Numpy
File Name: 04数组操作.py
Author: lsy
Create Date: 2021-10-11
-------------------------------------------------
"""
import numpy as np

# 一、数组与数的计算
a1 = np.random.random((3,4))
print(a1)
# 如果想要在a1数组上所有元素都乘以10，那么可以通过以下来实现
a2 = a1*10
print(a2)
# 也可以使用round让所有的元素只保留2位小数
a3 = a2.round(2)

# 二、数组与数组的计算
# 1.结构相同的数组
a1 = np.random.randint(0,24,size=(3,8))
a2 = np.random.randint(1,10,size=(3,8))
print(a1+a2)  #相减、乘、除也都可以

# 2.行相同，只有一列的数组
a1 = np.random.randint(0,24,size=(3,8))
a2 = np.random.randint(1,10,size=(3,1))
print(a1+a2)

# 3.列相同，只有一行的数组
a1 = np.random.randint(0,24,size=(3,8))
a2 = np.random.randint(1,10,size=(1,8))
print(a1+a2)

# 三、数组的形状
# 1.reshape:将数组转换成指定形状，原数组不会发生改变(行和列的乘积要相等）
a1 = np.random.randint(0,24,size=(3,8))
a2 = a1.reshape(4,6)

# 2.resize:将数组转换成指定形状，直接修改原数组本身，不会返回任何值
a1 = np.random.randint(0,24,size=(3,8))
a1.resize(4,6)

# 3.flatten:将多维数组转换成一维数组，然后将这个拷贝返回，后续对返回值进行操作不会影响原数组
a1 = np.array([[1,2],[3,4]])
a1.flatten()[1] = 100

# 4.ravel:将多维数组转换成一维数组后，将这个引用返回，后续对这个返回值进行操作会改变原数组
a1.ravel()[1] = 100

# 四、数组的组合
# 1.vstack:将数组垂直叠加，数组的列数必须相同
v1 = np.random.randint(0,24,size=(3,8))
v2 = np.random.randint(0,24,size=(1,8))
v3 = np.vstack([v1,v2])

# 2.hstack:将数组水平叠加，数组的行数必须相同
h1 = np.random.randint(0,24,size=(3,8))
h2 = np.random.randint(0,24,size=(3,1))
h3 = np.hstack([h1,h2])

# 3.concatenate([],axis):将两个数组按照指定方式叠加，axis=0垂直叠加，=1水平叠加，=None转换成一维数组叠加
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
c = np.concatenate([a,b],axis=0)

c = np.concatenate([a,b.T],axis=1)

c = np.concatenate([a,b.T],axis=None)

# 五、数组的切割
# 1.hsplit:水平方向切割
a1 = np.random.randint(0,24,size=(4,4))
np.hsplit(a1,2)  #把a1水平分隔成两部分
np.hsplit(a1,[1,2])  #下标为1的地方切一刀，下标为2的地方切一刀，分成三部分

# 2.vsplit:垂直方向切割
np.vsplit(a1,2) #把a1垂直分隔成两部分
np.vsplit(a1,[1,2]) #按照行进行分隔，在下标为1和下标为2的地方分隔成三部分

# 3.split(数组，分割份数，行/列）:指定切割方式，axis=0代表按照行，=1代表按照行
np.split(a1,2,axis=0)
np.split(a1,2,axis=1)
np.split(a1,[1,2],axis=0)
np.split(a1,[1,2],axis=1)

# 六、数组转置和轴对换

a1 = np.random.randint(0,24,size=(2,4))
a2 = a1.T  #T属性
a3 = a1.transpose()  #转置函数

# 求内积
a1 = np.random.randint(0,24,size=(2,4))
a2 = a1.T
a1.dot(a2)

# 七、深拷贝和浅拷贝
# 1.不拷贝
a = np.arange(12)
b = a
print(b is a) #返回true，说明a和b是相同的

# 2.浅拷贝(指向同一块内存空间，会改变原值，相当于C语言引用型参数）
c = a.view()
print(c is a) #返回false,说明a和c是两个不同的变量
c[0] = 100
print(a[0])  #打印100,说明对c的改变会影响原数组，他们指向同一个内存空间

# 3.深拷贝（重新开辟一块空间，不会改变原值）
d = a.copy()
print(d is a)  #返回false,说明a和d是两个不同的变量
d[1] = 200
print(a[1])  #打印1，说明d的改变不会影响原数组，他们是两个不同的变量，指向不同的空间

# 之前学习的flatten就是深拷贝，ravel就是浅拷贝
