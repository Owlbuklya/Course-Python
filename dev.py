# Задача - блок регистрации и входа пользователя в систему

# Объявляем словарь для хранения логинов и паролей пользователей
data_reg = {'admin': 'admin'}

question = input (f'''Введите "вход"  для авторизации. Или "регистрация" для регистрации. 
Для того чтобы выйти введите "выход": ''')

while question != 'вход' or question != 'регистрация' or question != 'выход':
    question = input ('Для продолжения введите "вход" или "регистрация": ')
    continue
else: 
    while True:
        if question == 'вход':
            login = input ('Введите логин: ')
            if login in data_reg.keys():
                password = input ('Введите пароль: ')
                if data_reg[login] == password:
                    print ('Вы успешно авторизированы!')
                    break
                else:
                    print ('Ввели не верный пароль')
                    question = input ('Введите "вход"  для авторизации. Или "регистрация" для регистрации: ')
                    continue
            else:
                print ('Ввели не верный логин')
                question = input ('Введите "вход"  для авторизации. Или "регистрация" для регистрации: ')
                continue
        elif question == 'регистрация':
            login = input ('Введите логин: ')
            password = input ('Введите пароль: ')
            if login in data_reg.keys():
                print ('Пользователь с таким логином уже существует!')
                question = input ('Введите "вход"  для авторизации. Или "регистрация" для регистрации: ')
                continue
            else:
                data_reg [login] = password
                print ('Вы успешно зарегистрированы!')
                continue
        elif question == 'выход':
            break 
