#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Data_Analytics
File Name: 案例1：爬取各国疫情数据.py
Author: lsy
Create Date: 2021-10-25
-------------------------------------------------
"""
import json

import pandas as pd
import requests


s = requests.Session()
#访问数据
covid = s.get('https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist')

#数据文本
data = covid.text
#读取解析JSON
pd.read_json(data)
#遍历索引
data = [(i['name'],i['confirm'],i['dead']) for i in pd.read_json(data).data]
#保存到dataframe中
df = pd.DataFrame(data,columns=['国家','确诊','死亡人数'])
#导出为csv文件
df.to_csv('covid.csv',encoding="utf_8_sig")
