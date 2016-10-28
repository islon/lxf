# -*- coding: utf-8 -*- 

import Image,ImageFilter
print "打开图片"
im =Image.open('I:\python\pic\pi.jpg')
print "获取图片尺寸"
#w,h=im.size
print "缩放尺寸"
#im.thumbnail((w//3,h//3))
print "模糊图片"
im =im.filter(ImageFilter.BLUR)
print "保持图片"
im.save('I:\python\pic\pi2.jpg','jpeg')


