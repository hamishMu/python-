"""
https://s.weibo.com/weibo?q=支付宝
问题；
1，headers中

"""
import  requests
import  re
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'sec-ch-ua-platform':'windows',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'cookie': 'SUB=_2AkMW87RJf8NxqwJRmP8dxW7haIx3ygrEieKgr0WSJRMxHRl-yT9jqlMmtRB6PXOaphnw3Jazhfir6XpkxyupTNtF5Qvd; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WW-1CdaKf978w86gwypfCAB; SINAGLOBAL=4388561163359.2036.1638874020247; _s_tentry=-; Apache=2665650451119.501.1645579599407; ULV=1645579599518:3:2:2:2665650451119.501.1645579599407:1645519422872'
}


url ='https://s.weibo.com/weibo?q=阿里巴巴'

response = requests.get(url,headers=headers,timeout=10)
response.encoding='UTF8'
data = response.text
p_nick_name = re.findall('<p class="txt" node-type="feed_list_content" nick-name="(.*?)">',data)
p_title = re.findall(' <p class="txt" node-type="feed_list_content" nick-name=".*?">(.*?)</p>',data,re.S)
print(p_title)
for i in range(len(p_title)):
    p_title[i] = p_title[i].strip()
    p_title[i]= re.sub('<.*？>','',p_title[i])
    print(str(i+1)+"."+p_title[i]+"-"+p_nick_name[i])



