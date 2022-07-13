"""
一个任务就是一个进程，在一个进程中可以同事做几件事。
在浏览器中可以浏览网页，听音乐，下载文件，在一个进程内部同事进行的
多个子任务成为线程Thread.
Cpu通过调度算法，轮流让每个进行交替执行。
爬虫方案：
1.在一个进程中启动多给线程
2.启动多个进行，通过多个进程进行多个爬虫任务。
"""
# 多线程被称为并发操作。
# 多进程成为并行操作。
# 爬虫的时候io操作，网络数据交换，文件读写不依赖cpu,可以通过使用多线程来提高效率

# 一般使用线程建议的数量是5-10个，

import time


def func1():
    print("任务1进行中，任务1持续3秒")
    time.sleep(3)
    print("任务1结束！")

def func2():
    print("任务2进行中，任务2持续2秒")
    time.sleep(2)
    print("任务2结束！")

start_time = time.time();
func1()
func2()
end_time = time.time()
total_time = end_time- start_time
print("所有任务结束，总耗时:"+str(round(total_time,2)))