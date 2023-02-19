
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

x = input('Введите размер вклада: ')
checking_number(x, 'Введите размер вклада: ')

p = input('Введите годовую процентную ставку: ')
checking_number(p, 'Введите годовую процентную ставку: ')

y = input ('Введите желаемый размер вклада: ')
checking_number(y, 'Введите желаемый размер вклада: ')

# Функция расчета прибыли за 1 год 
def annual_income (deposit_amount, interest_rate):
	yearly_income= int(deposit_amount + (deposit_amount * interest_rate * 0.01))
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

period = 1

income = annual_income(x, p)

print(income)

while y > income:
 	income += annual_income(income, p) 
 	period += 1
   
print(f'''Через {period} {year_or_yaers(period)} ваш вклад составит {income} рублей. Доход - {int(income - x)}''')


