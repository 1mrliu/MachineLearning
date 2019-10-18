# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/18 8:47 PM'

"""
设计一个函数返回传入的列表中最大和第二大的元素的值
"""
def max2(x):
    x = sorted(x)
    print(x[0], x[1])

def max2_(x):
    """

    :param x: 输入的列表
    :return: 返回第一大 和 第二大的值
    """
    m1, m2 = (x[0], x[1]) if x[0]>x[1] else (x[1], x[0])
    for index in range(2,len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    print(m1, m2)




if __name__ == '__main__':
    max2_([4,2,1,5,3])