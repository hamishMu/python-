"""
本案例要从百度新闻爬取数据写入mysql数据库，并进行去重处理
"""
import requests
import re
import pymysql

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}


def baidu(company):
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&medium=0&wd=' + company
    response = requests.get(url=url, headers=headers)
    data = response.text
    titles = re.findall('aria-label="标题：(.*?)"', data)
    hrefs = re.findall('<a href="(.*?)" target="_blank" class="news-title-font_1xS-F" aria-label="标题：.*?"', data)
    print(len(titles))
    for i in range(len(titles)):
        db = pymysql.connect(
            user='root',
            password='root',
            host='localhost',
            port=3306,
            database='books',
            charset='utf8'
        )
        cur = db.cursor()
        title = titles[i]
        print(title)
        href = hrefs[i]
        print(href)
        # 去重思路，爬取道一条新闻数据后，现在数据库中查找，如果发现该新闻的标题已经存在，就不写入数据库。
        sql_1 = 'select * from test where title =%s'
        cur.execute(sql_1,title)
        data_all = cur.fetchall()
        title_all = []
        for j in range(len(data_all)):
            title_all.append(data_all[j][1])
        if title not in data_all:
            sql = 'insert into test(title,href) values(%s,%s)'
            cur.execute(sql, (title, href))
            db.commit()
        else:
            db.rollback()
        cur.close()
        db.close()



baidu('矢量科技')
