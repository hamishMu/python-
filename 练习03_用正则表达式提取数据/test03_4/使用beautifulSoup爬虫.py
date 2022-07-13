"""
使用beautifulSoup爬虫，可以根据html解析网页元素并提取文本内容
"""
res = """
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <title>home2_03作业</title>
</head>
<body>
    <h1 class="title">华能信托是家好公司</h1>
    <h1 class="title">上海交大是所好大学</h1>
    <a href="https://www.baidu.com" id="source">百度新闻</a>
</body>
</html>

"""
# 引入beautifulSoup的固定写法
from bs4 import BeautifulSoup

# 激活BeaufitulSoup库，其中”html.parser“表示设置解析器为HTML解析器
soup = BeautifulSoup(res, 'html.parser')
title = soup.select("h1")
print(title)
source = soup.select('a')
print(source)
# 如果需要进一步提取标签中的文本内容，则需要遍历，并通过text属性提取文本内容。
title_all = []
for i in title:
    print(i.text)
    title_all.append(i.text)

print(title_all)
# 通过text属性可以提取文本内容，只会提取文本，可以自动忽略存在的标签。
# 特定的属性，如class ,id beautifulsoup可以进行解析。
"""
select()输入的参数不是标签名，而是class属性值，并且属性值之前需要加上'.'

如果想选特定id属性的标签，可以通过'#'
"""
title2 = soup.select(".title")
source2 = soup.select("#source")
print(title2)
print(source2,type(source2))
for i in source2:
    print(i['href'])
