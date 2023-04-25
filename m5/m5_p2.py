import json

class Model():
	title = ''
	text = ''
	author = ''

	def __init__(self):
		self.title = input('Введите заголовок: ')
		self.text = input('Введите текст: ')
		self.author = input('Введите автора: ')

	def save(self):
		note_data = self.__dict__
		with open('model.json', 'w') as f:
			json.dump(note_data, f)
		print('Иформация записана в файл model.json')

note_1 = Model()

note_1.save()

with open('model.json', 'r') as f:
		 print(json.load(f))