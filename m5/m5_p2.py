import json

class Model():
	title = ''
	text = ''
	author = ''

	def __init__(self, title_data, text_data, author_data):
		self.title_data = title_data
		self.text_data = text_data
		self.author_data = author_data

	def save(self):
		note_data = self.__dict__
		with open('model.json', 'w') as f:
			json.dump(note_data, f)
		print('Иформация записана в файл model.json')

title = 'Какой-то заголовок'
text = 'Какой-то текст'
author = 'Какой-то автор'

note = Model(title, text, author)

note.save()

with open('model.json', 'r') as f:
		 print(json.load(f))