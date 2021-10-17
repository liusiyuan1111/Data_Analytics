#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Numpy
File Name: 05文件操作.py
Author: lsy
Create Date: 2021-10-17
-------------------------------------------------
"""

import numpy as np

#csv文件保存
a = np.arange(100).reshape(10,10)
np.savetxt("b.csv",a,fmt="%d",delimiter=",",header="data")

#csv文件读取
b = np.loadtxt("a.csv",dtype=np.int32,delimiter=",")
c = np.loadtxt("a.csv",dtype=np.int32,delimiter=",",skiprows=3,usecols=(2,3,4),unpack=True)

#npy和npz文件的保存和读取
np.save("c",a)
d = np.load("c.npy")

import csv

#csv文件操作
#读取
with open("stock.csv","r") as fp:
    reader = csv.reader(fp)
    print(reader)
    for x in reader:
        print(x)
#通过标题读取
with open("stock.csv","r") as fp:
    reader = csv.DictReader(fp)
    for x in reader:
        print(x["secShortName"])

#写入数据
headers = ['name','age','classroom']
values = [['liu',27,'4'],['si',25,'3'],['yuan',26,'4']]
with open('test.csv','w',newline='') as fp:
    w = csv.writer(fp)
    w.writerow(headers)
    w.writerows(values)

#通过字典写入
headers = ['name','age','classroom']
values = [{'name':'si','age':20,'classroom':'4'},
          {'name':'yuan','age':20,'classroom':'4'}]
with open('test2.csv','w',newline='') as fp:
    w = csv.DictWriter(fp,headers)
    w.writerow({'name':'liu','age':20,'classroom':'4'})
    w.writerows(values)
