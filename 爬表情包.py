#!/usr/bin/env python3
# - - coding: utf-8 - -
"""
Created on Sat May  9 18:59:41 2020

@author: sportyjames
"""
import requests
import os
import urllib.parse
from bs4 import BeautifulSoup
   
print('-------  欢迎下载表情包  --------\n表情包会下载到当前文件所在位置')
print('请在下方输入你要下载的表情包关键字然后点击回车，直接关闭或者Ctrl+c可以终止程序----')
   
# 函数：判断表情包是不是0个
def is_zero(url):
      test = requests.get(url)
      msg = test.content
      s = BeautifulSoup(msg, 'html.parser')
      menu = s.find_all(attrs={'class': 'item active'})
      tip = menu[0].text.strip()
      return tip
   
   
# 函数：判断是否存在关键词文件夹，没有就创建
def make_dir(key):
      if not os.path.exists(key):
          os.mkdir(key)
   
   
# 函数：爬虫下载图片
def down_img(url, key):
      # 拿到所有页码的表情
      page = 1
      # 定义变量，作为图片名称
      count = 1
      # 定义列表存放图片地址
      img_list = []
      # 定义标志表示程序是否运行
      flag = True
      while True:
          url += '/type/bq/page/%d.html' % page
          page += 1
          # 爬虫网页,获取网页html标签
          response = requests.get(url)
          content = response.content
   
          # 通过网页内容找到图片地址列表
          soup = BeautifulSoup(content, 'html.parser')
          result = soup.findAll(attrs={'class': 'ui image bqppsearch lazy'})
   
          # 循环遍历图片列表
          for i in result:
              # 拿到图片地址与盛放path的列表进行比对，如果存在就终止程序
              path = i['data-original']
              if path not in img_list:
                  img_list.append(path)
                  # 判断文件名是不是http://开头，没有就加上https://fabiaoqing.com
                  if path.startswith('http'):
                      img_msg = requests.get(path)
                  else:
                      img_msg = requests.get('https://fabiaoqing.com' + path)
                  # 写入文件
                  with open(key + '/' + str(count) + '.gif', 'wb') as fw:
                      fw.write(img_msg.content)
                      print('第' + str(count) + '张:' + path, '下载成功')
                      count += 1
              else:
                  flag = False
          if not flag:
              print('下载完成')
              break
   
   
# 主函数
def main():
      # 获取下载地址
      key = input('----->请输入：')
      keyword = urllib.parse.quote(key)
      url = "https://fabiaoqing.com/search/search/keyword/" + keyword
      if is_zero(url) == '表情（0）':
          # 判断如果表情是0，就返回一句话
          print('哦 no 我们没有%s的表情包' % key)
      else:
          # 调用函数创建文件夹
          make_dir(key)
          # 如果表情不是0个，就开始爬虫下载
          down_img(url, key)
   
   
   
if __name__ == '__main__':
      main()
      input('按回车键退出----')
  
  


