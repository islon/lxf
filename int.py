print int('12345',16)
print int('12345',8)
print int('12345',base=12)
print int('1010101',2)

def int2(x,base=2):
	return int(x,base)
	

print int2('10000000')

import functools
int16=functools.partial(int,base=16)
print int16('100')