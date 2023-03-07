from random import randint

def checking_number(value, message):
	value = input(message)
	while True:
		try:
			value = value.replace(' ','')
			value = value.replace(',','.')
			value = float(value)
			if value <= 0:
				print('Пожалуйста, введите число больше нуля')
				value = input(message)
				continue
			if value % 1 == 0:
				value = int(value)
				break
		except:
			print('Пожалуйста, введите число: ')
			value = input(message)
			continue
		else:
			break
	return value
n = 0
mes = ('Введите количество числел в массиве: ')
n = checking_number(n, mes)

m = [randint(0,100) for i in range(n)]
print(f'Сгенерирован массив чисел - {m}')

p = []

for item in m:
	p.append(str(item)) 

p.sort(reverse=True)

max_number = ''.join(p)
print(f'Максимальное составное число -  {max_number}')	