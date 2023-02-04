import time
import requests
import re
import webbrowser
import os
import subprocess
import sys
import shutil
#name=''#coser分类模式
tag=''#tag模式
#tags1=""#搜索模式
startpages=1#开始的页数
pages=1#搜索的页数
sleeptime=10#等待时间，看文件大小设置
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76"}
totaldown=0
totalpages=0
os.system("cls")
for p in range(pages):
    url = 'https://coservip.com/tag/'+tag+'/page/'+str(p+startpages)#tag模式
    #url = 'https://coservip.com/'+str(p+startpages)+'?s='+name+'&type=post'#coser分类
    #url = 'https://coservip.com/cosplay/page/'+str(p+startpages)+'?tags1='+tags1#搜索模式
    data = requests.get(url=url, headers=headers).text#读取搜索页
    m = re.compile(r"https://coservip.com/([0-9]+).html")#查找当前页所有详情页的id
    match = m.findall(data)
    if match:
        match = list(set(match))#去重，爬到的url会重复两次
        print('第'+str(p+startpages)+'页，本页共找到'+str(len(match))+'个')
        totalpages+=len(match)
        for i in range(len(match)):
            if len(match)-i<20:
                sleeptime=5
            time.sleep(sleeptime)#小于10秒的间隔，容易被BAN IP
            url = 'https://coservip.com/'+match[i]+'.html'#拼接详情页的url
            data = requests.get(url=url, headers=headers).text#读取详情页
            m = re.search(r'\[素材名称\]：(.*)\[素材数量\]',data, re.M | re.I)#查找详情页的名称
            if m:
                print(m.group(1))
            m = re.search(r'https://url22.ctfile.com/f/(.*)\" ',data, re.M | re.I)#查找详情页城通网盘的链接，默认密码2233
            if m:#如果找到
                print('https://url22.ctfile.com/f/'+m.group(1))#输出网盘链接
                webbrowser.open('https://url22.ctfile.com/f/'+m.group(1))#打开城通网盘
                totaldown+=1
            else:#否则
                print(url)#输出详情页链接
                webbrowser.open(url)#打开详情页
    else:
        print('None')
print('共'+str(totalpages)+'条，共下载'+str(totaldown)+'个')