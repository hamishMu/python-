"""
https://so.eastmoney.com/yanbao/s?keyword=中原银行
"""
import os
from selenium import webdriver
import re
import requests
import traceback

try:
    brower = webdriver.Chrome()
    url = 'https://so.eastmoney.com/yanbao/s?keyword=格力电器'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    brower.get(url)
    data = brower.page_source
    # print(data)
    title = re.findall('</span><a href=".*?" target="_blank">(.*?)</a>', data)
    href = re.findall('</span><a href="(.*?)" target="_blank">.*?</a>', data)
    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        print(str(i + 1) + "." + title[i] + " - 链接：" + href[i])
        brower2 = webdriver.Chrome()
        brower2.get(href[i])
        data2 = brower2.page_source
        brower2.quit()
        name = re.findall('<div class="detail-header">.*?<h1>(.*?)</h1>', data2,re.S)
        # print(name)
        href_pdf = re.findall(
            '<a style="color: #039; text-decoration: underline; font-family: 宋体; font-size: 14px;".*? href="(.*?)">',
            data2, re.S)
        # print(href_pdf)
        response = requests.get(href_pdf[0], headers=headers, timeout=60)
        res_pdf = response.content
        if not os.path.exists("D:/爬虫/data/格力"):
            os.makedirs("D:/爬虫/data/格力")
        else:
            for i in name:
                print("name:"+i)
                i=i.strip()
                with open("D:/爬虫/data/格力/" + i + ".pdf", 'wb')as f:
                    f.write(res_pdf)
except Exception:
    print("发生异常")
    print(traceback.print_exc())
finally:
    brower.quit()
