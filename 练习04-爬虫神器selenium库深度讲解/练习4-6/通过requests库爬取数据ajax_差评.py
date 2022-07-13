"""
https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100000177770&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
差评：
https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98&productId=100000177770&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
"""
import re

import  requests
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    }
res_all = ''
for i in range(60):
    url = 'https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98&productId=100000177770&score=1&sortType=5&pageSize=10&isShadowSku=0&fold=1&page='+str(i)
    res = requests.get(url,headers=headers).text
    res_all += res
p_comment = '"content":"(.*?)"'
comment = re.findall(p_comment,res_all)
s= "213"
s.__contains__("1")
for i in range(len(comment)):
    comment[i] = comment[i].strip()
    if comment[i].__contains__("尊敬的客户") or comment[i].__contains__("感谢您对京东的支持")\
            or comment[i].__contains__("尊敬的") or comment[i].__contains__('祝您生活愉快'):
        pass
    else:
        with open("comment_bad_jd.txt",'a+',encoding="utf-8")as f:
            f.write(str(i+1)+". "+comment[i]+"\n")
            print(str(i+1)+". "+comment[i])
