"""
https://movie.douban.com/top250
"""
import requests
import re
import os
# from urllib.request import  urlretrieve  下载文件

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def spyderDoubanMovie(page):
    for i in range(page):
        num = i * 25
        url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        res = requests.get(url=url, headers=headers).text

        p_title = '<img width="100" alt="(.*?)"'
        title = re.findall(p_title, res)
        p_img = '<img width="100" alt=".*?" src="(.*?)" class="">'
        img = re.findall(p_img, res)
        # print(title)
        # print(img)
        if not os.path.exists("D:/爬虫/data/images"):
            os.makedirs("D:/爬虫/data/images")
        else:
            for i in range(len(title)):
                res = requests.get(img[i])
                with open("D:/爬虫/data/images/" + title[i] + ".jpg", "wb") as f:
                    f.write(res.content)


if __name__ == "__main__":
    spyderDoubanMovie(5)
