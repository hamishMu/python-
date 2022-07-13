"""
pandas库可以从多种类型的数据文件中读取文件，
并可以将数据写入文件中。
"""
import  pandas as pd
import  xlrd
data = pd.read_excel('data.xlsx')
print(data)