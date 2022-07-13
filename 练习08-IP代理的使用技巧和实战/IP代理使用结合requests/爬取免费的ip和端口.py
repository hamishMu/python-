"""
https://www.kuaidaili.com/free/inha/
"""
import requests
import re
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
}

"""
 <td data-title="IP">111.59.199.58</td>
 <td data-title="PORT">8118</td>
"""
def getIp(pn):
    url = 'https://www.kuaidaili.com/free/inha/' + str(pn) + '/'
    response = requests.get(url, headers=headers)
    data = response.text
    ips = re.findall('<td data-title="IP">(.*?)</td>',data)
    ports = re.findall('<td data-title="PORT">(.*?)</td>',data)
    ip_list = []
    for i in range(len(ips)):
        ip = ips[i]
        port = ports[i]
        ip = ip+':'+port
        ip_list.append(ip)
    return  ip_list


print(getIp(3))

