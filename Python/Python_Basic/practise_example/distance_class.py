# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/22 4:47 PM'
"""
定义一个类描述平面上的点并提供移动点和计算到另外一个点距离的方法
"""
from math import sqrt

class Point():
    def __init__(self, x, y):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return:
        """
        self.x = x
        self.y = y


    def move_by(self, dx, dy):
        """
        移动一定的距离
        :param dx: 横坐标的增量
        :param dy: 纵坐标的增量
        :return:
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算与另外一个点的距离
        :param other:
        :return:
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx **2 + dy**2)

    def __str__(self):
        return '{},{}'.format(str(self.x), str(self.y))

def main():
    p1 = Point(3,5)
    p2 = Point(0,0)
    print('p1:',p1)
    print('p2:',p2)
    p2.move_by(-1, 2)
    print('move p2:',p2)
    print('p1 p2 distance:', p1.distance_to(p2))


if __name__ == '__main__':
    main()

