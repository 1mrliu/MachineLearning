# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/18 8:38 PM'

def get_file_suffix(filename, has_dot=False):
    """
    获取文件的后缀名
    :param filename: 文件名
    :param has_dot: 返回的文件名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.find('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

if __name__ == '__main__':
    print(get_file_suffix("dsafdsfghjd.sdad", True))
