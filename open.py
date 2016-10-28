try:
	f=open('I:/python/txt/hello.txt','r')
	print f.read()
finally:
	if f:
		f.close()
		print "error"