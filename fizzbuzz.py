for i in range(15):
	if (i+1) % 3 == 0 and (i+1) % 5 == 0:
		print('fizz')
	elif (i+1) % 5 == 0:
		print('buzz')
	elif (i+1) % 3 == 0:
		print('fizzbuzz')
	else:
		print(i+1)
