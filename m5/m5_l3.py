from random import randint

class Warrior():
	num = 1
	health = 100
	endurance = 100
	armor = 100
	
	def __init__(self):
		self.name = input(f'Введите имя войну {self.num}: ')
		Warrior.num += 1
		print(f""">> Войн {self.name} <<
Здоровье - {self.health}
Вносливость - {self.endurance}
Броня - {self.armor}""")
	
	def print_condition(self):
		print(f""">> Войн {self.name} <<
Здоровье - {self.health}
Вносливость - {self.endurance}
Броня - {self.armor}""")

	#Атака - <атакующий>.attack(<атакуемый>)
	def attack(self,other, dam_health_out = None):
		if self.endurance >= 10:
			self.endurance -= 10
			if dam_health_out is not None:
				dam_health = dam_health_out
			else:	
				dam_health = randint(10,30)
			print(f'#Урон здоровью - {dam_health}')
			if (other.health - dam_health) > 10:
				other.health -= dam_health
				other.print_condition()
			elif 0 < (other.health - dam_health) <= 10:
				other.health -= dam_health
				other.print_condition()
				print(f"""_______________________

Бой окончен ...
Войну {other.name} нанесен критичный удар.
Он проигрывает бой!""")
				other.pollice_verso()
			else:
				print(f"""_______________________

Войну {other.name} нанесен смертельный удар.
Он проигрывает бой!""")
				other.health = 0
				print(f'Здоровье война {other.name} - {other.health}')
		else:
			self.endurance = 0
			if dam_health_out is not None:
				dam_health = dam_health_out
			else:	
				dam_health = randint(10,30)
			print(f'#Урон здоровью - {dam_health}')
			if (other.health - dam_health) > 10:
				other.health -= dam_health
				other.print_condition()
			elif 0 < (other.health - dam_health) <= 10:
				other.health -= dam_health
				other.print_condition()
				print(f"""_______________________

Бой окончен ...
Войну {other.name} нанесен критичный удар.
Он проигрывает бой!""")
				other.pollice_verso()
			else:
				print(f"""_______________________

Бой окончен ...
Войну {other.name} нанесен смертельный удар.
Он проигрывает бой!""")
				other.health = 0
				print(f'Здоровье война {other.name} - {other.health}')

	#Защита при атаке - <атакующий>.protect_attack(<защищающийся>)	
	def protect(self, other):
		if self.endurance > 10:
			# self.endurance -= 10
			dam_armor = randint(0,10)
			if (other.armor - dam_armor) > 0:
				other.armor -= dam_armor
				print(f'#Урон броне - {dam_armor}')
				self.attack(other, randint(0,20))
			else:
				other.armor = 0	
				self.attack(other)
		else:
			dam_armor = randint(0,10)
			if (other.armor - dam_armor) > 0:
				other.armor -= dam_armor
				print(f'#Урон броне - {dam_armor}')
				self.attack(other, randint(0,10))
			else:
				other.armor = 0	
				self.attack(other)

	def pollice_verso(self):
		while True:
			verdict = input(f'\nЧтобы помиловать война {self.name} введите  - 1, убить - 0: ')
			if verdict == "1":
				print('Помилован!')
				print('_______________________')
				break
			elif verdict == "0":
				print('Казнён!')
				print('_______________________')
				break
			else:
				print('Введите 1 или 0')
				continue

unit_1 = Warrior()
unit_2 = Warrior()

print('\n<<< Бой начался! >>>')

i = 1 # счетчик раундов

while unit_1.health > 10 and unit_2.health > 10:
	print(f'\n= Раунд {i} =')
	action_1 = randint(0,1)
	action_2 = randint(0,1)
	if action_1 == 1 and action_2 == 1:
		print('#Оба война атакают!')
		attack_priority = randint(1,2)
		if attack_priority == 1:
			print(f'#Первым наносит удар воин {unit_1.name}')
			unit_1.attack(unit_2)
			if unit_2.health < 10:
				break	
			print(f'#Ответный удар наносит воин {unit_2.name}')
			unit_2.attack(unit_1)
			if unit_1.health < 10:
				break	
		else:
			print(f'#Первым наносит удар воин {unit_2.name}')
			unit_2.attack(unit_1)
			if unit_1.health < 10:
				break	
			print(f'#Ответный удар наносит воин {unit_1.name}')
			unit_1.attack(unit_2)
			if unit_2.health < 10:
				break	
	elif action_1 == 1 and action_2 == 0:
		print(f'#Войн {unit_1.name} атакует, воин {unit_2.name} защищается')
		unit_1.protect(unit_2)
		if unit_2.health < 10:
			break
	elif action_1 == 0 and action_2 == 1:
		print(f'#Войн {unit_2.name} атакует, воин {unit_1.name} защищается')
		unit_2.protect(unit_1)	
		if unit_1.health < 10:
			break
	else:
		print('#Оба война ушли в защиту ...')
	i += 1

