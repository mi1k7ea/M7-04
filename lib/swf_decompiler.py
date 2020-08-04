# coding=utf-8

import os

# 必须进入asdec子目录中执行，原因是asdec.jar依赖的jar包是以绝对路径加载的
def decompile_swf(path):
    asdec_dir = os.getcwd() + "/asdec/"
    command = 'cd /d ' + asdec_dir + '&& java -jar asdec.jar -export as "../tmp/" ' + path
    os.system(command)
