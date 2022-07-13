"""
request 除了可以爬取文本信息，还可以下载网页上的文件
1,通过open
2，urlretrieve（）可以下载文件,from urllib.request import urlretrieve

"""
import  requests
url = 'http://www.sse.com.cn//disclosure/listedinfo/announcement/c/new/2022-01-27/600519_20220127_1_sHO38oLo.pdf'
res = requests.get(url)
with open("D:/爬虫/data/报告.pdf","wb") as f:
    f.write(res.content)
