import  queue

# 创建一个空队列
q = queue.Queue()
# put函数写入数据
q.put(0)
q.put(1)
q.put(2)
q.put(3)
print(q.queue)

# 数据存储后，可以用get函数提取队列中的数据
keyword = q.get()
print(keyword)
#0已经被取走了
print(q.queue)
# 判断队列是否为空empty()函数
print(q.empty())