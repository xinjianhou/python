# 面试题 1

def extendList(val, list=[]):
	list.append(val)
	return list

list1 = extendList(10)
list2 = extendList(20, [10])
list3 = extendList('a')

print(list1)
print(list2)
print(list3)

# 正确的因该是：

def extendList2(val, list=None):
	if list == None:
		list = []
	list.append(val)
	return list

list1 = extendList2(10)
list2 = extendList2(20, [10])
list3 = extendList2('a')

print(list1)
print(list2)
print(list3)