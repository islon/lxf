from collections import OrderedDict
from collections import Counter

d = dict([('a', 1), ('E', 2), ('c', 3)])
print d

#有序的dict
od=OrderedDict([('a', 1), ('E', 2), ('c', 3)])
print od
print od.keys(),od.values()

#统计字符出现的个数
c=Counter()
for ch in "programming":
	c[ch]=c[ch]+1
print c