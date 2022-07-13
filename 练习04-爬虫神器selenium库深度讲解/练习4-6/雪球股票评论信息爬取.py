"""
https://xueqiu.com 是一个股票投资交流平台
"""
from selenium import webdriver
import  time

url ='https://xueqiu.com/S/SH600519'
brower = webdriver.Chrome()
brower.get(url)
# 为手动登录设置足够的等待时间
time.sleep(30)
data = brower.page_source

