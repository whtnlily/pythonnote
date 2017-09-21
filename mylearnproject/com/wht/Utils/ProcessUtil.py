#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
多进程工具类
"""
import os
from multiprocessing import Process
from multiprocessing import Pool


def creatProcess(fun,args):

    """
    创建子进程
    :param fun: 子进程需要执行的函数
    :param args: 子进程需要执行的函数的参数，list元组（arg1,arg2,）
    :return: 返回子进程
    """
    thread_p = Process(target=fun,args=args)

    return thread_p
