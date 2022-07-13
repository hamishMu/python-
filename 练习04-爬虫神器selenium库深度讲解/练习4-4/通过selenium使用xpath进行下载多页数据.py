"""


"""
from urllib.request import urlretrieve

from selenium import webdriver
import re
import time

for i in range(10):
    data_all = ''
    url = 'http://www.sse.com.cn/disclosure/credibility/supervision/inquiries/'
    brower = webdriver.Chrome()
    brower.get(url)
    data = brower.page_source
    time.sleep(3)
    brower.find_element_by_xpath('//*[@id="ht_codeinput"]').send_keys(i + 1)
    brower.find_element_by_xpath('//*[@id="pagebutton"]').click()
    data_all += data
    company_code = re.findall('<tr class="isClickTr">.*?<td>(.*?)</td>', data, re.S)
    company_name = re.findall('<td><div class="nowrap">(.*?)</div></td>', data, re.S)
    date = re.findall('<td width="80px">.*?<div class="nowrap">(.*?)</div></td>', data, re.S)
    href = re.findall('<td><a href="(.*?)" target="_blank">.*?</a>', data)
    title = re.findall('<td><a href=".*?" target="_blank">(.*?)</a>', data)
    for i in range(len(company_name)):
        print("日期：" + date[i])
        print("链接：" + href[i])
        print("标题：" + title[i])
        print("公司名称：" + company_name[i].strip() + ". 公司代码：" + company_code[i] + ". 日期：" + date[i] + ".标题: " + title[
            i] + "链接：" + href[i])
        # response = requests.get(url=href[i])
        # response.encoding = 'UTF-8'
        # res = response.content
        urlretrieve(href[i], "D:/爬虫/data/" + title[i] + ".pdf")

