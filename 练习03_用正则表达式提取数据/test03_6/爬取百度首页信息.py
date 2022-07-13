"""
https://www.baidu.com
"""
import  requests
url = 'https://www.baidu.com'
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
response = requests.get(url,headers = headers)
res = response.text
print(res)