# -*- coding: utf-8 -*-
__author__ = 'liudong'
__date__ = '2018/10/14 8:00 PM'

class Me(object):
    def __init__(self,name,hobby):
        self.name = name
        self.hobby = hobby
    # def __str__(self):
    #     return ('__str__():'+self.name+' '+self.hobby)
    def __repr__(self):
        return ('__repr__():'+ self.name + ' '+ self.hobby)


if __name__ == "__main__":
    me = Me('liudong','game')
    
    print(me)
    name =  'Alice ll jjk kk ds hhn'
    last = name.split()
    print(last)

    girls = ['alice', 'bernice', 'clarice']
    boys =  ['chris','arnold','bob']
    letterGirls = {}
    for girl in girls:
        letterGirls.setdefault(girl[0], []).append(girl)
        print(letterGirls)
    print(b+'+'+g for b in boys for g in letterGirls[b[0]])
    exec("print('Hello !')")
    print([i for i in range(8)])
    # zip
    nums = [1,2,3]
    chars = ['a','b','c','d']
    for i , j in zip(nums,chars):
        print(i,j)
        print()