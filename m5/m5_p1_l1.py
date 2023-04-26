class StringVar:

	def __init__(self, str_data):
		self.str_data = str_data

	def set(self, str_data):
		self.str_data = str_data

	def get(self):
		return self.str_data

string_in = 'Какая-то строка'

s = StringVar(string_in)

print(f'\nТекущее содержимое строки: {string_in}')

string_set = input("\n>>Метод set<<\nВведите новую строку: ")

s.set(string_set)

string_get = s.get()

print(f'\n>>Метод get<<\nНовое содержимое строки: {string_get}')
