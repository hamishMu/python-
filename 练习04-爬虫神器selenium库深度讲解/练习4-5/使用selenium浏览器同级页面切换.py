"""
使用selenium_to.window()函数，
浏览器同级页面切换

窗口切换的具体方法：
1， 使用window_handles 属性获取浏览器所有窗口的句柄集合
2，再使用switch_to.window()函数根据句柄切换到对应的窗口。
"""
import re
import time

from selenium import webdriver

brower = webdriver.Chrome()
url ='http://www.baidu.com/s?rtt=1&tn=news&word=阿里巴巴'
brower.get(url)
# 模拟单机第一条新闻链接，会打开一个新的浏览器窗口展示该新闻的详情
brower.find_element_by_xpath('//*[@id="1"]/div/h3/a').click()
# 1. 核心1 .获取当前浏览器所有窗口的句柄
handles = brower.window_handles
print(handles)

#  切换到最新打开的窗口
brower.switch_to.window(handles[-1])

# print(data)
time.sleep(3)
data = brower.page_source
with open("百度_ali2.txt",'w+',encoding='utf8')as f:
    f.write(data)
brower.quit()


