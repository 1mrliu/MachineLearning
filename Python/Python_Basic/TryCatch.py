# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/7/3 10:49 PM'


try:
    print('try...')
    # r = 10/0
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('no error')
finally:
    print('finally...')
print('End')