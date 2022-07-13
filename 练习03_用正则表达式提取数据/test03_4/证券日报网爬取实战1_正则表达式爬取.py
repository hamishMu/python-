"""
证券日报网：http://www.zqrb.cn/
1.正则表达式爬取方式
2、BeautifulSoup爬取
"""
import requests
import time
import re

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def spyderSomething(kw, page):
    url = 'http://search.zqrb.cn/search.php?q=' + kw + '&m=&f=_all&src=all&s=newsdate_DESC&p=' + str(page)
    response = requests.get(url, headers=headers, timeout=10)
    data = response.text
    p_title = '<a href=".*?" target="_blank"><h4>(.*?)</h4></a>'
    p_href = '<a href="(.*?)" target="_blank"><h4>.*?</h4></a>'
    p_date = '<span><strong>时间:</strong>(.*?)</span>'
    title = re.findall(p_title, data)
    href = re.findall(p_href, data)
    date = re.findall(p_date, data)
    for i in range(len(title)):
        print("证券日报爬取数据：" + "关键字：" + kw)
        title[i] = re.sub('<.*?>', '', title[i])
        print("标题：" + title[i] + "证券日报 " + date[i]+" 链接："+href[i])


if __name__ == '__main__':
    kws = ['贵州茅台']
    for kw in kws:
        for i in range(1, 5):
            spyderSomething(kw, i)
            time.sleep(3)
