x = float (input ('Введите первое число: '))
y = float (input ('Введите второе число: '))

max1 = (x >= y) * x + (x < y) * y 

print ('Наибольшее число: ',max1)