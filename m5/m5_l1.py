from random import randint

class StringVar:

	def __init__(self):
		self.str_data = input('Введите содержимое строки: ')

	def set(self):
		self.str_data = input('Введите новое содержимое строки: ')

	def get(self):
		return self.str_data

s = StringVar()

s.set()

print('Текущее содержимое строки:',s.get())


print(randint(10,30))