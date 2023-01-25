x = int (input ('Введите первое число: '))
y = int (input ('Введите второе число: '))
z = int (input ('Введите третье число: '))

if x == y and x == z:
	print (3) # три числа равны
elif x == y or y == z or x == z:
	print (2) # два числа равны
else:
	print (0) # числа не равны