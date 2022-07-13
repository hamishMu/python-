"""
1.处理验证码页的乱码
2.将网页代码设置为weixin()函数的返回值，
3.编写ip代理地址的函数，
4.合理构造循环，实现智能ip切换。
"""
"""
http://weixin.sogou.com/
"""
import re
import time
import requests
import queue

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
}


def getIp(pn):
    url = 'https://www.kuaidaili.com/free/inha/' + str(pn) + '/'
    data_all = ''
    for i in range(pn):
        response = requests.get(url, headers=headers)
        data = response.text
        data_all += data
    ips = re.findall('<td data-title="IP">(.*?)</td>', data_all)
    ports = re.findall('<td data-title="PORT">(.*?)</td>', data_all)
    q = queue.Queue()
    for i in range(len(ips)):
        ip = ips[i]
        port = ports[i]
        ip = ip + ':' + port
        q.put(ip)
    return q


def ChangeIP():
    ip_q = getIp(2)
    ip = ip_q.get()
    print("代理ip为" + ip)
    proxies = {
        'http':'http://'+ip,
        'https':'https://'+ip
    }
    return proxies


def weixin(company):
    url = 'https://weixin.sogou.com/weixin?type=2&query=' + company

    res = requests.get(url, headers=headers, timeout=10, proxies=proxies).text
    # print(res)
    try:
        res.encode('ISO-8859-1').decode('utf8')
    except:
        try:
            res.encode('ISO-8859-1').decode('gbk')
        except:
            res = res

    titles = re.findall('uigs="article_title_.*?">(.*?)</a>', res)
    hrefs = re.findall('<div class="txt-box">.*?<h3>.*?<a target="_blank" href="(.*?)" ', res, re.S)
    source = re.findall('uigs="article_account_.*?">(.*?)</a>', res)
    date = re.findall('timeConvert\(\'(.*?)\'\)', res)

    for i in range(len(titles)):
        titles[i] = re.sub('<.*?>', '', titles[i])
        titles[i] = re.sub('&.*?;', '', titles[i])
        timestamp = int(date[i])
        timeArray = time.localtime(timestamp)
        date[i] = time.strftime('%Y-%m-%d', timeArray)
        hrefs[i] = 'https://weixin.sogou.com' + hrefs[i]
        print(str(i + 1) + "." + titles[i] + '+' + source[i] + '+' + date[i])
        print(hrefs[i])
    return res


if __name__ == '__main__':
    companies = ['92号汽油', '软件测试', '爬虫']
    proxies = ChangeIP()
    for company in companies:
        try:
            res = weixin(company)
            while '验证码' in res:
                print("原IP代理地址失效，开始切换ip代理地址.")
                proxies = ChangeIP()
                res = weixin(company)
            else:
                print(company + "微信公众号文章爬取成功!")
        except:
            print(company + "微信公众号文章爬取失败!")
