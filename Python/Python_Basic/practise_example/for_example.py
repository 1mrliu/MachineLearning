# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/22 2:35 PM'

"""
用 for循环实现1——100之间偶数的求和
"""
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

"""
用for求1-100的所有和
"""
sum = 0
for x in range(101):
    sum += x
print(sum)