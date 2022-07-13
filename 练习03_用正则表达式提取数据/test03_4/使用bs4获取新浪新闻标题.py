"""
https://news.sina.com.cn/china
"""
import requests
from bs4 import BeautifulSoup

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
url = ' https://news.sina.com.cn/china/'

res = requests.get(url, headers=headers)
res.encoding='utf-8'
data =res.text
# print(data)

soup = BeautifulSoup(data,"html.parser")
titles = soup.select(".left-content-1 a")
# print(titles)
title_href ={}
for i in titles:
    href = i['href']
    title = i.text
    title_href.update({i.text:i['href']})
print(len(title_href))
print(title_href)