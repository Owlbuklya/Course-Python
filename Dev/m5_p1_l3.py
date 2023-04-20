from random import randint

class Warrior():
	num = 1
	health = 100
	endurance = 100
	armor = 100
	def __init__(self, name):
		self.name = name

	def gen_action(self):
		return randint(0,1)

	def attack(self, damnum_health = None):
		self.endurance -= 10
		if damnum_health is not None and self.armor > 0:
			if self.health - damnum_health > 10: 
				self.health -= damnum_health
			elif self.health - damnum_health > 0:
				self.health -= damnum_health
				print(f'{self.name}  - проигрывает! Убить или помиловать?')
			else:
				print(f'{self.name}  - Убит!')
				self.health = 0	
		# if damnum_armor is not None:
		# 	armor -= damnum_armor 

unit_1 = Warrior('Воин 1')


unit_2 = Warrior('Воин 2')

# while unit_1.health > 10 or unit_1.health > 10:
# 	if unit_1.gen_action() == 1 and unit_2.gen_action() == 1:
# 		print(f'{unit_1.name} и {unit_1.name} атакуют!')
# 		unit_1.attack(randint(10,30))
# 		unit_1.attack(randint(10,30))



# for i in range(5):
# 	if unit_1.gen_action() == 1 and unit_2.gen_action() == 1:
# 		print(f'{unit_1.name} и {unit_1.name} атакуют')
# 		unit_1.attack()
# 		unit_2.attack()


unit_1.attack(10)
print(f'Здоровье {unit_1.name} - {unit_1.health}')

# while unit_1.health > 10 or unit_1.health > 10:
# 	a1 = randint(10,30)
# 	print('a1=', a1)
# 	a2 = randint(10,30)
# 	print('a2=', a2)
# 	unit_1.attack(a1)
# 	print(f'Здоровье {unit_1.name} - {unit_1.health}')
# 	unit_2.attack(a2)
# 	print(f'Здоровье  {unit_2.name} - {unit_2.health}')


