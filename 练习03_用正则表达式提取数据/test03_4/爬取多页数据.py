"""
爬取一家公司的多页数据,爬取分页数据
爬取数据太快会触发网站的反爬机制，需要让程序休眠3秒、
"""
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def spyderSomething(page, kw):
    num = page * 10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + kw + '&medium=0&pn=' + str(num)
    response = requests.get(url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    titles = soup.select('.news-title_1YtI1 a')
    print("第"+str(page+1)+"页爬虫数据"+"关键词为:"+kw)
    for i in titles:
        print("标题为：" + i.text)

# 访问超市设置，timeout 参数的使用
# 只需要在request.get（）中增加一个参数timeout =10

if __name__ == '__main__':
    kws = ['哈登', '詹姆斯', '李宁', '浩鲸科技']
    for kw in kws:
        for i in range(10):
            spyderSomething(i, kw)
        time.sleep(3)
