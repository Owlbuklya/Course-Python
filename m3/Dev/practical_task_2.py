a = int (input ('Enter the first number: '))
b = int (input ('Enter the second number:'))

for i in range (a, b):
	if i % 5 == 0:
		print (i)
		break