"""
爬虫主要两个工作：
1. 获取网页源代码  权重  7
2. 解析需要获取的数据  权重 3
获取网页源代码是一切爬虫项目的核心，只要能成功获取网页源代码，就有很多方法解析和提取数据。

获取网页的源代码有两个核心库： request  selenium库，能获取95%的网页源代码。
剩下的5%的网页可能存在IP地址反爬，验证码反爬的措施，后续讲解。
"""
# 百度新闻是一个非常重要的数据源
# 按焦点https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&ie=utf-8&word=冬奥
# 按时间 https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=冬奥&medium=0

# 百度新闻网站只认可浏览器发送请求，不认可python发送的请求，需要设置header
import  requests
url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=冬奥&medium=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
res = requests.get(url,headers=headers).text
print(res)

"""
requests 库的软肋：获取的是未经过渲染的网页源代码。如果使用动态渲染网页，爬取结果往往不是我们想要的代码。
如果要获取动态渲染的网页，需要通过selenium库打开一个模拟浏览器访问网页，然后获取到网页源代码。
主要因为requests 能直接访问网页，速度快。所以当通过requests爬取不到了，采用selenium库。
"""
