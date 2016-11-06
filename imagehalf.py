# -*- coding: utf-8 -*-
import Image
import os

def foo(fullpath):
	print "******Start******"
	for child in os.listdir(fullpath):
		childpath=os.path.join(fullpath,child)
		if os.path.isfile(childpath):
			childimage=Image.open(childpath)
			w,h=childimage.size
			childimage.thumbnail((w//2, h//2))
			newchildpath=os.path.join(fullpath,"new",os.path.split(childpath)[1])
			print os.path.split(childpath)[1]
			childimage.save(newchildpath,'jpeg')
	print "******Over******"
if __name__ =="__main__":
	foo('I:\\python\\pic\\more')