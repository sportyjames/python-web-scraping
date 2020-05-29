#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:04:06 2020

@author: sportyjames
"""

import requests
from bs4 import BeautifulSoup as bf

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
          'Referer':'http://93.174.95.27',}

link = "https://music.163.com/discover/toplist?id=3778678" #playlist link

response = requests.get(link, headers=header)  # get web data by using response

html = response.content  # convert the data to html

soup = bf(html, 'html.parser') #interpret html


alist=soup.select("a")

Songs=[]
for music in alist:
    if music.has_attr("href"):
        if str(music.attrs["href"]).startswith("/song?id="):
            id=str(music.attrs["href"]).replace("/song?id=", "")
            try:
                Songs.append([
                     "http://music.163.com/song/media/outer/url?id=" + id + ".mp3",
                     music.text
                    ])
            except:
                pass

i = 1 #表示歌曲数目

j = 0 #表示歌曲location

for j in range(len(Songs)):
    # try:
    song_link = Songs[j][0]
    song_name = Songs[j][1]
    print("第 " + str(i) + " 首歌曲：" + song_link)
    print("正在下载......")

    response = requests.get(song_link, headers=header).content
    file = open(song_name + " .mp3",'wb')
    file.write(response)
    file.close()
    print("下载完成.\n\r")
    i=i+1
    # except:
    #     pass


# 

#