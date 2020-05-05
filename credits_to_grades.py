file = open('/home/ashutosh/data', 'r')
lines = file.readlines()

for line in lines:
	roll, hours, credits_registered = map(int, line.split())
	credits_completed = hours//15
	if credits_completed > credits_registered:
		credits_completed = credits_registered
	S='S'*credits_completed
	F='F'*(credits_registered - credits_completed)
	grade=S+F
#	print('Roll: {0}, Grade: {1}'.format(roll, grade))
	print(grade)
