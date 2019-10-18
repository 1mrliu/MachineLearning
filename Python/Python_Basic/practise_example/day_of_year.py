# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/18 9:06 PM'
"""
计算指定的年月日是这一年的第几天
"""

def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    :param year: 输入指定的年份
    :return: 返回True表示是闰年，False表示不是闰年
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, date):
    """
    计算传入的这个日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31,28,31,30,31,30,31,31,30,31,30,31], # 平年二月28天
        [31,29,31,30,31,30,31,31,30,31,30,31]  # 闰年二月29天
        ][is_leap_year(year)] # 是闰年的话是1 代表第二个list  平年是 0 代表第一个list
    total = 0
    for index in range(month-1):
        total += days_of_month[index]
    return total + date

def main():
    print(which_day(1980, 11,20))


if __name__ == '__main__':
    main()




