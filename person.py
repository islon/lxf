def person(name,age,**kw):
	print 'name:',name,'age:',age,'other:',kw

person('Jack',30,city='shenzhen')
person('LiuXiang',33,city='BeiJing',job='Runner')
kw={'city':'BeiJing','job':'Runner','Wife':'She'}
person('LiuXiang',33,**kw)
