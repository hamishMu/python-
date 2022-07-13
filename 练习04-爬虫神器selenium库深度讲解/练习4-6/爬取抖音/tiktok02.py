"""
https://www.tgbak.com/抖音小姐姐/
<a href="(.*?)mp4">.*?</a>
"""
import requests
import time
from bs4 import BeautifulSoup
import os


def spyderTikTok():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    }
    with open("resource.txt", "r")as f:
        res = f.read()
        soup = BeautifulSoup(res, "html.parser")
        hrefs = soup.select(".fb-n a")
        print(hrefs)
        for i in hrefs:
            name = i.text
            href = "https://www.tgbak.com/"+i['href']
            if href.endswith("mp4"):
                if not os.path.exists("D:/爬虫/data/抖音小姐姐"):
                    os.makedirs("D:/爬虫/data/抖音小姐姐")
                else:
                    with open("D:/爬虫/data/抖音小姐姐/" + name.split('.')[0] + ".mp4", 'wb')as f:
                        response = requests.get(href, headers=headers)
                        f.write(response.content)
            else:
                pass


if __name__ == "__main__":
    spyderTikTok()
