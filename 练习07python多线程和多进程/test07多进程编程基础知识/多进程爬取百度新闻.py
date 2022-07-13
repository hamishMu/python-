"""
使用多进程爬取百度新闻
"""
import multiprocessing
import re
import time
import  requests


headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

def spyderNews(company):
    url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&&word=' + company
    # 使用timeout防止子线程被卡死
    response = requests.get(url=url, headers=headers)
    data = response.text
    titles = re.findall('aria-label="标题：(.*?)"', data)
    hrefs = re.findall('<a href="(.*?)" target="_blank" class="news-title-font_1xS-F" aria-label="标题：.*?"', data)
    for i in range(len(titles)):
        print(str(i+1)+".标题为："+titles[i]+". 链接："+hrefs[i])


if __name__ == '__main__':
    start_time = time.time()
    pool = multiprocessing.Pool(processes=3)
    companies = ['贵州茅台','五粮液','格力电器','中兴通信','腾讯','京东']
    pool.map(spyderNews,companies)
    end_time = time.time()
    total_time = end_time-start_time
    print("程序结束，耗时:"+str(round(total_time,3)))