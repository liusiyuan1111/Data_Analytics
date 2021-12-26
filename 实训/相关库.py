#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: 实训
File Name: 相关库.py
Author: lsy
Create Date: 2021-12-26
-------------------------------------------------
"""
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

str = "我来自广东工贸职业技术学院"
seg_list = jieba.cut(str, cut_all=False)
print(seg_list)
print("/".join(seg_list))

txt = "中国，是以华夏文明为源泉、中华文化为基础，并以汉族为主体民族的多民族国家，通用汉语、汉字，汉族与少数民族被统称为“中华民族”，又自称为炎黄子孙、龙的传人。中国是世界四大文明古国之一，有着悠久的历史，距今约5000年前，\
以中原地区为中心开始出现聚落组织进而形成国家，后历经多次民族交融和朝代更迭，直至形成多民族国家的大一统局面。\
20世纪初辛亥革命后，君主政体退出历史舞台，共和政体建立。1949年中华人民共和国成立后，在中国大陆建立了人民代表大会制度的政体。"
seg_list = jieba.cut(txt, cut_all=False)
seg_txt = "/".join(seg_list)
mask_path = plt.imread("res/d.jfif")
wc = WordCloud(
    width=1000,     #宽度为1000
    height=800,     #高度为800
    background_color='white',       #背景颜色白色
    font_path="C:\Windows\Fonts\simkai.ttf",     #中文字体路径，一般在这个文件夹，可以自定义
    mask=mask_path
).generate(seg_txt)
wc.to_file('wc.png')    #保存图片
plt.imshow(wc)      #接收图片
plt.axis("off")     #去除坐标轴
plt.show()      #显示图片