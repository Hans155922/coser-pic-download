import time
import requests
import re
import webbrowser
name='桜桃喵'
startpages=1#开始的页数
pages=4#搜索的页数
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76"}
url = 'https://coservip.com/page/?s='+name+'&type=post'
for p in range(pages):
    url = 'https://coservip.com/page/'+str(p+startpages)+'?s='+name+'&type=post'#拼接搜索页的url
    data = requests.get(url=url, headers=headers).text#读取搜索页
    m = re.compile(r"https://coservip.com/([0-9]+).html")#查找当前页所有详情页的id
    match = m.findall(data)
    if match:
        match = list(set(match))#去重，爬到的url会重复两次
        print('第'+str(p+startpages)+'页，本页共找到'+str(len(match))+'个')
        for i in range(len(match)):
            time.sleep(10)#小于10秒的间隔，容易被BAN IP
            url = 'https://coservip.com/'+match[i]+'.html'#拼接详情页的url
            data = requests.get(url=url, headers=headers).text#读取详情页
            m = re.search(r'https://url22.ctfile.com/f/(.*)2233',data, re.M | re.I)#查找详情页城通网盘的链接，默认密码2233
            if m:#如果找到
                print(m.group())#输出网盘链接
                webbrowser.open(m.group())#打开城通网盘
            else:#否则
                print(url)#输出详情页链接
                webbrowser.open(url)#打开详情页
    else:
        print('None')