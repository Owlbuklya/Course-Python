# функция проверки значения введенной координаты
def input_validation (coordinate):
	while  coordinate.isnumeric() == False or coordinate == '0':
		coordinate = input ('Пожалуйста, введите координату в виде целого положительного числа: ')
	valid_coordinate = int (coordinate)
	return valid_coordinate

# ввод и проверка значения координат

x1 = input ('Введите координату X первой клетки: ')
x1 = input_validation(x1)

y1 = input ('Введите координату Y первой клетки: ')
y1 = input_validation(y1)

x2 = input ('Введите координату X второй клетки: ')
x2 = input_validation(x2)

y2 = input ('Введите координату Y второй клетки: ')
y2 = input_validation(y2)

# проверка условия задачи

if x1 == x2 or y1 == y2:
	print ('YES') 
else:
	print ('NO')

