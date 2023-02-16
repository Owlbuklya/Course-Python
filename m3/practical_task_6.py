 # Задача - блок регистрации и входа пользователя в систему

# Объявляем словарь для хранения логинов и паролей пользователей
data_reg = {'admin': 'admin'}

while True: 
   question = input('Введите одну из команд: вход, регистрация, выход: ')
   if question == 'вход':
      login = input ('Введите логин: ')
      if login in data_reg.keys():
         password = input ('Введите пароль: ')
         if data_reg[login] == password:
            print ('Вы успешно авторизированы!')
            break
         else:
            print ('Вы ввели не верный пароль')   
      else:
         print ('Пользователь с таким логином не существует')
   elif question == 'регистрация':
      login = input ('Введите логин: ')
      if login in data_reg.keys():
            print ('Пользователя с таким логином уже существует!')
      else:
         password = input ('Введите пароль: ')
         data_reg [login] = password
         print ('Вы успешно зарегистрированы!')
   elif question == 'выход':
      break
else:
   question = input('Введите одну из команд: вход, регистрация, выход: ')
