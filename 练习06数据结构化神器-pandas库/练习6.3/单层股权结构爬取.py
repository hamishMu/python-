"""
https://aiqicha.baidu.com/brand/detail?pid=65781811851309&id=414444999
"""

from selenium import webdriver
import  re
import  time
import pandas as pd

company_name = '华能信托'
browser = webdriver.Chrome()

url ='https://www.aiqicha.com/company_detail_65781811851309'
browser.get(url)
time.sleep(30)
data = browser.page_source
# print(data)

table = pd.read_html(data)
df = table[1]
print(df)


