from random import randint

class Angel():
	"""docstring for Enemy"""
	def __init__(self):
		self.name = 'Angel'
		self.HP = 500
		self.Soul = 10
		self.CHP = self.HP
		self.CSoul = self.Soul
		self.Atk = 30
		self.Def = 30
		self.size = 'Medium'
		self.mod = 1
		self.effect = None

	def attack(self):
		if self.mod != 1:
			self.count -= 1
			if self.count == 0:
				self.mod = 1

		if self.CSoul < 2:
			return 20 * self.mod , 'Smite'
		else:
			chance = (self.CSoul/self.Soul) * 100
			if chance > 65:
				chance = 65
			elif chance < 25:
				chance = 25
			if randint(1,100) > chance:
				return 20 * self.mod , 'Smite'

			else:
				if self.CSoul < 4:
					self.mod *= 2
					self.count = 3
					self.CSoul -= 2
					return 0, 'Enflame'
				else:
					if randint(1,9) > 5:
						self.mod *= 2
						self.count = 3
						self.CSoul -= 2
						return 0, 'Enflame'
					else:
						self.CSoul -= 4
						return 70 * self.mod , 'Burn'
			


class MAngel():
	"""docstring for Enemy"""
	def __init__(self):
		self.name = 'Mangled Construct'
		self.HP = 500
		self.Soul = 10
		self.CHP = self.HP
		self.CSoul = self.Soul
		self.Atk = 30
		self.Def = 30
		self.size = 'Medium'
		self.mod = 1
		self.effect = None

	def attack(self):
		if self.mod != 1:
			self.count -= 1
			if self.count == 0:
				self.mod = 1

		if self.CSoul < 2:
			return 20 * self.mod , 'Slash'
		else:
			chance = (self.CSoul/self.Soul) * 100
			if chance > 65:
				chance = 65
			elif chance < 25:
				chance = 25
			if randint(1,100) > chance:
				return 20 * self.mod , 'Slash'

			else:
				if self.CSoul < 4:
					self.mod *= 2
					self.count = 3
					self.CSoul -= 2
					return 0, 'Glitch'
				else:
					if randint(1,9) > 5:
						self.mod *= 2
						self.count = 3
						self.CSoul -= 2
						return 0, 'Glitch'
					else:
						self.CSoul -= 4
						return 40 * self.mod , 'Electrocute'

class Spirit():
	"""docstring for Enemy"""
	def __init__(self):
		self.name = 'Spirit'
		self.HP = 300
		self.Soul = 20
		self.CHP = self.HP
		self.CSoul = self.Soul
		self.Atk =20
		self.Def = 10
		self.size = 'Small'
		self.mod = 1
		self.effect = None

	def attack(self):
		if self.CSoul < 3:
			return 20 * self.mod , 'Wail'
		chance = (self.CSoul/self.Soul) * 100
		if chance > 75:
			chance = 75
		elif chance < 25:
			chance = 25
		if randint(1,100) > chance:
			return 20 * self.mod , 'Wail'
		else:
			return 50 * self.mod , 'Project'


class GOD():
	"""docstring for Enemy"""
	def __init__(self):
		self.name = 'GOD'
		self.HP = 200000
		self.Soul = 1000040
		self.CHP = self.HP
		self.CSoul = self.Soul
		self.Atk = 40
		self.Def = 50
		self.size = 'Massive'
		self.mod = 1
		self.effect = None

	def attack(self):
		pass

class Archangel():
	"""docstring for Enemy"""
	def __init__(self):
		self.HP = 1500
		self.Soul = 35
		self.CHP = self.HP
		self.CSoul = self.Soul
		self.Atk = 35
		self.Def = 40
		self.size = 'Large'
		self.mod = 1
		self.effect = None


class Gabriel(Archangel):
	"""docstring for Gabriel"""
	def __init__(self):
		super().__init__()
		self.name = 'Gabriel'

	def attack(self):
		pass
		
class Micheal(Archangel):
	"""docstring for Micheal"""
	def __init__(self):
		super().__init__()
		self.name = 'Micheal'

	def attack(self):
		pass

class Raphael(Archangel):
	"""docstring for Raphael"""
	def __init__(self):
		super().__init__()
		self.name = 'Raphael'

	def attack(self):
		pass		

class Uriel(Archangel):
	"""docstring for Uriel"""
	def __init__(self):
		super().__init__()
		self.name = 'Uriel'

	def attack(self):
		pass

