#!/usr/bin/env python
# -*- coding: utf-8 -*-

'learn note'
__author__ = 'hyman.wan'
# 学习笔记
from com.wht.Utils import Utils
from collections import Iterable
import math
import functools
from com.wht.husn.bean import Wif
from com.wht.husn.bean import Student
from types import MethodType
import sys

print ord('A')

Utils.myprint()

# 列表list , python中的list相当于java中的数组。list中的元素可以是另外一个list。list用[ ]
# list的元素可以被修改
mywifis = ['husn', 'sunjj', 'gongyl', 'huyy', 'liut']
for wife in mywifis:
    print 'I love ' + wife
mywifis[1] = 'caim'

Utils.myprint()

mywifis.append('zhouyp')
for wife in mywifis:
    print 'I love ' + wife

Utils.myprint()
# tuple，元组，用（ ），元组中的元素可以是List，也可以是另外一个元组。
# 元组一旦确定，就不能修改。并且在定义的时候，元素就必须确定下来
tup = ('husn', 'sunjj', 'gongyl')
for tem in tup:
    print 'i love ' + tem

Utils.myprint()
formatstr = '%02d-%02d' % (3, 1)
print('formatstr:' + formatstr)

Utils.myprint()
formatstrs = 'Hi,%s,you have $%d' % ('husn', 99999999999999)
print(formatstrs, len(formatstrs))
Utils.myprint()

# 条件语句
age = 3  # int(raw_input())    ##input()       # raw_input()接收输入,返回的是字符串，可以用int()进行强转；input()也可接收输入，但返回的内容可以根据输入的内容自行判断类型
if age >= 18:  # lua 的if语句格式是 if true then: ..... end
    print 'your age is:', age, 'you are adult'
else:
    print 'your age is:', age, "you are teenager"

Utils.myprint()

sum = 0
for x in range(101):
    sum = sum + x
print 'sum:', sum  # 在python中，可以用'sum:'+sum 类型，但是sum变量必须是字符串，也就是说+只能用在字符串拼接。','相当于空格
Utils.myprint()

# dict 字典，相当于java中的map，键值对，用{ } 表示
# 遍历是要用items()函数。取元素，用[]或者get()函数
mylovewifs = {'husn': 98, 'gongyl': 90, 'liut': 86, 'zhouyp': 80, 'sunjj': 70, 'dingx': 85, 'chenzy': 83, 'caim': 90,
              'huyy': 90}
for k, v in mylovewifs.items():
    print 'name:%s,level:%d' % (k, v)
print 'my loveset leve:', mylovewifs['husn']
Utils.myprint()
for key in mylovewifs:
    print 'my love name:', key
Utils.myprint()
for value in mylovewifs:
    print 'my love level:', mylovewifs.get(value)
Utils.myprint()

# set : 无序，元素不能重复的列表，用()表示，必须用一个list作为输入集合。与List的区别就是，list是有序的，元素可重复的
settest = set(mywifis)
for w in settest:
    print 'my wf ', w
Utils.myprint()


# 函数定义，函数默认值
def power(x1, n=2):
    if not isinstance(x1, (int, float)):
        raise TypeError('bad operand type')
    s = 1
    while n > 0:
        n = n - 1
        s = s * x1
    return s


fun = power

funtest1 = power(5)
funtest2 = fun(5, 3)
print 'funtest power:', funtest1, funtest2
Utils.myprint()

# 递归函数，尾递归，存在栈溢出问题。所以尽量少用递归函数

# 切片功能，主要针对list
print 'list more-1:', mywifis[-1]  # 倒数第一个
print 'list more-2:', mywifis[-2]  # 倒数第二个
print 'list more0-3:', mywifis[0:3]
print 'list more-2-1:', mywifis[-2:-1]  # 倒数第二个到倒数第一个
print 'list more-3-2:', mywifis[-3:-1]
Utils.myprint()

# 迭代 dict迭代的是key，如果要迭代value，可以用d.itervalues，如果要同时迭代key和value，可以用d.iteritems()
if isinstance(mylovewifs, Iterable):  # 判断该对象是否是迭代对象
    i = 0
    for level in mylovewifs.itervalues():
        i += 1
        print 'itervalues%d:%s' % (i, level)

Utils.myprint()

# enumerate函数的作用：实现类似java中的for循环。带索引值i
for i, name in enumerate(mylovewifs):
    print 'name', i, ':', name

Utils.myprint()

# 列表生成式，主要针对列表list
listcreate = [x * x for x in range(1, 11)]
for ls in listcreate:
    sq = math.sqrt(ls)
    print '%d * %d = %d' % (sq, sq, ls)

Utils.myprint()


# 生成器 迭代器，在python中可以将一个函数修改为迭代器(只要在函数中出现yield关键字，该函数就是迭代器函数)，然后可以用for循环对其进行迭代
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


for g in fib(10):
    print 'generator test:', g

Utils.myprint()

# 高阶函数：即函数本身可以作为参数传入
lev_fun = fib   #函数可以赋值给一个变量
for lf in lev_fun(5):
    print 'lev_test:',lf
Utils.myprint()

def add(x2,y2,f):
    return f(x2)+f(y2)

print('add test:',add(-5,10,abs))   #ads系统自带函数。
Utils.myprint()

'''
内建函数map().高阶函数
map()函数接收两个参数，一个是函数，一个是序列，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
'''
def addstr(name1):
    return 'I fk %s' % name1

for mapkey in map(addstr,mywifis):
    print mapkey
print map(addstr,mywifis)
Utils.myprint()

