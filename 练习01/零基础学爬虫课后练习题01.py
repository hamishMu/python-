"""
1、 使用for循环语句计算1加到10000的结果
2. 结合使用if语句，for 语句，和range()语句批量打印输出1-100的奇数
3. 提取a ="2020-07-25 10:53"中的年月日信息
4. 使用两种方法删除a =' 华能信托是家好公司 '首尾的空格。
5.提取列表a =['丁一','王二','张三','李四','赵五']
"""
# 1.
result = 0
for i in range(1, 10001):
    result += i
print("1加到10000的结果是: {}".format(result))

# 2.
print("打印出的奇数为：")
for i in range(1, 101):
    if i % 2 == 1:
        print(i, end=",")
    else:
        continue
print()
# 3
a = '2020-07-25 10:53'
l = a.split(" ")[0].split("-")
print("年:" + l[0])
print("月:" + l[1])
print("日:" + l[2])

# 4、
a = ' 华能信托是家好公司 '
print("原始字符串为:" + a)
print("去掉首尾空格:" + a.strip())
b = a.replace(" ", '')
print("去掉首尾空格:" + b)

# 5
aa = ['丁一', '王二', '张三', '李四', '赵五']
b = list(range(0, len(aa), 2))
print(b)
for i in b:
    print(aa[i])
