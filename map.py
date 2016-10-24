def f(x):
	return x*x
print map(f,[1,2,3,4,5,6,7,8,9])
print map(str,[1,2,3,4,5,6,7,8,9])

def g(x,y):
	return x+y
print reduce(g,[1,2,3,4,5,6,7,8,9])