'''
内建高阶函数reduce
reduce把一个函数作用在一个序列[x1, x2, x3...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
'''
def sum_add(sa,sb):
    return sa * 10 + sb

print ('reduce test:',reduce(sum_add,[1,3,5,7,9]))  #将序列[1,3,5,7,9]变成13579
Utils.myprint()
'''
内建函数filter()
filter()也接收一个函数和一个序列。
和map()不同的时，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素
'''
def is_odd(od):
    return od % 2 == 1

print 'filter test1:',filter(is_odd,[1,2,4,8,9,10])     #删除掉偶数

def not_empty(s):
    '''
    python中的and，从左到右运算，当and左边都为真时，
    才会计算and右边的表达式，并返回右边的表达式
    '''
    return s and s.strip()      # 这里的and的意思是，s存在的情况下，才会计算右边的s.strip()
print 'filter test2:',filter(not_empty,['A','','c','b','','D'])     #去掉空字符串
Utils.myprint()

# sort排序函数
sortlist = [2,50,36,45,89,21]
newsortlist = sorted(sortlist)
print 'sorted1:',newsortlist
newmylist = sorted(mywifis)
print 'sorted2:',newmylist
Utils.myprint()

# 闭包 ：函数的返回值是另一个函数，内部函数可以访问外部函数的参数和局部变量

# 匿名函数，用关键字lambda x : x*x  冒号前面是参数，后面是函数体
def build(x,y):
    return lambda : x*x + y*y   # 冒号前面如果为空，则表示lambda函数不需要参数

lambdaf = build(3,4)
print 'lambda test:',lambdaf()

def build2(x,y):
    return lambda z=1:x*x+y*y+z*z   # 冒号前的参数可以有默认值
lambdaf2 = build2(3,4)
print 'lambda test2:',lambdaf2(2)
Utils.myprint()

# 装饰器 @ ,相当于java中的注解
# *args是非关键字参数，用于元组，**kw是关键字参数，用于字典
# *args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前
def log(func):
    def wrapper(*args,**kw):    #(*args,**kw)表示可以接受任意参数的调用
        print 'call %s():' % func.__name__
        return func(*args,**kw)
    return wrapper

@log        #相当于执行了log(now)
def now():
    print '2017-08-09'

now()
Utils.myprint()

# 偏函数 functools
int2 = functools.partial(int,base=2)
print int2('1000000')
print int2('1000000',base=10)
Utils.myprint()

# *args **kw
def argstest(arg1,arg2='husn',*args):
    print 'arg1:%s' % arg1
    print 'arg2:%s' % arg2
    for i,arg in enumerate(args):
        print '*arg%s:%s' %(i, arg)

argstest('weiy')
Utils.myprint()
argstest('dingx','zuoyq')
Utils.myprint()
argstest('caim','husn','liut','gongyl','huyy')
Utils.myprint()
# **kw
def dicrArgs(kw1,kw2='husn',**kw3):
    print 'kw1:%s' %kw1
    print 'kw2:%s' %kw2
    for k,v in kw3.iteritems():
        print '**kw3 k:%s | v:%s' %(k,v)

dicrArgs('huyy')
Utils.myprint()
dicrArgs('gongyl','caim')
Utils.myprint()
dicrArgs('liut','zuoyq',third='dingx',forth='chenzy')
Utils.myprint()

# 面向对象编程
w1 = Wif.Wif('yangxx', 88)
w1.setYD('jing')
w2 = Wif.Wif('weiy',90)
w2.setYD('song')
w3 = w1             # 这里注意，这里与java不同，这里不是赋值，这里是重命名，w3的值改变了，w1会跟着变
w1.print_score()
w2.print_score()
w3.name = 'sunjj'
w3.score = 70
w3.setYD('song')
w3.print_score()
Utils.myprint()

stu1 = Student.Stu()
stu1.setName('zhangsan')
stu1.setScore(60)
print stu1.toString()
print isinstance(stu1,Student.Stu)  #判断变量的类型
Utils.myprint()

# 面向对象高级编程 动态给类添加属性和方法
def set_xiongw(self,xvalue):
    if not isinstance(xvalue,int):
        raise ValueError('xiongw must int')
    if xvalue < 85 or xvalue > 130:
        raise ValueError('xiongw is too small or too big')
    self.__xvalue = xvalue

def get_xongw(self):
    return self.__xvalue

Wif.Wif.set_xiongw = MethodType(set_xiongw,None,Wif.Wif)    #动态给类添加方法
Wif.Wif.get_xiongw = MethodType(get_xongw,None,Wif.Wif)     #第二个参数如果为None则表示是绑定在类上，如果为具体的对象则表示绑定在具体的对象上
w1.set_xiongw(90)
print w1.print_score(),'xiongw:',w1.get_xiongw()
Utils.myprint()

w2.tengw = 98
print w2.print_score(),'tengw:',w2.tengw
Utils.myprint()

w3.tengw = 100
print w3.__str__()
Utils.myprint()
# python中是允许多继承的
# python中调试代码：print,assert,logging,pdb,pdb.set_trace(),IDE(pycharm)

#文件读写
lovlist = Utils.readFile('E:\\workspace\\pythonproject\\temp\\mynote.txt',True)
for i,lov in enumerate(lovlist):
    print 'lov %s : %s' % (i,lov)
Utils.myprint()

addstr = '我是Hyman.wan。'
Utils.writeFile('E:\\workspace\\pythonproject\\temp\\mynote.txt',addstr,True)
lovlist = Utils.readFile('E:\\workspace\\pythonproject\\temp\\mynote.txt')

for i,lov in enumerate(lovlist):
    print 'lov %s : %s' % (i,lov)
































































































