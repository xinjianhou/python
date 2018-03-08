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
		return(data.strip().split(','))
	except IOError as err:
		print('File error: ' + str(err))
		return(none)

import os

os.chdir('/Users/xinjianhou/Downloads/hfpy_ch5_data')
try:
	with open('james.txt') as james:
		james_data = james.readline().strip().split(',')

	with open('julie.txt') as julie:
		julie_data = julie.readline().strip().split(',')

	
	mikey_data = get_coach_data('mikey.txt')

	
	sarah_data = get_coach_data('sarah.txt')

except IOError as err:
	print('File error: ' + str(err))


clean_james = []

for each_time in james_data:
	clean_james.append(sanitize(each_time))

clean_julie = [sanitize(each_time)for each_time in julie_data]

clean_mikey = [sanitize(t) for t in mikey_data]

clean_sarah = sorted(set([sanitize(t) for t in sarah_data]))

print(sorted(james_data))
print(sorted(set(clean_james))[0:3])
print(sorted(julie_data))
print(sorted(set(clean_julie))[0:3])
print(sorted(mikey_data))
print(sorted(set(clean_mikey))[0:3])
print(sorted(sarah_data))
print(clean_sarah[0:3])
		