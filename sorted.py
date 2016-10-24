def reversed_cmp(x,y):
	if x>y:
		return -1
	if x<y:
		return 1
	return 0
L=[20,36, 5, 12, 9, 21]
print L
print sorted(L)
print sorted(L,reversed_cmp)

def cmp_ignore_case(s1,s2):
	u1=s1.upper()
	u2=s2.upper()
	if u1<u2:
		return -1
	if u1>u2:
		return 1
Q=['bob', 'about', 'Zoo', 'Credit']
print Q
print sorted(Q,cmp_ignore_case)