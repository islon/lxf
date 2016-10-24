def all_sum(*args):
	def clac_sum():
		sum=0
		for x in args:
			sum=sum+x
		return sum
	return clac_sum
f1=all_sum(1,2,3,4)
f2=all_sum(1,2,3,4)
print f1==f2