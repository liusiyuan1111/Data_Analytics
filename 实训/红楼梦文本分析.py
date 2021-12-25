#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: 实训
File Name: 红楼梦文本分析.py
Author: lsy
Create Date: 2021-12-25
-------------------------------------------------
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jieba
import wordcloud


plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']



# 注意编码


#0.读取数据
honglou_path = 'res/red_UTF82.txt'
stop_word_path = 'res/baidu_stopwords.txt'

#读取文本和停用词
honglou = pd.read_csv(honglou_path, header=None)
stop_word = pd.read_csv(stop_word_path, header=None)

print(honglou)

#1.数据预处理
#检测是否有空行
np.sum(pd.isnull(honglou))

#删除卷
index_juan = honglou[0].str.contains("^第+.+卷")
honglou.drop(index=(honglou.loc[index_juan]),axis=0,inplace=True)

#提取每章标题
index_hui = honglou[0].str.match("^第+.+回")
hui_name = honglou[index_hui].reset_index(drop=True)
print(hui_name)
#处理章节名
hui_split = hui_name[0].str.split(" ").reset_index(drop=True)
honglou_df = pd.DataFrame(list(hui_split),columns=["Chapter","LeftName","RightName"])

honglou_df["No."] = np.arange(1,121)

#每章开始
honglou_df["Start"] = index_hui[index_hui==True].index
#每章结束
honglou_df["End"] = honglou_df["Start"][1:len(honglou_df["Start"])].reset_index(drop=True)-1
honglou_df["End"][119] = len(honglou[0])
honglou_df["Length"] = honglou_df["End"]-honglou_df["Start"]
honglou_df["Content"] = "Content"

#将每段内容连接起来
for i in range(120):
    fanwei = np.arange(honglou_df["Start"][i]+1, int(honglou_df["End"][i]))
    honglou_df["Content"][i]= "".join(honglou[0][fanwei]).replace("\u3000","")

# 计算每章有多少字
honglou_df["Words"] = honglou_df["Content"].apply(len)

# 画图
# 散点图
plt.figure(figsize=(12,10))
plt.scatter(honglou_df["Length"],honglou_df["Words"])
for i in range(120):
    plt.text(honglou_df["Length"][i]+1-2, honglou_df["Words"][i]+100,honglou_df["No."][i])
plt.xlabel("章节段数")
plt.ylabel("章节字数")
plt.title("《红楼梦》章节段数与字数散点图")
plt.show()

# 趋势图
plt.figure(figsize=(12,10))
plt.subplot(2,1,1)
plt.plot(honglou_df["No."],honglou_df["Length"],"ro-",label="段落")
plt.xlabel("章节")
plt.ylabel("章节段数")
plt.title("《红楼梦》120回")
plt.hlines(np.mean(honglou_df["Length"]),0,125,"b")
plt.xlim((0,125))
plt.subplot(2,1,2)
plt.plot(honglou_df["No."],honglou_df["Words"],"yo-",label="字数")
plt.xlabel("章节")
plt.ylabel("章节字数")
plt.hlines(np.mean(honglou_df["Words"]),0,125,"k")
plt.xlim((0,125))
plt.show()


# 2.分词
row,col = honglou_df.shape
# 预定义列表
honglou_df["Cutword"] = "Cutword"
for i in np.arange(row):
    #分词
    cutwords = list(jieba.cut(honglou_df["Content"][i], cut_all=True))
    #去除长度为1的词
    cutwords = pd.Series(cutwords)[pd.Series(cutwords).apply(len)>1]
    #去除停用词
    cutwords = cutwords[~cutwords.isin(stop_word)]
    honglou_df["Cutword"][i] = cutwords.values
print(honglou_df["Cutword"])

# 统计词频