#Задача с удалением слова "hello" и знаков препинания

string_in = input ("Введите строку: ")
string_out = ''
string_without_punc_sym = ''

# удаление знаков препинания
for symbol in string_in:
    if symbol.isalnum() or symbol == ' ':
        string_without_punc_sym += symbol

# разбиваем строку на слова и убираем слово "hello"
word_list = string_without_punc_sym.split ()

for word in word_list:
    if word != "hello":
        string_out = string_out + ' ' + word

print (string_out[1:])