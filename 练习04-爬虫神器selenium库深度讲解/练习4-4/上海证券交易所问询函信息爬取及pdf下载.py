"""
http://www.sse.com.cn/disclosure/credibility/supervision/inquiries/
点击网站，查看源码发现没有找到需要的内容，说明是js或者xhr
"""
from selenium import webdriver
from urllib.request import urlretrieve
import time
import re

url = 'http://www.sse.com.cn/disclosure/credibility/supervision/inquiries/'

brower = webdriver.Chrome()
brower.get(url)

time.sleep(3)
# 这里必须加3秒的延迟，因为需要等待网页加载完毕。
data = brower.page_source
with open('page_source.txt', 'w+', encoding="utf-8")as f:
    f.write(data)
company_code = re.findall('<tr class="isClickTr">.*?<td>(.*?)</td>', data, re.S)
company_name = re.findall('<td><div class="nowrap">(.*?)</div></td>', data, re.S)
date = re.findall('<td width="80px".*?<div class="nowrap>(.*?)</div>"', data, re.S)
href = re.findall('', data)
brower.quit()
