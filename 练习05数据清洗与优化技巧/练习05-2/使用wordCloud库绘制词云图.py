"""
1.读取内容、
2.使用jieba分词，cut（）函数
3.wordcloud库绘制云图

还可以绘制特定形状的词云图。
"""
import  jieba
from wordcloud import WordCloud
from PIL import Image
import  numpy as np

report = open('信托行业报告.txt','r').read()

words = jieba.cut(report)

report_words = []
for  word in words:
    if len(word)>=4:
        report_words.append(word)
print(report_words)
# 指定形状图片的路径
background_pic = '微博.jpg'
# 打开图片
images = Image.open(background_pic)
# 将图片转为数值数组
maskImages = np.array(images)
content = ' '.join(set(report_words))
wc =  WordCloud(font_path='simhei.ttf',background_color='white',width=1000,height=600,mask=maskImages).generate(content)
# 导出图片
wc.to_file("词云图_自定义图片2.png")

