class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def pt_score(self):
		print "%s:%d"%(self.__name,self.__score)
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def __len__(self):
		return 100
	
xm=Student("xiaoming",80)
print xm.pt_score()
print xm.get_name(),":",xm.get_score()
print xm._Student__name
print isinstance(xm,Student)

print dir("asdf")
print dir(xm)
print len("daf")
print "adf:","adf".__len__()
print "len(xm):",len(xm)