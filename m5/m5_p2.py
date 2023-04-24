class Model():
	title = ''
	text = ''
	author = ''

	def __init__(self):
		self.title = input('Введите заголовок: ')
		self.text = input('Введите текст: ')
		self.author = input('Введите автора: ')

	def save(self):
		
		with open('model.json', 'w') as f:
			json.dump(data_reg, f)
		print(text_1.title)
		print(text_1.text)
		print(text_1.author)



text_1 = Model()


text_1.save()