# -*- coding: utf-8 -*-
from PIL import Image
import os
import ImageFilter

def foo(fullpath):
	print "******Start******"
	for child in os.listdir(fullpath):
		childpath=os.path.join(fullpath,child)
		if os.path.isfile(childpath):
			childimage=Image.open(childpath)
			w,h=childimage.size
			print u"改变尺寸"
			childimage.thumbnail((w//2, h//2))
			print u"保存到新的路径"
			newchildpath=os.path.join(fullpath,"new",os.path.split(childpath)[1])
			print os.path.split(childpath)[1]
			print u"模糊图片"
			childimage=childimage.filter(ImageFilter.BLUR)
			print u"保存图片"
			childimage.save(newchildpath,'jpeg')
			print u"保存成功"
	print "******Over******"
if __name__ =="__main__":
	foo('D:\\python\\pic\\more')