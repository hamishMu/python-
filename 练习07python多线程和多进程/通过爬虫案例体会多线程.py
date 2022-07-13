"""

"""
import  time
import  requests
import  threading
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
def f1():
    url ='https://www.baidu.com/s?tn=news&rtt=4&word=阿里巴巴'
    res = requests.get(url,headers=headers).text
    print(len(res))


def f2():
    url = 'https://www.baidu.com/s?tn=news&rtt=4&word=贵州茅台'
    res = requests.get(url, headers=headers).text
    print(len(res))
# 单线程所有任务结束，总耗时:2.68
# 多线程所有任务结束，总耗时:1.7
start_time = time.time();
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
total_time = end_time - start_time
print("所有任务结束，总耗时:" + str(round(total_time, 2)))
