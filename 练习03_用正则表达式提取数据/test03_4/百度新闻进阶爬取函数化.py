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

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def baidu(companies):
    for company in companies:
        t = time()
        url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&&word=' + company
        res = requests.get(url, headers=headers).text
        soup = BeautifulSoup(res, 'html.parser')
        try:
            if not os.path.exists('D:/爬虫/data'):
                os.makedirs("D:/爬虫/data")
            else:
                with open("D:/爬虫/data/" + company + str(int(t)) + ".txt", 'a+')as f:
                    titles = soup.select('.news-title_1YtI1 a')
                    f.write(company + "数据挖机完毕!+'\n'+'\n'")
                    for i in titles:
                        f.write("标题为：" + i.text + " 链接：" + i['href']+"\n")
        except Exception as e:
            print("Error: 没有找到文件或读取文件失败")
        finally:
            print("程序结束")


companys = [
    '华能信托',
    '阿里巴巴',
    '浩鲸科技',
    '腾讯科技',
    '京东',
]
baidu(companys)
