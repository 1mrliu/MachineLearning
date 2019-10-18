# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/18 8:30 PM'
import random
"""
设计一个函数生成指定长度的验证码，验证码有大小写字母和数字构成
"""
def generate_code(code_len=4):
    """

    :param code_len:
    :return:
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars)-1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    print(generate_code(4))