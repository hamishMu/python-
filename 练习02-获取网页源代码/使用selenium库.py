# 通过selenium 模拟浏览器,获取新浪财经股票信息
# 1. 导入Selenium库中的webdriver功能
from selenium import  webdriver
# 2. 要模拟的浏览器是谷歌浏览器
browser = webdriver.Chrome()
# 3. 需要访问的网址
browser.get("https://vip.stock.finance.sina.com.cn/mkt/")
# 获取网页源代码
data = browser.page_source
print(data)
# 4. 关闭模拟浏览器
browser.quit()