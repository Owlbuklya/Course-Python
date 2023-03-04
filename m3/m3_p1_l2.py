def checking_number(value, message):
	while True:
		try:
			value = value.replace(',','.')
			value = float(value)
			if value % 1 == 0:
				value = int(value)
				break
		except:
			print('Пожалуйста, введите число! ')
			value = input(message)
			continue
	return value

message_1 = 'Введите количество повторений: '

n = input(message_1) 

n = checking_number(n, message_1)

i = 1

while n != 0:
	print(f'''{i}) for - частный случай цикла while''')
	i += 1
	n -= 1