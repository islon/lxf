# -*- coding: utf-8 -*-

import os

#遍历当前文件夹的文件
#if 文件，打印位置
#else 文件夹，递归


def search(fullpath,key):
	for name in os.listdir(fullpath):
		Nfullpath=os.path.join(fullpath,name)
		if os.path.isfile(Nfullpath):
			if key in os.path.split(Nfullpath)[0]:
				print "%s is file contain %s"%(Nfullpath,key)
			else:
				print "%s is file#############################"%Nfullpath
		else:
			search(Nfullpath,key)
			
search('I:\\python','test')