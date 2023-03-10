import json

# Функция проверки на соответствие требованиям сложности пароля
def check_password (password):
	def checker(password):
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

	while checker(password) == False:
		print ('Пожалуйста, введите пароль отвечающий следующим требованиям:\n - длина не менее 8 символов без пробелов\n - должен содержать заглавные и строчные буквы\n - должен содержать хотя бы одну цифру и один специальный символ')
		
		password = input ('Введите пароль:')

		checker(password)
    
	else:
		return password

# Функция регистрации нового пользователя
def register(login, passwd):
	while True:
		with open('reg_data.json', 'r') as f:
			data_reg = json.load(f)
		if login in data_reg.keys():
			print('Пользователя с таким логином уже существует!')
			login = input('Введите логин: ')
			continue
		else:
			passwd = check_password(passwd)
			data_reg [login] = passwd
			print('Вы успешно зарегистрированы!')
			break
	with open('reg_data.json', 'w') as f:
		json.dump(data_reg, f)

# Функция для входа в систему
def login_function(login, passwd):
	with open('reg_data.json', 'r') as f:
			data_reg = json.load(f)
	while True:
		if login in data_reg.keys():
			if data_reg[login] == passwd:
				print('Вы успешно авторизированы!')
				break
			else:
				print('Вы ввели не верный пароль') 
		else:
			print ('Пользователь с таким логином не существует')
		break

# Функция при вводе неверной команды
def error_command(command):
	command_list = ['вход', 'регистрация', 'выход']
	if command not in command_list:
		print('Неверная команда!')

# Функция обработки команд
def command_processing():
	while True:
		command = input('Введите одну из команд: вход, регистрация, выход: ')
		if command == 'вход':
			login_in = input('Введите логин: ')
			password_in = input('Введите пароль: ')
			login_function(login_in, password_in)
			continue
		elif command == 'регистрация':
			login_in = input('Введите логин: ')
			password_in = input('Введите пароль: ')
			register(login_in, password_in)
			continue  
		elif command == 'выход':
			break
		else: 
			error_command(command)

command_processing()