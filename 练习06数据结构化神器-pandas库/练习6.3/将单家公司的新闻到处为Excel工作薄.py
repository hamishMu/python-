"""
批量爬取多家公司的新闻，将爬取结果保存为文本文件。
变量名= open("文件路径"，"写入方式")
w 表示每次写入内容哦都会清楚，覆盖
a 表示不清楚原来的内容，再原有基础上写入新的内容
"""
import requests
from bs4 import BeautifulSoup
from time import time
import  os
import  pandas as pd


headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def baidu(companies):

    for company in companies:
        t = time()
        url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&&word=' + company
        res = requests.get(url, headers=headers).text
        soup = BeautifulSoup(res, 'html.parser')
        titles = soup.select('.news-title_1YtI1 a')
        for i in titles:
            df = pd.DataFrame()
            df['标题'] = i.text
            df['网址'] = i['href']
        return  df


companys = [
    '华能信托'
]
df_all = baidu(companys)
df_all.to_excel("test.xlsx",index=False)