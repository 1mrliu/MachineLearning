# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2019/10/22 3:23 PM'
"""
两枚骰子 摇骰子进行游戏
规则：
 玩家第一次摇骰子如果摇到7点或者11点，玩家胜
 玩家如果第一次摇出2点、3点、12点，庄家胜
 其他的点数继续摇骰子，如果玩家摇出7点，庄家胜，如果摇出了第一次摇出的点，玩家胜。其他点数玩家继续摇骰子
"""
from random import randint

money = 1000
while money > 0:
    print('总资产是',money)
    needs_go_on = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = randint(1,6) + randint(1,6)
    print('玩家摇出了 %d 点' %first)
    if first == 7 or first == 11:
        print("玩家胜")
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print("庄家胜")
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1,6) + randint(1,6)
        print("玩家摇出了%d点" %current)
        if current == 7:
            print("庄家胜")
            money -= debt
        elif current == first:
            print("玩家胜")
            money += debt
        else:
            needs_go_on = True
print("你破产了")