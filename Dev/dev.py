#Защита при атаке - <атакующий>.protect_attack(<защищающийся>)	
	def protect_attack(self, other):
		if self.endurance > 10:
			self.endurance -= 10
			dam_armor = randint(0,10)
			if (other.armor - dam_armor) > 0:
				other.armor -= dam_armor
				dam_health = randint(0,20)
				print(f'Урон броне - {dam_armor}')
			else:
				other.armor = 0	
				dam_health = randint(10,30)
			if (other.health - dam_health) > 10:
				other.health -= dam_health
			elif (other.health - dam_health) < 0:
				print(f'Войну {other.name} нанесен смертельный удар. Он проигрывает бой!')
				other.health = 0
			else:
				other.health -= dam_health
		else:
			dam_armor = randint(0,10)
			if (other.armor - dam_armor) > 0:
				other.armor -= dam_armor
				dam_health = randint(0,10)
			else:
				other.armor = 0	
				dam_health = randint(0,20)
			if (other.health - dam_health) > 10:
				other.health -= dam_health
			elif (other.health - dam_health) < 0:
				print(f'Войну {other.name} нанесен смертельный удар. Он проигрывает бой!')
				other.health = 0
			else:
				other.health -= dam_health