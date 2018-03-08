import pickle
from athletelist import AthleteList

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		temp = data.strip().split(',')
		return(AthleteList(temp.pop(0),temp.pop(0),temp))
	except IOError as err:
		print('File error: ' + str(err))
		return(none)

def put_to_store(file_list):
	all_athletes = {}
	
	for each_file in file_list:
		ath = get_coach_data(each_file)
		all_athletes[ath.name] = ath

	try:
		with open('athlete.pickle','wb') as athf:
			pickle.dump(all_athletes,athf)

			
	except IOError as err:
		print('File error(put_to_store: ' + err)
	return all_athletes
	

def get_from_store():
	all_athletes = {}

	try:
		with open('athlete.pickle','rb') as athf:
			all_athletes = pickle.load(athf)
                        
		
	except IOError as err:
		print('File error(get_from_store: ' + err)
	return all_athletes

def get_names_from_store():
	athletes = get_from_store()
	response = [athletes[each_ath].name for each_ath in athletes]

	return(response)