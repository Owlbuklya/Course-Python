# Модуль 1 / Часть 2 / Уровень 3

password = input ('Введите пароль:')

def check_password (password):

	check1 = False # переменная для проверки длины строки
	check2 = False # переменная для проверки строчных букв
	check3 = False # переменная для проверки заглавных букв
	check4 = False # переменная для проверки цифр
	check5 = True # переменная для проверки пробелов
	check6 = True # переменная для проверки спец. символов
	check_all = False # переменная для проверки всех условий

	if len (password) > 7:
		check1 = True

	# проверка строчных букв
	for i in password:
		if i.islower():
			check2 = True

	# проверка заглавных букв
	for i in password:
		if i.isupper():
			check3 = True

	# проверка цифр
	for i in password:
		if i.isdigit():
			check4 = True

	# проверка пробелов
	if ' ' in password:
		check5 = False

	# проверка спец. символов
	if password.isalnum():
		check6 = False

	# проверка всех условий
	check_all = (check1 and check2 and check3 and check4 and check5 and check6)

	return check_all

while check_password (password) == False:
	print ('Пожалуйста, введите пароль отвечающий следующим требованиям:\n - длина не менее 8 символов без пробелов\n - должен содержать заглавные и строчные буквы\n - должен содержать хотя бы одну цифру и один специальный символ')
	
	password = input ('Введите пароль:')

	check_password (password)
    
else:
	print ('Пароль принят!')