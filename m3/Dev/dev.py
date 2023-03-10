def checking_number(value, message):
	while True:
		try:
			value = value.replace(',','.')
			value = float(value)
			if value % 1 == 0:
				value = int(value)
				return value
		except:
			print('Пожалуйста, введите число: ')
			value = input(message)
			continue
		else:
			break
	return value

message_1 = 'Введите начальный размер вклада: '
 x = input('Введите начальный размер вклада: ')
 x = checking_number(x, message_1)