def isNotPrime(n):
	if n<=1:
		return 1
	elif n==2:
		return 0
	else:
		for x in range(2,n/2+1):
			if n%x==0:
				return 1

print filter(isNotPrime,range(1,101))

p=filter(isNotPrime,range(1,101))

n=1
for p1 in range(1,101):
	if p1 not in p:
		print n,":",p1
		n+=1
		
print range(2,2)