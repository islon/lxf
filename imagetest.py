# -*- coding: utf-8 -*- 
from PIL import Image
import ImageFilter
print u"打开图片"
im =Image.open('D:\python\pic\pi.jpg')
print u"获取图片尺寸"
#w,h=im.size
print u"缩放尺寸"
#im.thumbnail((w//3,h//3))
print u"模糊图片"
im =im.filter(ImageFilter.BLUR)
print u"保持图片"
im.save('D:\python\pic\pi2.jpg','jpeg')


