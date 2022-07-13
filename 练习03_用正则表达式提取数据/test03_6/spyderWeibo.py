import  requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'sec-ch-ua-platform':'windows',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'cookie': 'SUB=_2AkMW87RJf8NxqwJRmP8dxW7haIx3ygrEieKgr0WSJRMxHRl-yT9jqlMmtRB6PXOaphnw3Jazhfir6XpkxyupTNtF5Qvd; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WW-1CdaKf978w86gwypfCAB; SINAGLOBAL=4388561163359.2036.1638874020247; _s_tentry=-; Apache=2665650451119.501.1645579599407; ULV=1645579599518:3:2:2:2665650451119.501.1645579599407:1645519422872'

}

url ='https://s.weibo.com/weibo?q=阿里巴巴'

response = requests.get(url=url,headers=headers)
response.encoding= 'utf8'
data = response.text
print(data)