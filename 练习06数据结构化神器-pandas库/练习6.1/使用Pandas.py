#创建DataFrame

import  pandas as pd

a = pd.DataFrame([[1,2],[3,4],[5,6]],columns=['data','score'],index=['A','B','C'])
print(a)
# 查看列索引
print(a.columns)
# 修改列索引
a.columns = ['日期','分数']
print(a)

b = pd.DataFrame()
date1 = [1,3, 5]
score1 = [2,4,6]
b['data'] = date1
b['score'] = score1
print(b)


# 通过字典创建DataFrame
c = pd.DataFrame({'data':[1,2,3],'score':[3,4,5]})
print(c)