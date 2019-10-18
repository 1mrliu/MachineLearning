# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/18 8:25 PM'
import os
import time
"""
实现跑马灯的输出效果
"""
def main():
    content = '北京欢迎你为你开天辟地。。。'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()