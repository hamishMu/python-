"""
mkdir 单个目录
makedirs 创建多个目录

文件的相对路径和绝对路径
相对路径就是代码文件所在的文件夹。其中"./"表示同级文件夹
绝对路径就是文件的完整路径。

"""
import os

try:
    if not os.path.exists('D:/爬虫/data'):
        os.makedirs("D:/爬虫/data")
    else:
        with open("D:/爬虫/data/test.txt", 'a+')as f:
            f.write("测试测试！")
except Exception as e:
    print("Error: 没有找到文件或读取文件失败")
finally:
    print("程序结束")
