"""
https://www.jisilu.cn/data/cbnew/#cb
"""

from selenium import webdriver
import  pandas as pd
import  time
url ='https://www.jisilu.cn/data/cbnew/#cb'
brower = webdriver.Chrome()
brower.maximize_window()

brower.get(url)
data = brower.page_source
tables = pd.read_html(data,header=1)
df = tables[0]
print(df)
df.columns = ['代码','转债名称','现价','涨跌幅'
              ,'正股名称','正股价','正股涨跌'
              ,'正股PB','转股价','转股价值','溢价率','纯债价值'
              ,'债券评级','期权价值','正股波动率','回售触发价','强赎触发价'
              ,'转债占比','机构持仓','到期时间','剩余年限'
              ,'剩余规模','成交额','换手率','到期税前收益'
              ,'回售收益','双低','操作']

df.to_excel("test2.xlsx",index=False)