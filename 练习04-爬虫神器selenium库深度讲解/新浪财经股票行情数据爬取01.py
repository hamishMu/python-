"""
通过selenium库从新浪财经的股票行情页面爬取数据
"""
from selenium import  webdriver
import  re
import  time
brower = webdriver.Chrome()
url = 'https://finance.sina.com.cn/realstock/company/sh600519/nc.shtml'
brower.get(url)
data = brower.page_source
p_price = '<div id="price" class=".*?">(.*?)</div>'
price = re.findall(p_price,data)
print(price)
time.sleep(10)
brower.quit()


