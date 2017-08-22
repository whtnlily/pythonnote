#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Wif(object):

    # __slots__ = ('name','score','__level','__xvalue')     #该属性是限制该类支持的属性名

    '''
    __init__相当于构造函数，如果没有该函数，则有个默认无参数的构造函数，
    如果有该函数，则自动覆盖无参的构造函数。
    '''
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %d: %s' % (self.name,self.score,self.__level)

    def setYD(self,level):
        self.__level = level

    def getYD(self):
        print 'her YD is : %s' % self.__level

    def getName(self):
        return self.name

    @property           #把一个getter方法变成属性，只需要加上@property就可以了
    def tengw(self):
        return self.__tengw

    @tengw.setter       #@tengw.setter，负责把一个setter方法变成属性赋值
    def tengw(self,tengw):
        if not isinstance(tengw,int):
            raise ValueError('tengx must int')
        if tengw < 90 or tengw > 150:
            raise ValueError('tengx is too small or too big')
        self.__tengw = tengw

    def __str__(self):  #相当于java中的toString方法
        return 'name:%s,score:%d,tengw:%d,level:%s' % (self.name,self.score,self.__tengw,self.__level)

    __repr__ = __str__









