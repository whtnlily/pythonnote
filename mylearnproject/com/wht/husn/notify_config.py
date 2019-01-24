#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Just for clone and pull code

import os
import sys
import shutil
import codecs


PRODUCT_ID = "K_PRODUCT_ID"
ALIAS_KEY = "K_ALIAS_KEY"
API_KEY = "K_API_KEY"
PICKUP_MODE = "pickup_mode"


def notify(file,content):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param file: 文件路径
    :param new_str: 替换的字符串
    :return: None
    """
    with codecs.open(file, "r", encoding="utf-8") as f1,codecs.open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            if line.find(PRODUCT_ID) >= 0:
                if "Default" != content[PRODUCT_ID] and "" != content[PRODUCT_ID]:
                    line = line.replace(line, content[PRODUCT_ID])
            if line.find(ALIAS_KEY) >= 0:
                if "Default" != content[ALIAS_KEY] and "" != content[ALIAS_KEY]:
                    line = line.replace(line, content[ALIAS_KEY])
            if line.find(API_KEY) >= 0:
                if "Default" != content[API_KEY] and "" != content[API_KEY]:
                    line = line.replace(line, content[API_KEY])
            if line.find(PICKUP_MODE) >= 0:
                if "Default" != content[PICKUP_MODE] and "" != content[PICKUP_MODE]:
                    line = line.replace(line, content[PICKUP_MODE])
            f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)

if __name__ == '__main__':
    print 'notify config.propertites'
    #参数1：产品ID 参数2：分支号  参数3：apiKey 参数4：拾音方式
    product_id = sys.argv[1].strip()
    alias_key = sys.argv[2].strip()
    api_key = sys.argv[3].strip()
    pickup_mode = sys.argv[4].strip()
    params = {PRODUCT_ID:"",ALIAS_KEY:"",API_KEY:"",PICKUP_MODE:""}

    if ("Default" == product_id or "" == product_id) and ("Default" == alias_key or "" == alias_key) and ("Default" == api_key or "" == api_key) and ("Default" == pickup_mode or "" == pickup_mode):
        print "params all is Default"
    else:
        config_path = os.path.abspath('.//tvui_tv//src//main//assets//config.properties')
        # config_path = os.path.abspath('E:\\workspace\\v3-190123\\tvui-v3\\tvui_tv\\src\\main\\assets\\config.properties')
        if "Default" != product_id and "" != product_id:
            prodcut_id_value = PRODUCT_ID + " = " + product_id + "\n"
            params[PRODUCT_ID] = prodcut_id_value
        if "Default" != alias_key and "" != alias_key:
            alias_key_value = ALIAS_KEY + " = " + alias_key + "\n"
            params[ALIAS_KEY]=alias_key_value
        if "Default" != api_key and "" != api_key:
            api_key_value = API_KEY + " = " + api_key + "\n"
            params[API_KEY]=api_key_value
        if "Default" != pickup_mode and "" != pickup_mode:
            pickup_mode_value = PICKUP_MODE + " = " + pickup_mode + "\n"
            params[PICKUP_MODE]=pickup_mode_value

        notify(config_path,params)







