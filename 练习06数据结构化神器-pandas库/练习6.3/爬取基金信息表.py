"""
http://fund.eastmoney.com/data/fundranking.html#tgp;c0;r;s6yzf;pn50;ddesc;qsd20210307;qed20220307;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb
"""
import  pandas as pd
from selenium import webdriver
import  time
import  re

url ='http://fund.eastmoney.com/data/fundranking.html#tgp'

brower = webdriver.Chrome()
brower.maximize_window()
brower.get(url)

data = brower.page_source
table = pd.read_html(data)
df = table[3]
print(df)
brower.quit()




