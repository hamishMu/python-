"""
selenium 模拟投票功能

"""
url =r'file:///C:/Users/hy/Desktop/python/9.%E8%87%AA%E5%8A%A8%E6%8A%95%E7%A5%A8/vote.html'

import  time
from selenium import webdriver

brower = webdriver.Chrome()
brower.get(url)
for i in range(10):
    brower.find_element_by_xpath('//*[@id="main"]/tbody/tr[1]/td/input').click()
    brower.find_element_by_xpath('//*[@id="main"]/tbody/tr[19]/td/input').click()
    # 切换到提示框，并且模拟点击确定按钮
    brower.switch_to.alert.accept()
    time.sleep(1)