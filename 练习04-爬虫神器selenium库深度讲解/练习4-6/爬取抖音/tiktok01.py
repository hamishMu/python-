"""
https://www.tgbak.com/抖音小姐姐/
"""
import requests
import time
from bs4 import BeautifulSoup
import os


def spyderTikTok():
    url = "https://www.tgbak.com/抖音小姐姐/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    }
    response = requests.get(url, headers=headers, timeout=60)
    response.encoding = 'utf8'
    res = response.text
    with open("resource.txt","w+")as f:
        f.write(res)
    soup = BeautifulSoup(res, "html.parser")
    hrefs = soup.select(".item  a")
    print(hrefs)
    for i in hrefs:
        href = i['href']
        a = 1
        if not os.path.exists("D:/爬虫/data/抖音小姐姐"):
            os.makedirs("D:/爬虫/data/抖音小姐姐")
        else:
            with open("D:/爬虫/data/抖音小姐姐/" + a + ".mp4", 'wb')as f:
                f.write(requests.get(i, headers=headers).content)
            a += 1


if __name__ == "__main__":
    spyderTikTok()
