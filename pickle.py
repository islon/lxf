# -*- coding: utf-8 -*-
 
try:
	import cPickle as pickle
except ImportError:
	import pickle

d=dict(name='bob',age=20,score=88)
pickle.dumps(d)
f=open('dumps.txt','wb')
pickle.dump(d,f)
print u"dumps.txt 保存成功".encode("GBK")
f.close

f=open('dumps.txt','rb')
print f
d=pickle.load(f)
f.close()
print d