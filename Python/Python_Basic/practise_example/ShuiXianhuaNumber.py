# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/22 3:10 PM'

"""
水仙花数 是一个三位数，满足每个位上数字的立方之和等于它本身
"""
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10 # //代表向下取整
    high = num // 100
    if num == low **3 + mid ** 3 + high **3:
        print(num)