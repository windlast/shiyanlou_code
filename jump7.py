for i in range(1,101):
	if i % 7 == 0:
		continue
	elif i>69 and i<80:
		continue
	elif i>10 and i % 10 == 7:
		continue
	else:
		print(i)
