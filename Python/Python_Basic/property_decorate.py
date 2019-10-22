# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/22 5:12 PM'
"""
装饰器的使用 
@property
Python中的属性和方法的权限问题，不建议使用私有
可以使用@property包装getter和setter方法，是的对属性的访问既安全又方便
"""
class Person():
    def __init__(self, name, age):
        """
        初始化方法
        :param name: 姓名
        :param age: 年龄
        """
        self._name = name
        self._age = age

    # 访问器- getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name


    def play(self):
        if self._age <= 16:
            print("little age::",self._name)
        else:
            print("age old")


def main():
    person = Person('lll', 12)
    person.play()
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()
