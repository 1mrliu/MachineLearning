# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/22 4:27 PM'
"""
定义一个类描述数字时钟
"""
from time import sleep
import os

class Clock():
    """
    数字时钟
    """
    def __init__(self, hour=0, minute=0,second=0):
        """

        :param hour:
        :param minute:
        :param second:
        """
        self._hour = hour
        self._minute = minute
        self._second = second


    def run(self):
        """
        走字
        :return:
        """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """
        显示时间
        :return:
        """
        return '{}:{}:{}'.format(self._hour,self._minute,self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        # os.system("clear")
        sleep(1)
        clock.run()


if __name__ == '__main__':
   main()