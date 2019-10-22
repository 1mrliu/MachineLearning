# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/22 2:30 PM'

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长是：%f' %(a+b+c))
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    print('面积是：%f'%(area))
else:
    print('不能构成三角形')