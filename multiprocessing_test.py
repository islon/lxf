#window have no fork,so  

from multiprocessing import Process
import os
import time


def run_proc(name):
	for n in range(0,5):
		print 11111,'*******','Run child process %s(%s)...'%(name,os.getpid())
		time.sleep(0)
		print 11111,'*******',n+1
		
def run_proc2(name):
	for n in range(0,5):
		print 222222,'*******','Run child process %s(%s)...'%(name,os.getpid())
		time.sleep(2)
		print 222222,'*******',n+1

if __name__=='__main__':
	print 'Parent process %s.'% os.getpid()
	p=Process(target=run_proc,args=('test1111',))
	p2=Process(target=run_proc2,args=('test2222',))
	print 'Process will start.'
	p.start()
	p2.start()
	p.join()
	p2.join()
	print 'Process end.'