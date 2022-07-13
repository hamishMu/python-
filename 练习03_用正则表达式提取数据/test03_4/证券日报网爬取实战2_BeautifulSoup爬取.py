"""
爬取beautifulSoup爬取
"""

import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def spyderSomething(kw, page):
    url = 'http://search.zqrb.cn/search.php?q=' + kw + '&m=&f=_all&src=all&s=newsdate_DESC&p=' + str(page)
    response = requests.get(url, headers=headers, timeout=10)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    titles = soup.select('dt a')
    # print(titles)
    dates = soup.select('.field-info span')
    # print(dates)
    for i in range(len(titles)):
        title = titles[i].text
        href = titles[i]['href']
        print("标题：" + title + " 链接：" + href + " " + dates[2].text)


if __name__ == '__main__':
    kws = ['茶百道']
    for kw in kws:
        for i in range(1, 5):
            spyderSomething(kw, i)
