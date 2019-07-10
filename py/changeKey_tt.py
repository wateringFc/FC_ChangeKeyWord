#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


#文件名列表
filelist = ['Change_Constant.h', 'Change_Constant.m']
#原关键字
src_keywords = ['_k', 'NEW']
#新关键字
dest_keywords = ['_s', 'FC']


def main():
    for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        if filename in filelist:
        #获得文件相对路径
                filepath = os.path.join(dirpath, filename)
                #print 'filepath: ' + filepath
                change_keywords(filepath, src_keywords ,dest_keywords)


def change_keywords(filepath, src_keywords, dest_keywords):
    content_old = open(filepath, 'r')
    content_new = ''
    code_list = content_old.readlines()
    for code in code_list:
    i = 0
        for i in range(len(src_keywords)): 
            code = code.replace(src_keywords[i], dest_keywords[i])
            i += 1  
            print  'change to: ' + code
        #生成新的文件内容
        content_new += code
    content_old.close()
    #写入源文件并保存
    file_new = open(filepath, 'w')
    file_new.writelines(content_new)
    file_new.close()


main()