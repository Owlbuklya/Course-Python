password = input ('Введите пароль:')

while len(password) < 7 or password.islower() == True or password.isupper() == True or password.isdigit() == True or password.isspace() == True:
    print ('Пожалуйста, введите пароль отвечающий следующим требованиям:\n - длина не менее 8 символов;\n - должен содержать заглавные и строчные буквы')
    password = input ('Введите пароль:')
else:
    print ('Пароль принят!')