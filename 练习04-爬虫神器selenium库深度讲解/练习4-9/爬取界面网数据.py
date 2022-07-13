"""
爬取界面网  https://www.jiemian.com
"""
import  requests
import  re



headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
data_all = ''
for i in range(10):
    url = 'https://a.jiemian.com/index.php?m=search&a=index&msg=%E4%B9%8C%E5%85%8B%E5%85%B0&type=news&page='+str(i+1)
    response = requests.get(url,headers=headers)
    response.encoding='utf-8'
    data = response.text
    data_all += data
    with open("youjie.txt",'a+',encoding="utf-8")as f:
        f.write(data_all)
    # print(data)
titles = re.findall('<div class="news-header"><h3><a href=".*?"  target="_blank" title="(.*?)">',data_all)
hrefs = re.findall('<div class="news-header"><h3><a href="(.*?)"  target="_blank" title=".*?">',data_all)
content = re.findall('<div class="news-main"><p>(.*?)</p></div>',data_all)
for i in range(len(titles)):
    print(str(i+1)+"标题："+titles[i]+". 链接："+hrefs[i])
    content[i] = re.sub('<.*?>','',content[i])
    print("简介："+content[i])