"""
有的动态渲染的页面，网址不明确的页面，需要使用selenium库完成爬取。
如果有IP反爬机制，同时需要使用IP代理。
"""
import queue
import re

import requests
from selenium import webdriver

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
}


def getIp(pn):
    url = 'https://www.kuaidaili.com/free/inha/' + str(pn) + '/'
    data_all = ''
    for i in range(pn):
        response = requests.get(url, headers=headers)
        data = response.text
        data_all += data
    ips = re.findall('<td data-title="IP">(.*?)</td>', data_all)
    ports = re.findall('<td data-title="PORT">(.*?)</td>', data_all)
    q = queue.Queue()
    for i in range(len(ips)):
        ip = ips[i]
        port = ports[i]
        ip = ip + ':' + port
        q.put(ip)
    return q


if __name__ == '__main__':
    ip = getIp(2)
    chrome_options = webdriver.ChromeOptions()
    while True:
        chrome_options.add_argument('--proxy-server=' + ip.get())
        browser = webdriver.Chrome(options=chrome_options)
        url = 'https://httpbin.org/get'
        browser.get(url)
        data = browser.page_source
        print(data)
        if '该网页无法正常运作' not in data:
            break
        else:
            browser.quit()
            ip.get()
