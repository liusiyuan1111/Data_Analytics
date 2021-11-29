#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Pandas
File Name: 案例2：股票数据的处理.py
Author: lsy
Create Date: 2021-11-23
-------------------------------------------------
"""
import pandas as pd

df = pd.read_csv('res/00700.HK.csv',index_col=0)