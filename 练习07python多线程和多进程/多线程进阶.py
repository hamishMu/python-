"""
创建固定的数量的线程-5-10个，需要一个容器来存放。
列表是线程不安全的，因此需要一个队列，queue，而且是线程安全的，
"""
import  queue
import  threading
import  requests
import  re
import  time

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

companies = [
    '阿里巴巴',
    '华能信托',
    '京东',
    '一号店',
    '腾讯'
]

url_queue = queue.Queue()

def crawl():
    for company in companies:
        url_i = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&medium=0&wd='+company
        url_queue.put(url_i)
    while not url_queue.empty():
        url = url_queue.get()
        print(url)
        data = requests.get(url,headers=headers,timeout=10).text
        titles = re.findall('aria-label="标题：(.*?)"', data)
        hrefs = re.findall('<a href="(.*?)" target="_blank" class="news-title-font_1xS-F" aria-label="标题：.*?"', data)
        for i in range(len(titles)):
            print(str(i+1)+"."+titles[i]+".链接："+hrefs[i])

start_time = time.time()
thread_list = []
for i in range(5):
    t = threading.Thread(target=crawl)
    thread_list.append(t)
for i in thread_list:
    i.start()
for i in thread_list:
    i.join()
end_time = time.time()
total_time = end_time-start_time
print("所有任务结束，耗时："+str(round(total_time,2)))
