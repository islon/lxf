# -*- coding= utf-8 -*-

try:
	import cpickle as pickle
except ImportError:
	import pickle

d=dict(a=1,name="bob",c=3)
print d

print pickle.dumps(d)