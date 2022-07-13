"""
需要自己寻找IP代理地址，通常向IP代理上购买ip代理服务。
从ip代理池中提取ip代理地址。
"""

import  requests
proxy = ''
proxies = {'http':"http://"+proxy,
           'https':'https://'+proxy}

url = 'https://httpbin.org/get'
res = requests.get(url,proxy=proxies).text
print(len(res))