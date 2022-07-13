"""
https://vip.stock.finance.sina.com.cn/mkt/#bjs_root
"""
from selenium import  webdriver
import  pandas as pd

url ='https://vip.stock.finance.sina.com.cn/mkt/#bjs_root'

brower = webdriver.Chrome()
brower.get(url)
brower.switch_to.frame("")
table = pd.read_html(url)[0]
print(table)
# 查询没有显示数据，说明可能是动态渲染。需要使用selenium获取原网页代码。

# pandas 库在爬虫领域的核心代码
#  创建DataFrame 用于组织和管理数据的一种二维表格数据结构。