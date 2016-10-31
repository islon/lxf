import os

#print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#print [x for x in os.listdir('.') if os.path.isfile(x) and 'test' in os.path.splitext(x)[0]]
print [x for x in os.glo('D:\\python\\lxf\\search\\') if os.path.isfile(x) and 'un' in os.path.splitext(x)[0]]
#print [x for x in os.listdir('D:/python/lxf/search/') if os.path.isfile(x) and 'test' in os.path.splitext(x)[0]]
#new='D:\\python\\lxf\\search\\'
#print [x for x in os.listdir(new)]