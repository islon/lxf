def now():
	print '2016-10-24'
f=now
print 'f():',f()
print now.__name__
print f.__name__
print "#################"


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
log(now())
print "#################"

