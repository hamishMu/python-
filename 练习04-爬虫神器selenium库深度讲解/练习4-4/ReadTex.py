"""
读取文件中的网页源代码

"""
import re
import requests
from urllib.request import urlretrieve


def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
  @blocknum: 已经下载的数据块
  @blocksize: 数据块的大小
  @totalsize: 远程文件的大小
  '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent > 100:
        percent = 100
    print("%.2f%%" % percent)


with open("page_source.txt", 'r', encoding="UTF-8")as f:
    data = f.read()
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
        urlretrieve(href[i], title[i] + ".pdf")
