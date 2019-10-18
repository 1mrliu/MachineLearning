# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/18 4:18 PM'
import re

# 拆分字符串
def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[, 。，.]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

def main1():
    sentence = '你Y是傻叉吗？我操你大爷的。Fuck you.'
    purified = re.sub('[[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔]]', '*', sentence, flags=re.IGNORECASE)
    print(purified)

if __name__ == '__main__':
    main1()