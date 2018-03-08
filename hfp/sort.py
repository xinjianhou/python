import os

os.chdir('/Users/xinjianhou/Downloads/hfpy_ch5_data')
try:
	with open('james.txt') as james:
		james_data = james.readline().strip().split(',')

	with open('julie.txt') as julie:
		julie_data = julie.readline().strip().split(',')

	with open('mikey.txt') as mikey:
		mikey_data = mikey.readline().strip().split(',')

	with open('sarah.txt') as sarah:
		sarah_data = sarah.readline().strip().split(',')

except IOError as err:
	print('File error: ' + str(err))

print(sorted(james_data))
print(sorted(julie_data))
print(sorted(mikey_data))
print(sorted(sarah_data))
	