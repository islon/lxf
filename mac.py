# -*- coding: utf-8 -*-

import uuid
import random
mac=uuid.uuid1().hex[-12:]
#获取mac地址
print mac

print "############"
a=['c','d']
a.reverse()
#倒序
print a
b=','.join(a)
#通过符号“,”把a的元素连接起来
print b


print "############"
for i in range(1,5):
	x=random.randint(1,100)
	print x
	y=random.choice('abcd')
	print y
	
print "############"
a=[1,2,3]
b=['a','b','c']
c=dict(zip(a,b))
print u"2个列表合成一个dict".encode("GBK")
print a,"+",b,"=>",c

print "############"
a='1-2-3-4'
b=map(int,a.split('-'))
print a,"=>",b

print "############"

