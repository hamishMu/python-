"""
使用非谈判匹配查找网页
"""
import requests
import re

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
url = 'https://search.sina.com.cn/news?q=阿里巴巴'

response = requests.get(url=url,headers=headers)
data2 = response.text
# print(data2)
p_title = "<a.*?>(.*?)<font color='red'>(.*?)</font>(.*?)</a>"
result = re.findall(p_title,data2)
print(result)

# .*?是用于填充我们不关心的内容。
# 正则表达式：自动考虑换行的修饰符re.S
# 修饰符很多，最常用的是re.S.作用的是让findall()函数在查找时候自动忽略换行的影响。
# re.findall(匹配规则，原始文本，re.S)
