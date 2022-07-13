"""
多进程使用multiprocessing
"""
import  multiprocessing
import  time

# print(multiprocessing.cpu_count())
# 输出为4 ，说明cpu是4核，启动进程时候不要超过4.
# 因为一个cpu同一时间只能执行一个进咸亨，对于多个进程也是使用时间片轮转算法进行调度。
def t1():
    result = 0
    for i in range(20000000):
        result += i
    print(result)

def t2():
    result = 0
    for i in range(20000000):
        result += i
    print(result)


if __name__ == "__main__":
    start_time = time.time()
    m1 = multiprocessing.Process(target=t1)
    m2 = multiprocessing.Process(target=t2)
    m1.start()
    m2.start()
    m1.join()
    m2.join()
    end_time = time.time()
    total_time = end_time - start_time
    print("所有任务结束，耗时：" + str(total_time))


