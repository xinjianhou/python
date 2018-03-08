verbs = ('go', 'stop', 'kill', 'eat')
stop_words = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')
Direction_words = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back', 'forward')

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None


def scan(s):
	a = [];
	words = s.split(' ')
	for x in words:
		a.append(macth_with(x))

	return a

def macth_with(word):
	if word in verbs:
		return ('verb', word)
	elif word in stop_words:
		return ('stop', word)
	elif word in nouns:
		return ('noun', word)
	elif word in Direction_words:
		return ('direction', word)
	elif convert_number(word) != None:
		return ('number', convert_number(word))
	else: 
		return ('error', word)