# 第一步 引入request库
import requests

# 网址要完整，不能只输入www.baidu.com
url = "https://vip.stock.finance.sina.com.cn/mkt/"
reponse = requests.get(url)
# 通过request.get()函数可以访问该网站，并通过text属性获取网页源代码内容
reponse.encoding = "gb2312"
print(reponse.text)
