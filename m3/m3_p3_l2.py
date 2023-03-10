def textor(string_in, len_word):
	string_without_punc_sym = ''
	for symbol in string_in:
		if symbol.isalnum() or symbol == ' ' or symbol == '\n':
			string_without_punc_sym += symbol
	str_list = string_without_punc_sym.split()
	list_out = []
	for word in str_list:
		if len(word) < len_word:
			list_out.append(word)
	return list_out

n = 5 # длина слов для поиска 

s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я - того.
На столе записка от неё смятая
Недопитый виски допиваю с матами.
Посмотрю в окно, допишу главу
Первое сентября, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''

print(textor(s, n))