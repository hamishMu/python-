"""
如果多线程需要参数，可以通过参数args传入
threading.Thread(target=test1,args=(参数1，参数2，参数3)
需要注意的：
传入的参数是一个元组，如果传入一个参数，需要后面加一个逗号。
"""
import  threading
import  time

def f1(x):
    print("任务1进行中，此时参数为："+str(x))
    time.sleep(3)
    print("任务1结束")

def f2(x):
    print("任务2进行中，此时参数为："+str(x))
    time.sleep(2)
    print("任务2结束")

start_time = time.time();
t1 = threading.Thread(target=f1,args=('x1',))
t2 = threading.Thread(target=f2,args=('x2',))
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
total_time = end_time - start_time
print("所有任务结束，总耗时:" + str(round(total_time, 2)))