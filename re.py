import re
test='010-12345'
if re.match(r'^\d{3}\-\d{3,8}$',test):
	print 'ok'
else:
	print 'failed'

print 'a b   c'.split(' ')
print re.split(r'\s+','a b   c')
print re.split(r'[\s\,]+','a,b, c  d')
print re.split(r'[\s\,\;]+','a,b;; c  d')

m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print m.group(0)
print m.group(1)
print m.group(2)

def isemail(email):
	if re.match(r'^<(*.)>([0-9a-zA-z\_]+)|\.|([0-9a-zA-z\_]+)@([0-9a-zA-z]+)\.([a-zA-z]+)$',email):
		print '%s is email address'%email
	else:
		print '%s is not email address'%email
		
isemail('someone@gmail.com')
isemail('bill.gates@microsoft.com')
isemail('<Tom Paris> tom@voyager.org')