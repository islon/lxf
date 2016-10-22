def fib(Max):
	n,a,b=0,1,1
	while n<=Max:
		print a
		a,b=b,a+b
		n+=1
fib(5)