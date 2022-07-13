"""
正则表达式提取数据非常高效，不仅可以在爬虫任务中从网页中提取数据。
还可以在非爬虫任务中从普通文本中提取信息。
1.正则表达式基础1.findall()函数,返回数据是一个列表，
"""
# 1. 导入正则表达式包re
import re
# 使用re库中的findall()函数提取文本，匹配规则中
# ‘\d’表示匹配一个数字，返回的是一个列表['123']
a = 'Hello 123 world'
result = re.findall('\d\d\d',a)
content  = 'Hello 123 world 456 华小智python教学 135'
result2 = re.findall('\d\d\d',content)

print(result)
print(result2)


# 正则表达式规则组合千变万化，不过在爬虫任务中，大部分用到的就是(.*?)与.*?
