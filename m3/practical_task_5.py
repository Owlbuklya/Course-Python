#Задача с удалением слова "hello" и знаков препинания

string_in = input ("Введите строку: ")
string_out = ''
string_without_punc_sym = ''

# удаление знаков препинания
for symbol in string_in:
    if symbol.isalnum() or symbol == ' ':
        string_without_punc_sym += symbol

string_out = string_without_punc_sym.replace('hello','')

print (string_out)