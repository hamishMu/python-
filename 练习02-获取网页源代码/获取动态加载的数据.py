"""
动态加载的数据指服务器返回一个网页模板，通过ajax或其他方式填充到模板中，我们想要的数据一般都在服务器返回的json格式数据包中
"""
import  requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
url = 'https://movie.douban.com/j/chart/top_list'
params = {
    'type':'25',
    'interval_id':'100:90',
    'action':'',
    'start':'0',
    'limt':'1'
}
response = requests.get(url=url,headers=headers,params=params)
print(response.json())