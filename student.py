
class student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def pt_score(self):
		print "score:",self.score
		return None
	def get_grade(self):
		if self.score>=90:
			return "A"
		elif self.score>=60:
			return "B"
		else:
			return "C"
xm=student("xiaoming",70)
ls=student("lisa",99)
print 1,xm
print 2,"name:%s\nscore:%d"%(xm.name,xm.score)
print 3,xm.pt_score()
print 4,xm.get_grade()
xm.age=18
print xm.age