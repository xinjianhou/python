import os
import nester
os.chdir('/Users/xinjianhou/Downloads')
man = []
other = []
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role,line_spoken) = each_line.split(':',1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			else:
				other.append(line_spoken)
				
		except ValueError:
			pass
	data.close()
except IOError:
	print('The data file is missing!')
try:
	'''用了with就不需要主动关闭file了
	'''
	with open('man_data.txt','w') as man_file:
		nester.print_lol(man,fn=man_file)
	with open('other_data.txt','w') as other_file:
		nester.print_lol(other,fn=other_file)

except IOError as err:
	print('File error: ' + str(err))


