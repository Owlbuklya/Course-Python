def area(a, b, c):
	p = (a + b + c) / 2
	area_triangle = (p * (p - a) * (p - b) * (p - c)) ** 0.5
	return area_triangle

def checking_number(value, message):
	value = input(message)
	while True:
		try:
			value = value.replace(',','.')
			value = value.replace(' ','')
			value = float(value)
			break
		except:
			print('Пожалуйста, введите число!')
			value = input(message)
			continue
	return value

message_1 = 'Введите длину первой стороны треугольника: '
message_2 = 'Введите длину второй стороны треугольника: '
message_3 = 'Введите длину третьей стороны треугольника: '

x = 0
y = 0
z = 0 

x = checking_number(x, message_1)
y = checking_number(y, message_2)
z = checking_number(z, message_3)

triangle_area = area(x, y, z)

print(triangle_area)