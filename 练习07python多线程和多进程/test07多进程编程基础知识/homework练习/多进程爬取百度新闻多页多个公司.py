"""
多线程爬取百度新闻关于五粮液。贵州茅台的多页新闻
"""
import re
import time
import requests
import multiprocessing

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def spyderNews(company, pn):
    url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&&word=' + company + '&pn=' + str((pn) * 10)
    # 使用timeout防止子线程被卡死
    response = requests.get(url=url, headers=headers,timeout=10)
    data = response.text
    titles = re.findall('aria-label="标题：(.*?)"', data)
    hrefs = re.findall('<a href="(.*?)" target="_blank" class="news-title-font_1xS-F" aria-label="标题：.*?"', data)
    for i in range(len(titles)):
        print(str(i + 1) + ".标题为：" + titles[i] + ". 链接：" + hrefs[i])


# 耗时：11.101944208145142
# 耗时：1.5698537826538086
if __name__ == "__main__":
    #耗时：2.9972290992736816
    s_time = time.time()
    # 创建空的队列
    thread_list =[]
    companies = ['五粮液', '贵州茅台','腾讯']
    for i in range(10):
        for company in companies:
            t = multiprocessing.Process(target=spyderNews,args=(company,i))
            thread_list.append(t)
    for i in thread_list:
        i.start()
    for i in thread_list:
        i.join()
    e_time = time.time()
    t_time = e_time - s_time
    print("耗时：" + str(t_time))
