def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins,secs) = time_string.split(splitter)

	return (mins + '.' + secs)


def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		temp = data.strip().split(',')
		return({'Name':temp.pop(0),
			'DOB':temp.pop(0),
			'Times':str(sorted(set([sanitize(t) for t in temp]))[0:3])})
	except IOError as err:
		print('File error: ' + str(err))
		return(none)

import os

os.chdir('/Users/xinjianhou/Downloads/hfpy_ch6_data')

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')


print(james['Name'] + "' a fastest times are " + james['Times'])
print(julie['Name'] + "' a fastest times are " + julie['Times'])
print(mikey['Name'] + "' a fastest times are " + mikey['Times'])
print(sarah['Name'] + "' a fastest times are " + sarah['Times'])

		