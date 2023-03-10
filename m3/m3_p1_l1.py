
def checking_number(value, message):
	while True:
		try:
			value = value.replace(' ','')
			value = value.replace(',','.')
			value = value.replace('-','')
			value = float(value)
			if value % 1 == 0:
				value = int(value)
				return value
		except:
			print('Пожалуйста, введите число!')
			value = input(message)
			continue
		else:
			break
	return value

message_1 = 'Введите начальный размер вклада: '
x = input(message_1)
x = checking_number(x, message_1)

message_2 = 'Введите годовую процентную ставку: '
p = input(message_2)
p = checking_number(p, message_2)

message_3 = 'Введите желаемый размер вклада: '
y = input (message_3)
y = checking_number(y, message_3)

# Функция расчета прибыли за 1 год 
def annual_income (deposit_amount, interest_rate):
	yearly_income = int((deposit_amount * interest_rate * 0.01))
	return yearly_income

# Функция определния формы слова "год" взависимости от количества
def year_or_yaers(year):
	if period == 1:
		year = 'год'
	elif period <= 4:
		year = 'года'
	else:
		year = 'лет'
	return year

while y < x:
	print('Желаемый размер вклада должен быть больше')
	y = float(input ('Введите желаемый размер вклада: '))

period = 0

income = int(x)

while annual_income(x, p) == 0:
	print('Слишком маленькие значения вклада или ставки. Доход за год меньше 1 рубля.')
	x = input(message_1)
	x = checking_number(x, message_1)
	p = input(message_2)
	p = checking_number(p, message_2)

while y > income:
	income += annual_income(income, p) 
	period += 1

print(f'''Через {period} {year_or_yaers(period)} ваш вклад составит {income} рублей. Доход - {int(income - x)}''')


