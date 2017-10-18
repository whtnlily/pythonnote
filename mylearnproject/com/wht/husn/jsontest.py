#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import json

import sys

jsonPath = 'D:\\temp\\tep\\100000841_product.json'

if __name__ == '__main__':
    print 'json test'
    with codecs.open(jsonPath, 'r', 'utf-8') as f:
        linelist = []
        for line in f.readlines():
            if line == '\r\n' or "" == line:  # 去掉空行
                pass
            else:
                linelist.append(line.strip())

        jsonStr = ''
        if not len(linelist):
            print 'skill config file is null'
        else:
            jsonStr = ''.join(linelist)

        print '==<<>>== jsonStr:%s' % jsonStr
        skillJson = json.loads(jsonStr)
        skills = skillJson['skills']   # list []
        print 'skills type:%s'  % type(skills)  # list [ ]   要用
        print 'skills[2] type:%s' % type(skills[2])   # dict { }
        print 'tasks type:%s' % type(skills[2]['tasks'])   # list []
        print 'intents type:%s' % type(skills[2]['tasks'][0]['intents'])  # list []
        print 'intents[5] type:%s' % type(skills[2]['tasks'][0]['intents'][5])  # dict { }
        print 'output type:%s' % type(skills[2]['tasks'][0]['intents'][5]['output'])  # dict { }
        print 'responses type:%s' % type(skills[2]['tasks'][0]['intents'][5]['output']['responses'])  # list []
        print 'responses[0] type:%s' % type(skills[2]['tasks'][0]['intents'][5]['output']['responses'][0])  # dict { }
        print 'command type:%s' % type(skills[2]['tasks'][0]['intents'][5]['output']['responses'][0]['command'])  # 字符串  unicode
        # skills[2]['tasks'][0]['intents'][5]['output']['responses'][0]['command']  #获取指令
        '''
        需要保存的skill的数据格式(dict，value是另外一个dict)
        { 'skillid1':{'skillname':'xxx','command前缀':'xxx','command列表':['cmd1','cmd2','cmd3']},'skillid2':{...},'skillid3':{...},'skillid4':{...},'skillid5':{...}.'skillid6':{...} }
        commandDomain
        '''
        skillsDict = {}  #存放最终skill-value的dict，这个主要用于聚合到DEMO工程中。格式如上
        skillsValueDict = {}  # 存放最终skill-value的dict中的value对应的dict。格式如：{'skillname':'xxx','command前缀':'xxx','command列表':['cmd1','cmd2','cmd3']}
        skillsCommandList = []  #存放最终结果的指令集合，格式如下：['cmd1','cmd2','cmd3']
        commandDomain = ''
        for i, sk in enumerate(skills):
            # 先清空commandlist 指令集合
            skillsCommandList = []

            # 清空value集合
            skillsValueDict = {}
            skillsDictTemp = skills[i]  # dict { }
            skillId = skillsDictTemp['skillId']
            skillName = skillsDictTemp['skillName']
            # 3、添加skill名称
            skillsValueDict['skillName'] = skillName.encode('utf8')    # .encode('unicode-escape').decode('string_escape')
            print '==1== id:%s, skillId:%s,skillName:%s' % (i,skillId,skillName)
            tasksListTemp = skillsDictTemp['tasks']   # list []
            for j,task in enumerate(tasksListTemp): # task is dict
                print '==2== task :%s' % task
                intentListTemp = task['intents']   # list []
                print '==2== id:%s, task:%s' % (j, intentListTemp)
                for m,intent in enumerate(intentListTemp):  # intent is dict
                    print '==3== intent:%s' % intent   # intent is dict
                    responseListTemp = intent['output']['responses']
                    print '==3== id:%s, response:%s' % (m, responseListTemp)
                    for n,response in enumerate(responseListTemp):  # response is dict
                        commandTemp = response['command']
                        print '==4== id:%s, command:%s' % (n, commandTemp)
                        if '?' in commandTemp:  # 判断command是否含有?
                            command = commandTemp.split('?')[0].encode('unicode_escape').strip()   # 取?前面的字段
                        else:
                            command = commandTemp.encode('unicode_escape').strip()

                        print '==4== id:%s, command2:%s' % (n, command)
                        if not command:
                            pass
                        else:
                            skillsCommandList.append(command.encode('unicode_escape'))

                # 组合skillsDict
                # 1、添加指令集合
                if not len(skillsCommandList):  # 列表为空
                    continue
                else:
                    skillsValueDict['commandList'] = skillsCommandList

                # 2、添加指令的前缀
                if '.' in skillsCommandList[0]:  # 指令是否以'.'分隔
                    commandDomain = skillsCommandList[0].split('.')[0]  # 取指令的第一个字段作为领域划分
                    skillsValueDict['commandDomain'] = commandDomain.encode('unicode_escape')   #取指令的第一个字段作为领域划分

            # 4、以skillId为key,以skillsValueDict为value，添加到skillDict中
            skillsDict[skillId] = skillsValueDict  # ok


        for p,skill in skillsDict.items():
            print '==> skillid:%s | value:%s' % (p,skill)

        print sys.getdefaultencoding()