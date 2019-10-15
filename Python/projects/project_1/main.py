# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/15 5:22 PM'

# 项目1 使用Python 将纯文本的信息转化为带标签的文件
# 使用自动的标签匹配列表进行匹配  纯文本进行标记
import sys
import re

# 文本块生成器
def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

# 标记程序
print('<html><head><title>...</title><body>')
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')

#  调用命令python main.py <wenben.txt> test_output.html