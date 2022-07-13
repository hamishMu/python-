"""
多线程爬取百度新闻关于贵州茅台的多页新闻
"""
import re
import time
import requests
import  multiprocessing


headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

def spyderNews(pn):
    url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&&word=贵州茅台&pn=' + str((pn) * 10)
    # 使用timeout防止子线程被卡死
    response = requests.get(url=url, headers=headers)
    data = response.text
    titles = re.findall('aria-label="标题：(.*?)"', data)
    hrefs = re.findall('<a href="(.*?)" target="_blank" class="news-title-font_1xS-F" aria-label="标题：.*?"', data)
    for i in range(len(titles)):
        print(str(i+1)+".标题为："+titles[i]+". 链接："+hrefs[i])

# 耗时：11.101944208145142
# 耗时：1.5698537826538086
if __name__ =="__main__":
    s_time = time.time()
    # 创建空的队列
    pool = multiprocessing.Pool(processes=3)
    pool.map(spyderNews,list(range(10)))
    e_time = time.time()
    t_time = e_time - s_time
    print("耗时："+str(t_time))