# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/22 8:30 PM'
"""
使用继承实现的奥特曼打小怪兽的游戏
"""
from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(metaclass=ABCMeta):
    """战斗者 """

    # 使用__slots__魔法限定对象可以绑定的成员变量 只对当前类的对象生效，对子类不起任何作用
    __slots__ = ('_name', '_hp')
    def __init__(self, name, hp):
        """
        初始化
        :param name: 姓名
        :param age: 年龄
        """
        self._name = name
        self._hp = hp


    @property
    def name(self):
        return self._name


    @property
    def hp(self):
        return self._hp


    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0


    @property
    def alive(self):
        return self._hp > 0


    @staticmethod
    def attack(self, other):
        """

        :param self:
        :param other: 被攻击的对象
        :return:
        """
        pass

class Ultraman(Fighter):
    """奥特曼"""
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """
        初始化方法
        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        """
        super(Ultraman,self).__init__(name,hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15,25)

    def huge_attack(self, other):
        """
        必杀技
        :param other:
        :return:
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            return False


    def magic_attack(self, others):
        """
        魔法攻击
        :param others: 被攻击的群体
        :return: 使用魔法攻击成功就返回True 否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for item in others:
                if item.alive:
                    item.hp -= randint(10,15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1,10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '---{}奥特曼\n---生命值:{}\n---魔法值:{}'.format(self._name,self._hp,self._mp)


class Monster(Fighter):
    """怪兽"""
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10,20)
    def __str__(self):
        return '---{}怪兽\n---生命值{}'.format(self._name,self._hp)


def is_any_alive(monsters):
    """判断是是否有存活的"""
    for monster in monsters:
        if monster.alive > 0:
            return True
        else:
            return False

def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('卤蛋', 1000, 120)
    m1 = Monster('王大锤',250)
    m2 = Monster('李元芳',500)
    m3 = Monster('犀利哥',750)
    ms = [m1,m2,m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('第{}回合\n'.format(fight_round))
        m = select_alive_one(ms)
        skill = randint(1,10)
        if skill <= 6:
            print('{}普通攻击{}'.format(u.name,m.name))
            u.attack(m)
            print('{}的魔法值恢复了{}'.format(u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('{}使用魔法攻击'.format(u.name))
            else:
                print('{}使用魔法攻击失败'.format(u.name))
        else:
            if u.huge_attack(m):
                print('{}使用必杀技{}'.format(u.name,m.name))
            else:
                print('{}使用普通攻击打了{}'.format(u.name,m.name))
                print('{}的魔法值恢复了{}'.format(u.name, u.resume()))
        if m.alive > 0:
            print('{}回击了{}'.format(m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
        print('\n')
    print('---战斗结束---')
    if u.alive > 0:
        print('{}奥特曼胜利！'.format(u.name))
    else:
        print('小怪兽胜利！')

if __name__ == '__main__':
    main()




