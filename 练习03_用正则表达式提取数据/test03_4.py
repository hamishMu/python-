"""
使用修饰符re.S

"""
import re

res = """
    文本A
    百度新闻文本B
"""
p_source = '文本A(.*?)文本B'
source = re.findall(p_source, res, re.S)
print(source)

#  re.sub(需要替换的内容，替换值，原字符串)
title = '<!--s -test--> 双十一点燃线下经济"小时达"服务成<em>阿里巴巴</em>增长新引擎<!--/s-text-->'
title  =re.sub('<.*?>','',title)
print(title)

# 正则表达式中[]的用法，如果想匹配这些.*?,需要使用[]