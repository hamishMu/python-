"""
定义一个爬虫函数test,爬取百度新闻中的不同公司的新闻、
"""
import os
import  time
import  requests
import  threading

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def baidu(company):
    url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&&word=' + company
    # 使用timeout防止子线程被卡死
    res = requests.get(url, headers=headers).text
    print(len(res))


companies = [
    '阿里巴巴',
    '华能信托',
    '京东',
    '一号店',
    '腾讯'
]

start_time = time.time()
thread_list = []
for i in range(len(companies)):
    t = threading.Thread(target=baidu,args=(companies[i],))
    thread_list.append(t)
for i in thread_list:
    i.start()
for i in thread_list:
    i.join()
end_time = time.time()
total_time = end_time-start_time
print("所有任务结束，耗时："+str(total_time))
