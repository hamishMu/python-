import requests
import re

url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=冬奥&medium=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
data = response.text
# print(data)
pattern1 = 'aria-label="标题：(.*?)"'
# 不存在换行，就无需添加re.S
result = re.findall(pattern1,data)
print(result)
pattern2 = '<a href="(.*?)" target="_blank" class="news-title-font_1xS-F" aria-label="标题：.*?"'
result2 = re.findall(pattern2,data)
print(result2)
print("+++++++++++++++++++++++++++++++++++++++++++++")\
    
for i in result:
    title = re.sub('<.*?>','',i)
    print(title)

