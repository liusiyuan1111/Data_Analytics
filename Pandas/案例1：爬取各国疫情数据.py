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
import pandas as pd
import requests

s = requests.Session()
#访问数据
covid = s.get('https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=provinceCompare')
#数据文本
data = covid.text
#读取解析JSON
pd.read_json(data)

data = [(['name']) for i in pd.read_json(data).data]
