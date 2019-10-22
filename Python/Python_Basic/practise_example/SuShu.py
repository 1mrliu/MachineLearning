# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/22 2:39 PM'

from math import sqrt
"""
判断一个正整数是不是素数
*** 素数指的是只能被1和自身整除的大于1的整数
"""

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))

is_prime = True
for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
