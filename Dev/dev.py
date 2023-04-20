from random import randint

class Warrior():
	health = 100
	endurance = 100
	armor = 100
	def __init__(self, name):
		self.name = name

	def gen_action(self):
		return randint(0,1)

	def attack(self, other):
		self.endurance -= 10
		other.health -= 20



unit_1 = Warrior('Воин 1')


unit_2 = Warrior('Воин 2')


unit_1.attack(unit_2)

print(f'Здоровье {unit_2.name} - {unit_2.health}')
print(f'Выносливость {unit_1.name} - {unit_1.endurance}')