def f(x):
	return x[0].upper()+x[1:].lower()
print map(f,['adam', 'LISA', 'barT'])

def prd(x,y):
	return x*y
print reduce(prd,[1, 3, 5, 7, 9])