"""
实战中，很多网页都是经过渲染的，直接通过requests很难获取真正的网页源码
使用selenium库则能获取大部分的网页源码，
"""
# selenium可以模拟人在浏览器中的鼠标和键盘操作。
# 下面模拟在百度首页搜索框内输入python进行搜索操作
from  selenium import  webdriver
import  time
# 申明要模拟的浏览器是谷歌浏览器
brower = webdriver.Chrome()
# 将模拟浏览器最大化
brower.maximize_window()
# 浏览器打开指定的网页
brower.get('https://www.baidu.com/')
# 定位网页元素有两种方法xpath 和css选择器法
# brower.find_element_by_xpath("xpath表达式")
brower.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
brower.find_element_by_xpath('//*[@id="su"]').click()

time.sleep(5)
# 关闭浏览器
brower.quit()

"""
css选择器是另外一中定位网页元素的手段
find_element_by_css_selector()
"""

# 3 .无界面浏览器模式，如果希望运行代码时候不弹出浏览器窗口，
# 启用chrome headless模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
brower = webdriver.Chrome(options=chrome_options)


"""
有的网页需要时间来加载和刷新，需要使用time.sleep()让程序暂停一会，然后
brower.page_siyrce获取的才是正确的网页源代码。

selenium其他知识点
brower.switch_to.frame("子页面")

"""


