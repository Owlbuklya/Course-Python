check1 = False # переменная для проверки длины строки
check2 = False # переменная для проверки строчных букв
check3 = False # переменная для проверки заглавных букв
check4 = False # переменная для проверки цифр
check5 = True # переменная для проверки пробелов
check6 = True # переменная для проверки спец. символов

password = input ('Введите пароль:')

# проверка длины строки  
if len (password) > 7:
    check1 =  True

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

while check_all == False:
    print ('Пожалуйста, введите пароль отвечающий следующим требованиям:\n - длина не менее 8 символов без пробелов\n - должен содержать заглавные и строчные буквы\n - должен содержать хотя бы одну цифру и один специальный символ')

    # возврат значений переменным проверки
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    check5 = True
    check6 = True

    password = input ('Введите пароль:')

    # проверка длины строки  
    if len (password) > 7:
        check1 =  True
    
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
    
else:
    print ('Пароль принят!')