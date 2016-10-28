# -*- coding: utf-8 -*-
 
class Student(object):
	pass

s=Student()
s.name='Jack'
print s.name

def set_age(self,age):
	self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s,Student) #给实例绑定一个方法
s.set_age(25)
print s.age

def set_score(self,score):
	if not isinstance(score,int):
		return score,"不是int类型"
	if score <0 or score>100:
		return score,"score must between 0^100!"
	self.score=score

Student.set_score=MethodType(set_score,None,Student)
s.set_score(100)
print s.score
s2=Student()
s2.set_score(200)
print s2.score()