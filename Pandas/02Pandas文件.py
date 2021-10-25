#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Data_Analytics
File Name: 02Pandas文件.py
Author: lsy
Create Date: 2021-10-25
-------------------------------------------------
"""
import pandas as pd
import numpy as np

pd.read_csv('res/GDP-China.csv')
pd.read_csv('https://www.gairuo.com/file/data/dataset/GDP-China.csv')

data = pd.read_csv('res/GDP-China.csv',parse_dates=True)

d = {'国家': ['中国', '美国', '日本'],
     '人口': [14.33, 3.29, 1.26]}
df = pd.DataFrame(d)
df.to_csv('done.csv')
df.to_csv('done.csv', index=False) # 不要索引

xlsx = pd.ExcelFile('res/team1.xlsx')
df = pd.read_excel(xlsx, 'Sheet1') # 读取
xlsx.parse('Sheet1') # 取指定标签为 DataFrame

df.to_excel('path_to_file.xlsx')
df.to_excel('path_to_file.xlsx', sheet_name='GDP', index=False)
df.to_excel('path_to_file.xlsx', index_label='label', merge_cells=False)

d1 = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df1 = pd.DataFrame(d1)

d2 = {'国家': ['中国', '美国', '日本'],
     '人口': [14.33, 3.29, 1.26]}
df2 = pd.DataFrame(d2)

with pd.ExcelWriter('path_to_file.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')




with pd.ExcelWriter('path_to_file.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')


pd.read_json('data.json')
json = '''{"columns":["col 1","col 2"],
"index":["row 1","row 2"],
"data":[["a","b"],["c","d"]]}
'''
pd.read_json(json)
pd.read_json(json, orient='split') # json 格式

cdf = pd.read_clipboard()

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': ['p', 'q', 'r']},
                  index=['x', 'y', 'z'])
df.to_clipboard()