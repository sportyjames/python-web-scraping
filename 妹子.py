#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:39:02 2020

@author: sportyjames
"""

import requests
from bs4 import BeautifulSoup as bf

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

picURL = "https://www.mzitu.com/137617" #picture url

html = requests.get(picURL, headers=header)  # get web data by using response


soup = bf(html.text, 'html.parser') #interpret html

# all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')

# for a in all_a:
#     title = a.get_text()
#     print(title)


pic_max = soup.find_all('span')[9].text #最大页数在span标签中的第9个


title = soup.find('h2',class_='main-title').text #找标题

#输出每个图片页面的地址
for i in range(1,int(pic_max) + 1):
    href = picURL+'/'+str(i)
    html = requests.get(href, headers=header)
    mess = bf(html.text,"html.parser")


    #图片地址在img标签alt属性和标题一样的地方
    pic_url = mess.find('img',alt = title)

    html = requests.get(pic_url['src'],headers = header)

    #获取图片的名字方便命名
    file_name = pic_url['src'].split(r'/')[-1]

    #图片不是文本文件，以二进制格式写入，所以是html.content
    f = open(file_name,'wb')
    f.write(html.content)
    f.close()
