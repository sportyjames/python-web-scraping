#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:02:46 2020

@author: sportyjames
"""

# 导入urlopen函数
from urllib.request import urlopen
# 导入BeautifulSoup
from bs4 import BeautifulSoup as bf
# 导入urlretrieve函数，用于下载图片
from urllib.request import urlretrieve

# 请求获取HTML
html = urlopen("https://www.google.com/")
# 用BeautifulSoup解析html
obj = bf(html.read(),'html.parser')
# 从标签head、title里提取标题
title = obj.head.title
# 打印标题
print(title)
# 使用find_all函数获取所有图片的信息
pic_info = obj.find_all('img',alt="Google")
# 提取logo图片的链接
logo_url = "https://www.google.com"+pic_info[0]['src']
# 打印链接
print(logo_url)
# 使用urlretrieve下载图片
urlretrieve(logo_url, 'logo2.png')




# # 分别打印每个图片的信息
# for i in pic_info:
#     print(i)