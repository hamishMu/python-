"""
使用selenium模拟浏览器获取上海证券交易所网页源代码
"""
from selenium import  webdriver

brower = webdriver.Chrome()
url = 'http://www.sse.com.cn/'
response = brower.get(url=url)
data = brower.page_source
print(data)
brower.quit()
