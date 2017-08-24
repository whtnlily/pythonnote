#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stu(object):
    def setName(self,name):
        self.__name = name

    def setScore(self,socre):
        self.__socre = socre

    def toString(self):
        return 'stu name:%s | socre:%d' % (self.__name,self.__socre)