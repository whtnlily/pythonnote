# -*- coding: utf-8 -*-
import codecs
import shutil

def myprint():
    print '==============='

"""
文件操作
params: 
path 文件路径
type 读写权限
isdelspace 是否删除空行
"""
def readFile(path,isdelspace=False):
    linelist = []
    # with open(path,type) as f:    #这里不使用codecs，则在line.strip()后面需要手动转码
    with codecs.open(path,'r','utf-8') as f: # 使用codecs，自动转码
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
        newPath = '%s%s' % (path,'.new')
        shutil.copy(path, newPath)
        # 2、重写文件
        with open(newPath, 'w') as f:   # 'w'表示覆盖写
            linelist = readFile(path, isdelspace)
            for line in linelist:
                f.write('%s\n' % line.encode("utf-8"))
            f.write('%s\n' % content)
        # 3、覆盖旧文件
        shutil.move(newPath, path)
    else:
        with open(path,'a') as f:   # 'a'表示追加写
            f.write('\n%s' % content)
























