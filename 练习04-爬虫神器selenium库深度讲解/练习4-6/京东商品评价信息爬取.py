"""
https://item.jd.com/100000177770.html
分别使用selenium requests库完成爬取
"""
# 1. 使用selenium爬取
import  time
import  re
from selenium import webdriver
url ='https://item.jd.com/100000177770.html'
brower = webdriver.Chrome()
brower.get(url)
time.sleep(30)
# 为手动登录查看评价
# 使用xpath 模拟点击评价
brower.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]').click()

data = brower.page_source

data_all = data
brower.find_element_by_xpath('//*[@id="comment-0"]/div[12]/div/div/a[2]').click()
time.sleep(3)
data = brower.page_source
data_all +=data
for i in range(8):
    brower.find_element_by_xpath('//*[@id="comment-0"]/div[12]/div/div/a[8]').click()
    time.sleep(3)
    data = brower.page_source
    data_all += data

brower.quit()
p_comment = '<p class="comment-con">(.*?)</p>'
comment = re.findall(p_comment,data)
for i in range(len(comment)):
    comment[i] = comment[i].replace(r"\n",'')
    print(str(i+1+". "+comment[i]))