import os
import pickle
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
	#用了with就不需要主动关闭file了
	
	with open('man_data.txt','wb') as man_file:
		pickle.dump(man,man_file)
	with open('other_data.txt','wb') as other_file:
		pickle.dump(other,other_file)

except IOError as err:
	print('File error: ' + str(err))

except pickle.PickleError as perr:
	print('Pickle error: '+str(perr))


