def log(func):
	def wrapper(*args,**kw):
		print 'call %s():'%func.__name__
		return func(*args,**kw)
	return wrapper
	
log(abs)

@log
def now():
	print '20161024'
now()