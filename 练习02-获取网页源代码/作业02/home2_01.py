"""
通过request获取虎扑nba页面网页源代码
"""
import requests

url = 'https://nba.hupu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
print(response.status_code)
print(response.text)
