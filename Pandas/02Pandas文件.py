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

data = pd.read_csv('res/GDP-China.csv',header=None,prefix="c+")

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
pd.read_json(json,orient='column')
df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index=['row 1', 'row 2'],
                  columns=['col 1', 'col 2'])
# 输出 json 字符串
df.to_json(orient='split')

#html
url = 'https://www.runoob.com/css/css-margin.html'
dfs = pd.read_html(url)
dfs[0] # 查看第一个 df

# 读取网页文件，第一行为表头
dfs = pd.read_html('data.html', header=0,attrs={'class':'df1'})
# 第一列为索引
dfs = pd.read_html(url, index_col=0)
header = '''
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
'''
footer = '''
    </body>
</html>
'''
with open("data.html",'w') as f:
    f.write(header)
    f.write(df.to_html(classes='df',bold_rows=False))
    f.write(df1.to_html(classes='df1'))
    f.write(footer)

#剪贴板
cdf = pd.read_clipboard()

df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': ['p', 'q', 'r']},
                  index=['x', 'y', 'z'])
df.to_clipboard()


#xml
xml = """<?xml version='1.0' encoding='utf-8'?>
<data>
 <row>
    <shape>square</shape>
    <degrees>360</degrees>
    <sides>4.0</sides>
 </row>
 <row>
    <shape>circle</shape>
    <degrees>360</degrees>
    <sides/>
 </row>
 <row>
    <shape>triangle</shape>
    <degrees>180</degrees>
    <sides>3.0</sides>
 </row>
 </data>"""

df = pd.read_xml(xml)

pd.read_xml("https://www.w3school.com.cn/example/xdom/books.xml",attrs_only=True)


df.to_xml() # 输出 xml 字符
# 指定根节点和各行的标签名称
df.to_xml(root_name="geometry", row_name="objects")
# 编写以属性为中心(attribute-centric)的XML
df.to_xml(attr_cols=df.columns.tolist())
# <row index="0" name="Liver" team="E" Q1="89" Q2="21" Q3="24" Q4="64"/>
# 编写元素和属性的组合
df.to_xml(
        index=False,
        attr_cols=['shape'],
        elem_cols=['degrees', 'sides'])



df.to_markdown(index=False)
with open("df.md",'w') as f:
    f.write(df.to_markdown(index=False))