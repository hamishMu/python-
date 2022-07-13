"""
进程池Pool
"""
import  multiprocessing
import  time


# 创建玩进程池后，接下来将执行函数传递给进程
# 参数：函数名和和函数的参数列表
def t1(x):
    result = 0
    for i in range(x):
        result += i
    print("从0到："+str(x-1)+"的累加和为："+str(result))

if __name__ == '__main__':
    start_time = time.time()
    # 设置进程池的最大进程数3,所有任务结束耗时：4.72
    # 进程数为1，所有任务结束耗时：5.27
    pool = multiprocessing.Pool(processes=1)
    num = [1000000,200000,3000000,4000000,5000000,60000000]
    pool.map(t1,num)
    end_time = time.time()
    total_time = end_time-start_time
    print("所有任务结束耗时："+str(round(total_time,2)))
