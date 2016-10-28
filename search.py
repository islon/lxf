 # -*- coding: utf-8 -*-
import os
#def search(x):
	#匹配x在不在文件名中
	#假如在，获取当前文件绝对路径
	#合并绝对路径+文件名
print [x for x in os.listdir('I:/python/search/py/.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print 'end'
	