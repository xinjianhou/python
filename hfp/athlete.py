class Athlete:
	def __init__(self,a_name,a_dob=None,a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

	def top3(self):
		return sorted(set([sanitize(t) for t in self.times]))[0:3]

	def  add_time(self,time):
		self.times.append(time)
	
	def add_times(self,times):
		self.times.extend(times)

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
		return(Athlete(temp.pop(0),temp.pop(0),temp))
	except IOError as err:
		print('File error: ' + str(err))
		return(none)



import os

os.chdir('/Users/xinjianhou/Downloads/hfpy_ch6_data')

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')


print(james.name + "' a fastest times are " + str(james.top3()))
print(julie.name + "' a fastest times are " + str(julie.top3()))
print(mikey.name + "' a fastest times are " + str(mikey.top3()))
print(sarah.name + "' a fastest times are " + str(sarah.top3()))

	
