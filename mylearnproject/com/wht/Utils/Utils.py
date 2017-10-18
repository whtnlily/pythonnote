# -*- coding: utf-8 -*-
import codecs
import os
import shutil

import sys
import types


def myprint():
    print '==============='


"""
文件操作
params: 
path 文件路径
type 读写权限
isdelspace 是否删除空行
"""
def readFile(path, isdelspace=False):
    linelist = []
    # with open(path,type) as f:    #这里不使用codecs，则在line.strip()后面需要手动转码
    with codecs.open(path, 'r', 'utf-8') as f:  # 使用codecs，自动转码
        i = 0
        for line in f.readlines():
            # python中的list,添加元素可以用append或者insert
            # linelist.append((line.strip()).decode('gbk').encode("utf-8"))   #中文转码问题)
            if isdelspace:
                if line == '\r\n' or "" == line:  # 去掉空行
                    pass
                else:
                    linelist.append(line.strip())
            else:
                linelist.append(line.strip())
            i += 1
        return linelist


"""
写文件
param: 
path 文件路径
content 追加内容
isdelspace 是否去掉空行
"""


def writeFile(path, content, isdelspace=False):
    if isdelspace:
        # 1、先备份
        newPath = '%s%s' % (path, '.new')
        shutil.copy(path, newPath)
        # 2、重写文件
        with open(newPath, 'w') as f:  # 'w'表示覆盖写
            linelist = readFile(path, isdelspace)
            for line in linelist:
                f.write('%s\n' % line.encode("utf-8"))
            f.write('%s\n' % content)
        # 3、覆盖旧文件
        shutil.move(newPath, path)
    else:
        with open(path, 'a') as f:  # 'a'表示追加写
            f.write('\n%s' % content)


"""
替换文件中的指定的字符串
file_path : 文件路径
old_str ：需要替换的字符串
new_str ：新字符串
"""


def replace(file_path, old_str, new_str):
    if not os.path.exists(file_path):
        print '文件路径不存在'
        return
    with open(file_path, 'r+') as f:
        all_lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_lines:
            line = line.replace(old_str, new_str)
            f.write(line)
        f.close()


"""
在文件的指定行插入内容
file_path:文件路径
line_num:指定行数
content:插入内容
"""


def submitcontent(file_path, line_num, content):
    if not (type(line_num) is types.IntType):
        print "参数类型不正确，行数必须为整数"
        raise TypeError("参数类型不正确，行数必须为整数")
        return
    if not os.path.exists(file_path):
        print '文件路径不存在'
        return

    with open(file_path, 'r+') as f:
        f = file(file_path)
        s = f.read()
        f.close()
        a = s.split('\n')
        a.insert(line_num, content)  # 在第几行插入
        s = '\n'.join(a)
        fp = file(file_path, 'w')
        fp.write(s)
        fp.close()


'''
查找文件中的某一行的内容的行数
filepath：文件路径
content:要查找的内容，字符串
返回行数
'''
def findContentIndex(filepath, content):
    with open(filepath, 'r+') as f:
        allLines = f.readlines()
        i = 0  # 文件行数从1开始
        isContainer = False
        for line in allLines:
            i = i + 1
            if line.strip() == content:
                isContainer = True
                break

        if not isContainer:
            i = -1

        return i


'''
字符串拼接
content:原字符串
appendstr:拼接字符串
'''


def strappend(content, appendstr):
    str = content % appendstr

    return str


'''
拷贝文件到指定目录
sourceFilePath:源文件路径
desFilePath ：目的路径
'''


def copyfile(sourceFilePath, desFilePath):
    try:
        if not os.path.exists(sourceFilePath) or not sourceFilePath.strip():
            print "源文件不存在"
            return
        if not os.path.exists(desFilePath) or not desFilePath.strip():
            print "目的路径不存在"
            return
        shutil.copy(sourceFilePath, desFilePath)
    except Exception:
        print '拷贝文件出错'


def sourcecpy(src, des):
    src = os.path.normpath(src)
    des = os.path.normpath(des)
    if not os.path.exists(src) or not os.path.exists(src):
        print("文件路径不存在")
        sys.exit(1)
    # 获得原始目录中所有的文件，并拼接每个文件的绝对路径
    os.chdir(src)
    src_file = [os.path.join(src, file) for file in os.listdir()]
    for source in src_file:
        # 若是文件
        if os.path.isfile(source):
            shutil.copy(source, des)  # 第一个参数是文件，第二个参数目录
        # 若是目录
        if os.path.isdir(source):
            p, src_name = os.path.split(source)
            des = os.path.join(des, src_name)
            shutil.copytree(source, des)  # 第一个参数是目录，第二个参数也是目录


'''
s为字符串
s.isalnum() 所有字符都是数字或者字母
s.isalpha() 所有字符都是字母
s.isdigit() 所有字符都是数字
s.islower() 所有字符都是小写
s.isupper() 所有字符都是大写
s.istitle() 所有单词都是首字母大写，像标题
s.isspace() 所有字符都是空白字符、\t、\n、\r
'''

'''
清空某个文件夹下的所有文件
'''


def clearDirtree(filepath):
    if not os.path.exists(filepath):
        print '文件路径不存在'
        return
    shutil.rmtree(filepath)  # 先删除在创建目录的原因是：防止文件夹下面的文件被占用抛错的问题
    os.mkdir(filepath)
    # shutil.move('原文件夹/原文件名', '目标文件夹/目标文件名')  #把一个文件从一个文件夹移动到另一个文件夹，并同时重命名


def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text.strip()
