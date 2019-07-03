#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/7/3 10:04 PM'
# Python字符串的操作
'''
字符	 ASCII	    Unicode	            UTF-8
A	 01000001	00000000 01000001	01000001
中	 x	        01001110 00101101	11100100 10111000 10101101
Unicode 常见的编码是两个字节表示一个字符
Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
'''

# ord()获取字符的整数表示
print(ord('A'))
print(ord('中'))

# chr()把编码转化为对应的字符
print(chr(66))
print(chr(25991))

# encode()方法可以编码为指定的bytes类型
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

# 计算str包含多少个字符，可以用len()函数
print(len('ABC'))
print(len('中文'))
# 如果换成bytes，len()函数就计算字节数
print(len(b'ABC'))
print(len('中文'.encode('utf-8')))

# format()格式化的写法
print('Hello {}, grow {:.1f} %'.format('alice', 12.122))
print('Hello {}, grow {:.2f} %'.format('alice', 12.122))