# Задача - чат-бот для записи покупок

shopping_list = {'Хлеб':1} 

# Функция добавления наименования и кол-ва (с проверкой на число) в список
def add_position (shopping_list):
   name = input ('Введите наименование: ')
   while True:
      quantity = input('Введите количество: ')
      quantity = quantity.replace(',','.')
      try:
      	quantity = float(quantity)
      	if quantity % 1 == 0:
      		quantity = int(quantity)
      except:
         print('Пожалуйста, введите число: ')
         continue
      else:
         break
   if name in shopping_list:
      shopping_list[name] += quantity     
   else:
      shopping_list[name] = quantity
   return shopping_list

# Функция удаление позиции из списка
def remove_position(shopping_list):
   name = input('Введите наименование позициии, которую хотите удалить: ')
   shopping_list.pop(name, None)
   return shopping_list

# Функция отображения списка
def show_shopping_list(shopping_list):
   sort_shopping_list = sorted(shopping_list.keys())
   i = 0
   for name in sort_shopping_list:
      i += 1
      print(f'''{i}) {name} - {shopping_list[name]}''')

# Функция при вводе неверной команды
def error_command(command):
   if command != "+" or command != "-" or  command != "@" or  command != "!":
      print('Неверная команда!')

# Функция обработки команд
def command_processing(shopping_list):
	while True:
	   command = input ('Введите команды: "+" чтобы добавить / "-"  чтобы удалить / "@" чтобы вывести список / "!" чтобы выйти: ')
	   if command == '+':
	      shopping_list = add_position (shopping_list)
	   elif command == '-':
	      shopping_list = remove_position(shopping_list)  
	   elif command == '@':
	      show_shopping_list(shopping_list)
	   elif command == '!':
	      break
	   else: 
	      error_command(command)

command_processing(shopping_list)