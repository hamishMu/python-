"""

http://www.shibor.org
爬取方法1 ，用switch_to.frame()函数到子网页
"""

from selenium import webdriver
import  pandas as pd

url = 'http://www.shibor.org'
brower = webdriver.Chrome()
brower.get(url=url)

# 生成文件后，查询网页源代码，并没有发现利率数值。
# 原因是因为有些数据在<iframe>标签中。就是在一个网页中嵌套了另外一个网页。
# Selenium库打开url后，默认操作是在父网页操作，无法获取子网页中的信息，需要使用
# switch_to.frame()函数切换到子网页。现在推荐使用switch_to.frame 替代
brower.switch_to.frame("volume10BondDealQuotesEN")
data = brower.page_source
with open("利率2.txt",'w+',encoding="utf-8")as f:
    f.write(data)
brower.quit()

# 利用pandas库进行快速提取网页中的表格数据。
# table是一个列表，包含该网页中所有的表格
table = pd.read_html("利率2.txt")
df = table[3]
df = df[[1,2,4]]
# 修改列名
df.columns = ['期限','Shibor(%)','涨跌(BP)']
print(df)

