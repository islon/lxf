# -*- coding: utf-8 -*-

import os

def search(fullpath,key):
	for name in os.listdir(fullpath):
		Nfullpath=os.path.join(fullpath,name)
		if os.path.isfile(Nfullpath):
			if key in name:
				print "%s is file contain %s"%(Nfullpath,key)
			else:
				print "%s is file,but not contain %s"%(Nfullpath,key)
		else:
			search(Nfullpath,key)
			


if __name__ == "__main__":
	keyword=raw_input("Please input the keyword:")
	search('D:\\python\\lxf\\search',keyword)
	#路径替换成你自己的电脑路径，注意\\双斜杠
	
	
#遍历当前文件夹的文件
#if 文件，打印位置
#else 文件夹，递归