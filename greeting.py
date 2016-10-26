def _private_1(name):
	return "hello,+3,%s"%name
def _private_2(name):
	return "hi,-=3,%s"%name

def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)


print greeting("dfa")