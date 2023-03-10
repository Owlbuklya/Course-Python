# Функция проверка ввденного значения на число 
def checking_number(message):
	value = input(message) 
	while True:
		try:
			value = value.replace(' ','')
			value = value.replace('-','')
			value = int(value)
			break
		except:
			print('Пожалуйста, введите число! ')
			value = input(message)
			continue
	return value

message_1 = 'Введите количество повторений: '

n = ''

n = checking_number(message_1)

i = 1

while n != 0:
	print(f'''{i}) for - частный случай цикла while''')
	i += 1
	n -= 1