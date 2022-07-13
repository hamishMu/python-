"""
http://www.cb.com.cn

"""
import  requests
import  re
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

url = 'http://www.cb.com.cn/index/list/jj/cv/5'
response = requests.get(url,headers =headers)
data = response.text

titles = re.findall('<a class="f_hover_red f_size_20 f_size_16_mp text_ellipsis_2" target="_blank" href=".*?" title=".*?">(.*?)</a>',data)
contents = re.findall('<a class="opacity_hover_v7 m_t_15 text_ellipsis_2 f_color_gray_v6 d_none_mp" href=".*?" target="_blank">(.*?)</a>',data)
for i in range(len(titles)):
    titles[i] = titles[i].strip()
    print(str(i+1)+". 标题： "+titles[i]+" .内容："+contents[i])
