# -*- coding= utf-8 -*-

#打开文档、读取内容
try:
	f=open('D:\\python\\txt\\hello.txt','r')
	print f.read()
finally:
	if f:
		f.close
		print '--------f is close--------'

#打开文档、读取内容、每行显示文字，精简版
with open('D:\\python\\txt\\hello.txt','r') as f:
	for line in f.readlines():
		print '----',line.strip()
if f:
	f.close
	print '--------f is close--------'
	

#打开二进制：图片、视频等
#with open('D:\\python\\pic\\girl_1.jpg','rb') as f:
#	print f.read()
	#显示出来的是16进制的字节

#写文件
with open('D:\\python\\txt\\write.txt','a') as f:
	f.write('this is first line')
	print u'--------写入成功--------'.encode("GBk")
with open('D:\\python\\txt\\write.txt','r') as r:
	print r.read()
	
with open('D:\\python\\txt\\write.txt','a') as f:
	f.write('\nthis is second line')
	print u'--------写入成功--------'.encode("GBk")
with open('D:\\python\\txt\\write.txt','r') as r:
	print r.read()