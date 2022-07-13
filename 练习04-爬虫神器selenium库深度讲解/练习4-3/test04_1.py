"""

"""
import  requests
import  re
url = 'http://data.eastmoney.com/report/zw_stock.jshtml?infocode=AP202108241512140374'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
response = requests.get(url,headers = headers)
data = response.text
# print(data)
name = re.findall('<div class="detail-header">.*?<h1>(.*?)</h1>', data,re.S)
print(name)
href_pdf = re.findall('<a style="color: #039; text-decoration: underline; font-family: 宋体; font-size: 14px;".*? href="(.*?)">',data, re.S)
print(href_pdf)
for i in name:
    i = i.strip()
    print(i)
    with open(i+".txt",'w+')as f:
        f.write("test!")

