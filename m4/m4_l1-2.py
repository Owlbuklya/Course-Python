from random import randint

n = 12 # число элементов генерируемого массива
m = [randint(0,50) for i in range(n)]

# Функция проверки вводимого значения на целое число
def checking_val(value):
	while True:
		try:
			value = int(value)
			break
		except:
			print('Пожалуйста, введите число! ')
			value = input ('Введите искомое число: ')
			continue
	return value

# Функция сортировки массива простыми вставками
def insertion_sort(array):
	for i in range(1, len(array)):
		key = array[i]
		j = i - 1
		while (array[j] > key and j >= 0):
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key
	return array

# Функция бинарного поиска
def binary_search(array, value):
	mid = len(array) // 2
	low = 0 
	high = len(array) - 1 
 
	while (array[mid] != value and low <= high):
		if value > array[mid]: 
			low = mid + 1
		else:
			high = mid - 1
		mid = (low + high) // 2

	if low > high:
		return print('Искомое число не найдено!')
	else: # проверка на повтор искомого значения в массиве
		index = []
		i = mid
		while (array[i] == value and i >= 0):
			index = [i] + index
			i -= 1
		i = mid + 1 
		if i <= high:
			while (array[i] == value and i <= len(array)):
				index = index + [i]
				i += 1
				if i > high:
					break
		if len(index) == 1:
			return print(f'Индекс искомого значения - {index}')
		else:
			return print(f'Найдено несколько совпадений. Индексы искомого числа: {index}')


print('Сгенерирован случайный массив чисел -', m)
m = insertion_sort (m)
print('Массив отсортирован методом простых вставок -', m)
val = input('Введите искомое число: ')
val = checking_val(val)
binary_search(m,val)
