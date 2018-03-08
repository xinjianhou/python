import pickle
import nester
import os
os.chdir('/Users/xinjianhou/Downloads')

new_man = []

try:
	with open('man_data.txt','rb') as man_file:
		new_man = pickle.load(man_file)

except IOError as err:
	print('File error: ' + str(err))
except pickle.PickleError as perr:
	print('Pickle Error: ' + str(perr))

nester.print_lol(new_man)
