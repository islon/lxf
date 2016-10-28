# -*- coding: utf-8 -*-

import os

#操作系统的名字，window为NT
print os.name

#列出所有环境变量的值，显示为dict
print os.environ

#列出环境变量的值
print 'getenv:',os.getenv('OS')

#查看绝对路径
print os.path.abspath('.')

#合并为一个路径
print os.path.join('I:/python/txt','newtxt')

# print os.mkdir('I:/python/txt/newtxt','.txt')

#分类出文件路径+文件名称
print os.path.split('I:/python/txt/newtxt.txt')

#分裂出文件+后缀
print os.path.splitext('I:/python/txt/newtxt.txt')

#列出所有的目录
print [x for x in os.listdir('I:/python/.') if os.path.isdir(x)]

#列出所有后缀为.py的文件
print [x for x in os.listdir('I:/python/.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']