import sys
def print_lol(the_list,indent=False,level=0,fn=sys.stdout):
	'''来循环遍历集合，打印出集合里的每一样东西
	'''
	# 传入一个集合
	for iteam in the_list:
		if isinstance(iteam,list):
			print_lol(iteam,indent,level+1,fn);
		else:
			if indent:
				for tab_stop in range(level):
					print('\t',end='',file=fn)
			print(iteam,file=fn);
