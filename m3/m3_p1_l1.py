x = float(input('Введите размер вклада: '))
p = float(input('Введите годовую процентную ставку: '))
y = float(input ('Введите желаемый размер вклада: '))

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


