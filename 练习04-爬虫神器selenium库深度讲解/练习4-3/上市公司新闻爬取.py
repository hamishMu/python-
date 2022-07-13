"""
https://eastmoney.com/news/s?keyword =格力电器
"""
from selenium import webdriver
import  time
import  re
url ='https://so.eastmoney.com/news/s?keyword=中原银行'
brower = webdriver.Chrome()
brower.get(url)
data = brower.page_source
# print(data)
title = re.findall('<div class="news_item_t"><a href=".*?" target="_blank">(.*?)</a></div>',data)
href = re.findall('<div class="news_item_t"><a href="(.*?)" target="_blank">.*?</a></div>',data)
for i in range(len(title)):
    title[i] = re.sub('<.*?>','',title[i])
    print(str(i+1)+". "+ title[i]+". 链接: "+href[i])
time.sleep(10)
brower.quit()
