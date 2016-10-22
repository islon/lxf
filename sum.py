
def sum(*number):
	sum=0
	for x in number:
		sum+=x*x
	return sum
	
y=sum(1,2,3)
print y