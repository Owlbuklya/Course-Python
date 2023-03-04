def checking_number(value, message):
	while True:
		try:
			value = value.replace(' ', '')
			value = value.replace('-', '')
			value = int(value)
			break
		except:
			print('Пожалуйста, введите целое число!')
			value = input(message)
			continue
	value = str(value)
	return value

message_1 = 'Введите целое число: '
n = input(message_1)
n = checking_number(n, message_1)

sum = 0

for i in range(len(n)):
	sum += int(n[i])	
	

print(f'Сумма цифр данного числа - {sum}')
