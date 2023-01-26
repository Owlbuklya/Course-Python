n = int (input('Введите предел диапазона для поиска простых чисел: '))

for i in range (1, n):
	k = 0
	for j in range (2, i):
		if i % j == 0:
			k += 1
	if k == 0:
		print (i) 