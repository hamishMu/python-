"""
http://weixin.sogou.com/
"""
import re
import time
import  requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
}
url ='https://weixin.sogou.com/weixin?type=2&query=乌克兰'

res = requests.get(url,headers=headers,timeout=10).text
# print(res)

titles = re.findall('uigs="article_title_.*?">(.*?)</a>',res)
hrefs = re.findall('<div class="txt-box">.*?<h3>.*?<a target="_blank" href="(.*?)" ',res,re.S)
source = re.findall('uigs="article_account_.*?">(.*?)</a>',res)
date = re.findall('timeConvert\(\'(.*?)\'\)',res)

for i in range(len(titles)):
    titles[i]= re.sub('<.*?>','',titles[i])
    titles[i]= re.sub('&.*?;','',titles[i])
    timestamp = int(date[i])
    timeArray = time.localtime(timestamp)
    date[i] = time.strftime('%Y-%m-%d',timeArray)
    hrefs[i]=re.sub('amp;','',hrefs[i])
    hrefs[i]='https://weixin.sogou.com'+hrefs[i]
    print(str(i+1)+"."+titles[i]+'+'+source[i]+'+'+date[i])
    print(hrefs[i])

