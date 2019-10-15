# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/15 8:05 PM'

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