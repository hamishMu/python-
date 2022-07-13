"""
https://www.eastmoney.com/
http://guba.eastmoney.com/list,600519.html
:param：url= 'http://guba.eastmoney.com/list,600519.html'
"""
from selenium import webdriver
import re



try:

    url= 'http://guba.eastmoney.com/list,600519.html'
    brower = webdriver.Chrome()
    brower.get(url=url)
    data = brower.page_source
    title = re.findall('<a href=".*?" title="(.*?)">',data)
    for i in range(len(title)):
        print(str(i+1)+"." +title[i])
except Exception:
    pass
finally:
    brower.quit()

