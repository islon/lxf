L=[x*x for x in range(1,11)]
print 'L=',L
P=(x*x for x in range(1,11))
print 'P=',P
#for n in P:
#	print n
n=5
while n>0:
	print P.next()
	n-=1
