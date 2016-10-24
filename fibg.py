def fibg(M):
	n,a,b=0,0,1
	while n<M:
		yield b
		#print b
		a,b=b,a+b
		n=n+1
print fibg(5)
for x in fibg(5):
	print x