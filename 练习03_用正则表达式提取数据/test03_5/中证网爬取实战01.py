"""
中证网：https://www.cs.com.cn/
http://search.cs.com.cn/search?searchword=贵州茅台&channelid=215308#
"""

import  requests
from selenium import webdriver
import  re

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
# brower = webdriver.Chrome()

url ='http://search.cs.com.cn/search?searchword=贵州茅台&channelid=215308#'

response = requests.get(url,headers=headers,timeout=10)
data  = response.text
# print(data)
p_title = '<a style="font-size: 16px;color: #0066ff;line-height: 20px" href=".*?" target="_blank">(.*?)</a>'
p_href = '<a style="font-size: 16px;color: #0066ff;line-height: 20px" href=(.*?)" target="_blank">.*?</a>'
p_dates = '&nbsp;&nbsp;.*?&nbsp;(.*?)</td>'
p_article = '<td style="font-size: 12px;line-height: 24px;color: #333333;margin-top: 4px;" >.*?(.*?)</td>'
titles = re.findall(p_title,data)
# print(titles)
hrefs = re.findall(p_href,data)
# print(hrefs)
dates = re.findall(p_dates,data,re.S)
# print(dates)
articles = re.findall(p_article,data,re.S)
# print(articles)
source = []
# brower.quit()
for i in range(len(titles)):
    source.append("中国证券报")
    # 清除<xx>格式
    titles[i] = re.sub("<.*?>",'',titles[i])
    dates[i] = dates[i].strip()
    articles[i] = re.sub("<.*?>",'', articles[i])
    print(str(i+1)+", "+titles[i]+ source[i]+" "+dates[i]+articles[i]+hrefs[i])


