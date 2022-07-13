"""
实战中，很多网页都是经过渲染的，直接通过requests很难获取真正的网页源码
使用selenium库则能获取大部分的网页源码，
"""
from  selenium import  webdriver
# 申明要模拟的浏览器是谷歌浏览器
brower = webdriver.Chrome()
# 将模拟浏览器最大化
brower.maximize_window()
# 浏览器打开指定的网页
brower.get('https://www.baidu.com/')
# 关闭浏览器
brower.quit()

# selenium可以模拟人在浏览器中的鼠标和键盘操作，下面模拟在百度首页的
