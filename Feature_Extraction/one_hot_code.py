# _*_ coding:utf-8 _*_

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

'''
对离散型数据的处理方式 
例如：sex（male female） 可以使用LabelEncoder转化为数值型
再使用OneHotEncoder转化为0 1编码

'''

data =  pd.read_csv('D:/Users/sangfor/Desktop/train.csv')
print(data.describe())

print(data['Sex'].value_counts())
dummies = pd.get_dummies(data['Sex'])
print(dummies.head())
# 1.LabelEncoder将字符型的数据专户为数值型变量，然后使用OneHotEncoder进行编码
one_hot_1 = LabelEncoder().fit_transform(data['Sex'])
one_hot_2 = OneHotEncoder(sparse=False).fit_transform(one_hot_1.reshape((-1,1)))
print(one_hot_1)
print(one_hot_2)

'''
one_hot_1:LabelEncoder的输出结果
[1 0 0 0 1 1 1 1 0 0 0 0 1 1 0 0 1 1 0 0 1 1 0 1 0 0 1 1 0 1 1 0 0 1 1 1 1
 1 0 0 0 0 1 0 0 1 1 0 1 0 1 1 0 0 1 1 0 1 0 1 1 0 1 1 1 1 0 1 0 1 1 0 1 1
 1 1 1 1 1 0 1 1 0 1 0 0 1 1 0 1 1 1 1 1 1 1 1 1 0 1 0 1 1 1 1 1 0 1 1 0 1
 0 1 0 0 1 1 1 1 0 1 1 1 0 1 1 1 1 0 1 1 1 0 0 1 1 0 1 1 1 0 0 0 1 1 1 1 0
...
 1 1 0 1 1 1 0 1 1 0 1 1 1 1 1 0 0 1 1 1 1 0 1 1 1 1 1 1 0 1 1 1 1 1 1 0 1
 1 0 0 0 0 0 1 0 1 1 1 0 0 1 0 0 1 1 1 1 0 1 1 0 0 1 1 1 0 0 1 0 1 1 0 1 0
 0 1 1]
one_hot_2:OneHotEncoder的输出结果
[[0. 1.]
 [1. 0.]
 [1. 0.]
 ...
 [1. 0.]
 [0. 1.]
 [0. 1.]]
'''