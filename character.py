from random import randint
from dialogueText import *

class chtrcls():
	def __init__(self,gameclass,name):
		self.name = name
		if gameclass == 0:
			self.Classname = "Pure of Heart"
			self.Abil = [0,1,2]
			self.skills = [0,1,2,3]
			self.spells = [1,2,4,10,3]
			self.Guns = [0]
			self.HP = 1200
			self.Atk = 30
			self.Def = 60
			self.Soul = 20
			self.Ammo = 3
			self.CHP = self.HP
			self.CSoul = self.Soul
			self.CAmmo = self.Ammo
			
			

		elif gameclass == 1:
			self.Classname = "Dumb of Ass"
			self.Abil = [3,4,5,12]
			self.skills = [0,4,5,6]
			self.spells = [5,0,6,9,3]
			self.Guns = [1]
			self.HP = 800
			self.Atk = 35
			self.Def = 70
			self.Soul = 35
			self.Ammo = 4
			self.CHP = self.HP
			self.CSoul = self.Soul
			self.CAmmo = self.Ammo
		

		elif gameclass == 2:
			self.Classname = "Ass of Hole"
			self.Abil = [6,7,8]
			self.skills = [0,7,8,9]
			self.spells = [7,0,8,3]
			self.Guns = [2]
			self.HP = 900
			self.Atk = 45
			self.Def = 40
			self.Soul = 25
			self.Ammo = 4
			self.CHP = self.HP
			self.CSoul = self.Soul
			self.CAmmo = self.Ammo
		

		elif gameclass == -1:
			self.Classname = "Doom of Guy"
			self.Abil = [9,10,11]
			self.skills = [10,11]
			self.spells = [11]
			self.Guns = [4,6,5,7,8,9,10]
			self.HP = 1200
			self.Atk = 100
			self.Def = 60
			self.Soul = 3
			self.Ammo = 8
			self.CHP = self.HP
			self.CSoul = self.Soul
			self.CAmmo = self.Ammo

		self.LAbil = []
		self.Lskills = []
		self.Lspells = []
		self.LGuns = []
		self.mod = []

		for index in self.Abil:
			a = Abilities(index)
			self.LAbil.append(a[0])

		for index in self.skills:
			a = Skills(index)
			self.Lskills.append(a[0])

		for index in self.spells:
			a = Spells(index)
			self.Lspells.append(a[0])

		for index in self.Guns:
			a = Guns(index)
			self.LGuns.append(a[0])

		self.effect = None
		self.luck = False

	def check(self,action):
		if action == None:
			return None

		if action in '1 2 3 4 5 6 7 8 9 0 a s d f g h j k l q w e r t y u i o p z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M - ( ) ':
			return None

		if action in 'Rest':
			return 0

		if action in 'Trip':
			return 0

		if action in 'Contagious Goof':
			return 0

		if action in 'Flail':
			return 0

		if action in 'Pure Flash':
			return 0

		if action in '(X)plode':
			if self.CSoul < 5:
				return 'Not enough Soul'
			return 0

		if action in 'Minor heal':
			if self.CSoul < 3:
				return 'Not enough Soul'
			return 0

		if action in 'Psych':
			if self.CSoul < 4:
				return 'Not enough Soul'
			return 0

		if action in 'Cheat Life':
			if self.CSoul < 8:
				return 'Not enough Soul'
			return 0

		if action in 'Load Gun':
			if self.CSoul < 4:
				return 'Not enough Soul'
			return 0

		if action in '+1 Tommy Gun':
			if self.CAmmo < 1:
				return 'Not enough Ammo'
			return 0

		if action in 'Heal':
			if self.CSoul < 5:
				return 'Not enough Soul'
			return 0

		if action in 'Blast Flash':
			if self.CSoul < 3:
				return 'Not enough Soul'
			return 0

		if action in 'Def Buff' and self.Classname == 'Pure of Heart':
			return 0

		if action in 'Health Explosion':
			return 0

		if action in 'Vitality Drip':
			if self.CSoul < 5:
				return 'Not enough Soul'
			return 0

		if action in 'Bubble Skin':
			if self.CSoul < 4:
				return 'Not enough Soul'
			return 0

		if action in 'Pool Pistol':
			if self.CAmmo < 1:
				return 'Not enough Ammo'
			return 0

		if action in 'Fuck Up':
			return 0

		if action in 'Atk buff':
			return 0

		if action in 'Soul Siphon':
			return 0

		if action in 'Soular Burst':
			if self.CSoul < 7:
				return 'Not enough Soul'
			return 0

		if action in 'Def debuff':
			if self.CSoul < 4:
				return 'Not enough Soul'
			return 0

		if action in 'Vampiric Shotgun':
			if self.CAmmo < 1:
				return 'Not enough Ammo'
			return 0


	def attack(self,action):
		if action == None:
			return None

		if action in 'Rest':
			return self.Rest()

		if action in 'Trip':
			return self.Trip()

		if action in 'Contagious Goof':
			return self.Goof()

		if action in 'Flail':
			return self.Flail()

		if action in '(X)plode':
			return self.xplode()

		if action in 'Minor heal':
			return self.minor()

		if action in 'Psych':
			return self.Psych()

		if action in 'Cheat Life':
			return self.life()

		if action in 'Load Gun':
			return self.load()

		if action in '+1 Tommy Gun':
			return self.Tommy()

		if action in 'Heal':
			return self.Heal()

		if action in 'Pure Flash':
			return self.PFlash()

		if action in 'Blast Flash':
			return self.BFlash()

		if action in 'Def Buff' and self.Classname == 'Pure of Heart':
			return self.DBuff()

		if action in 'Health Explosion':
			return self.HealthX()

		if action in 'Vitality Drip':
			return self.Vitality()

		if action in 'Bubble Skin':
			return self.Bubble()

		if action in 'Pool Pistol':
			return self.PoolP()

		if action in 'Fuck Up':
			return self.FUp()

		if action in 'Atk buff':
			return self.ABuff()

		if action in 'Soul Siphon':
			return self.Siphon()

		if action in 'Soular Burst':
			return self.Soular()

		if action in 'Def debuff':
			return self.DDebuff()

		if action in 'Vampiric Shotgun':
			return self.VShotgun()





	def Rest(self):
		self.CSoul += 6
		if self.CSoul > self.Soul:
			self.CSoul = self.Soul
		return 0, 'Rest'

	def Trip(self):
		if randint(1,4) == 1:
			self.CAmmo += 1
			printSlow('You found some ammo!')
			if self.CAmmo > self.Ammo:
				self.CAmmo = self.Ammo
		elif type(self.luck) == int:
			self.CAmmo += 1
			if self.CAmmo > self.Ammo:
				self.CAmmo = self.Ammo

		return 50 , 'Trip'

	def Goof(self):
		return 'acc' , 'Contagious Goof'
		
	def Flail(self):
		if type(self.luck) == int:
			return randint(100,120) , 'Flail'
		return randint(1,120) , 'Flail'

	def xplode(self):
		
		self.CSoul -= 5
		if randint(1,5) == 5 and type(self.luck) != int:
			self.CHP -= self.HP//4
			if self.CHP <= 0:
				self.CHP = 1
		return 240 , '(X)plode'

	def minor(self):
		
		self.CSoul -= 3

		self.CHP += self.HP//5
		if self.CHP > self.HP:
			self.CHP = self.HP
		return 0 , 'Minor heal'

	def Psych(self):
		
		self.CSoul -= 4
		return 0 , 'Psych'

	def life(self):
		
		self.CSoul -= 8
		self.luck = 1
		return 0, 'Cheat Life'

	def load(self):
		
		self.CSoul -= 4
		self.CAmmo += 3
		if self.CAmmo > self.Ammo:
			self.CAmmo = self.Ammo
		return 0, 'Load Gun'

	def Tommy(self):
		damage = 0
		self.CAmmo -= 1
		if type(self.luck) == int:
			return randint(20,25) * 17 , '+1 Tommy Gun'
		for spray in range(randint(0,5)):
			damage += randint(1,5)*17
		return damage , '+1 Tommy Gun'

	def Heal(self):
		
		self.CSoul -= 5

		self.CHP += (self.HP*35)//100
		if self.CHP > self.HP:
			self.CHP = self.HP
		return 0 , 'Heal'

	def PFlash(self):
		self.CSoul += 1
		if self.CSoul > self.Soul:
			self.CSoul = self.Soul
		return 60 , 'Pure Flash'

	def BFlash(self):
		self.CSoul -= 3
		return 180 , 'Blast Flash'

	def DBuff(self):
		new = self.Def//3 
		self.Def += new
		self.mod.append(('2Def:33%',new))
		return 0 , 'Def buff'

	def HealthX(self):
		percent = None
		while percent == None:
			percent = inputSlow('How much life do you want to use?(Percent as a whole number): ')
			try:
				percent = int(percent)
				if percent >= (self.CHP/self.HP)*100:
					percent = (self.CHP//self.HP)*100 - 1
				if percent < 0:
					percent = 0
			except:
				pass
		damage = (self.CHP*percent)//100
		self.HP -= damage
		return (3000 * percent)//100, 'Health Explosion'

	def Vitality(self):
		self.CSoul -= 5
		self.CHP += round(self.HP*.10)
		if self.CHP > self.HP:
			self.CHP = self.HP
		self.mod.append(('Vitality', 5))

		return 0,'Vitality Drip'

	def Bubble(self):
		self.CSoul -= 4
		self.effect = ['Bubble', round(self.HP*.15)]

		return 0 , 'Bubble Skin'

	def PoolP(self):
		self.CAmmo -= 1
		self.CSoul += 3
		if self.CSoul > self.Soul:
			self.CSoul = self.Soul
		return 340 , 'Pool Pistol'

	def FUp(self):
		return 100 , 'Fuck Up'

	def ABuff(self):
		new = round(self.Atk*.25) 
		self.Atk += new
		self.mod.append(['ABuff', 2 , new])
		return 0 , 'Atk buff'

	def Siphon(self):
		return 'Siphon' , 'Soul Siphon'

	def Soular(self):
		self.CSoul -= 7
		return 450 , 'Soular Burst'

	def DDebuff(self):
		self.CSoul -= 4
		return 'DDebuff' , 'Def debuff'
	
	def VShotgun(self):
		self.CAmmo -= 1
		return 'VShotgun' , 'Vampiric Shotgun'






	def mods(self):
		delete = []
		if type(self.luck) != bool:
			self.luck -= 1
			print(self.luck)
			if self.luck == -1:
				self.luck = False
		for change in range(len(self.mod)):
			if type(self.mod[change]) == tuple:
				if self.mod[change][0] == '2Def:33%':
					self.mod[change] = ('1Def:33%',self.mod[change][1])

				elif self.mod[change][0] == '1Def:33%':
					self.mod[change] = ('0Def:33%',self.mod[change][1])

				elif self.mod[change][0] == '0Def:33%':
					self.Def -= self.mod[change][1]
					delete.append(change)

				if self.mod[change][0] == 'vitality':
					if self.mod[change][1] == 0:
						delete.append(change)

					else:
						self.mod[change][1] -= 1
						self.CHP += round(self.HP*.10)
						if self.CHP > self.HP:
							self.CHP = self.HP

				if self.mod[change][0] == 'ABuff':
					if self.mod[change][1] == 0:
						self.Atk -= self.mod[change][2]
						delete.append(change)
					else:
						self.mod[change][1] -= 1

		for thing in delete:
			del self.mod[thing]



	def AM(self, attack):
		if 6 in self.Abil:
			if randint(1,9) < 3:
				return attack*1.2
		return attack

	def Clean(self):
		for change in range(len(self.mod)):
			if type(self.mod[change]) == tuple:
				if self.mod[change][0] == '2Def:33%' or self.mod[change][0] == '1Def:33%' or self.mod[change][0] == '0Def:33%':
					self.Def -= self.mod[change][1]













		



def Abilities(index):

	if index == 0:
		name = "Regeneration"
		desc = "Regenerate 25 HP every turn."
		return [name,desc]

	elif index == 1:
		name = "Pheonix Soul"
		desc = "If HP goes to 0, once per battle, you will ressurect with 50% health."
		return [name,desc]

	elif index == 2:
		name = "Health Boost"
		desc = "Boosts healing and health based moves."
		return [name,desc]

	elif index == 3:
		name = "Soothing Spells"
		desc = "Chance to heal when casting spells."
		return [name,desc]

	elif index == 4:
		name = "Rollback Spells"
		desc = "Chance to heal MP when casting spells."
		return [name,desc]

	elif index == 5:
		name = "Busty Mumbo Jumbo"
		desc = "Chance to increase power of spells."
		return [name,desc]

	elif index == 6:
		name = "Angry Monkey"
		desc = "Chance to increase damage of attack."
		return [name,desc]

	elif index == 7:
		name = "A Bad Game of Russian Roulette"
		desc = "Last ammo instantly kills enemy."
		return [name,desc]

	elif index == 8:
		name = "Last hurrah"
		desc = "If HP drops to 0, one last turn is taken, if the enemy dies in the next turn then you survive the battle."
		return [name,desc]

	elif index == 9:
		name = "Argent Energy"
		desc = "All perminent stat boosting items increase HP, Def and ammo"
		return [name,desc]

	elif index == 10:
		name = "Destruction Empowerment"
		desc = "Every enemy killed during current battle increases Atk by 5%"
		return [name,desc]

	elif index == 11:
		name = "Weapon Mastery"
		desc = "Increases damage from guns by 15%"
		return [name,desc]

	elif index == 12:
		name = "Cheat Death"
		desc = "Chance to survive when HP reaches 0%"
		return [name,desc]



def Skills(index):

	if index == 0:
		name = "Rest - +6 Soul"
		desc = "Regenerates 6 Soul"
		return [name,desc]

	elif index == 1:
		name = "Def buff"
		desc = "Strengthens defense temporarily"
		return [name,desc]

	elif index == 2:
		name = "Pure Flash"
		desc = "Damaging move, recovers 1 MP"
		return [name,desc]

	elif index == 3:
		name = "Health Explosion"
		desc = "Deals damage using health"
		return [name,desc]

	elif index == 4:
		name = "Trip - 50 BP"
		desc = "Damaging move, chance to pick up ammo"
		return [name,desc]

	elif index == 5:
		name = "Contagious Goof"
		desc = "Lowers enemy accuracy for two turns"
		return [name,desc]

	elif index == 6:
		name = "Flail - 1-120 BP"
		desc = "Wildly variable damage"
		return [name,desc]

	elif index == 7:
		name = "Fuck Up"
		desc = "Deals a good amount damage"
		return [name,desc]

	elif index == 8:
		name = "Atk buff"
		desc = "Temporarily increases attack power"
		return [name,desc]

	elif index == 9:
		name = "Soul Siphon"
		desc = "Steals Soul from enemy and deals light damage"
		return [name,desc]

	elif index == 10:
		name = "Melee"
		desc = "Good damage - If enemy health after damage is less than 25% then Rip & Tear is activated"
		return [name,desc]

	elif index == 11:
		name = "Rip & Tear"
		desc = "If enemy has less than 25% HP then the enemy is instantly killed and HP is gained in ratio to how much health is left"
		return [name,desc]



def Spells(index):
	
	if index == 0:
		name = "Minor heal +20% HP - Cost: 3 Soul"
		desc = "Heals 20% HP - 3 Soul"
		return [name,desc]

	elif index == 1:
		name = "Heal"
		desc = "Heals 35% HP - 5 Soul"
		return [name,desc]

	elif index == 2:
		name = "Blast Flash"
		desc = "A more powerful flash - 3 Soul"
		return [name,desc]

	elif index == 3:
		name = "Load Gun - Cost: 4 Soul"
		desc = "Regenerates 3 ammo - 4 Soul"
		return [name,desc]

	elif index == 4:
		name = "Vitality Drip"
		desc = "Regenerates HP over time - 5 Soul"
		return [name,desc]

	elif index == 5:
		name = "(X)plode 240 BP - Cost: 5 Soul"
		desc = "Deals great damage, chance to hurt self - 5 Soul"
		return [name,desc]

	elif index == 6:
		name = "Psych - Cost: 4 Soul DOES NOTHING"
		desc = "Gives a random buff/debuff to self - 4 Soul"
		return [name,desc]

	elif index == 7:
		name = "Def debuff"
		desc = "Permanently lowers enemies Def - 4 Soul"
		return [name,desc]

	elif index == 8:
		name = "Soular Burst"
		desc = "Massive damage - 7 Soul"
		return [name,desc]

	elif index == 9:
		name = "Cheat Life - Cost: 8 Soul"
		desc = "Next turn all good probabilities will be 100% - 8 Soul"
		return [name,desc]

	elif index == 10:
		name = "Bubble Skin"
		desc = "Creates a shield for 15% HP that blocks incoming attacks - 4 Soul"
		return [name,desc]

	elif index == 11:
		name = "Chainsaw"
		desc = "instantly kills and enemy - Drops lots of ammo - 1-5 Soul depending on strength of enemy"
		return [name,desc]

	



def Guns(index):

	if index == 0:
		name = "Pool Pistol"
		guntype = "Sidearm, Basic weapon"
		desc = "Single shot - heals 3 Soul"
		return [name,guntype,desc]

	elif index == 1:
		name = "+1 Tommy Gun"
		guntype = "Auto, Basic weapon"
		desc = "Shoots 0-5 Sprays with each spray shooting 1-5 bullets"
		return [name,guntype,desc]

	elif index == 2:
		name = "Vampiric Shotgun"
		guntype = "Shotgun, Basic weapon"
		desc = "Tight spread - heals 25% of damage dealt"
		return [name,guntype,desc]

	elif index == 3:
		name = ".45 Magnnum"
		guntype = "Revolver"
		desc = "Chance to headshot dealing massive damage"
		return [name,guntype,desc]

	elif index == 4:
		name = "Combat Shotgun"
		guntype = "Shotgun"
		desc = "Tight spread - High damage"
		return [name,guntype,desc]

	elif index == 5:
		name = "Super Shotgun"
		guntype = "Shotgun"
		desc = "Needs to be reloaded every 2 Shells - Massive damage"
		return [name,guntype,desc]

	elif index == 6:
		name = "Frag Grenade"
		guntype = "Misc"
		desc = "Deals damage to all enemies"
		return [name,guntype,desc]
	
	elif index == 7:
		name = "Gauss Cannon"
		guntype = "Energy"
		desc = "Instantly kills small-medium enemies - Massive damage"
		return [name,guntype,desc]

	elif index == 8:
		name = "Heavy Assault Rifle"
		guntype = "Auto"
		desc = "Great damage shoots 5-10 bullets"
		return [name,guntype,desc]

	elif index == 9:
		name = "Rocket Launcher"
		guntype = "Rocket"
		desc = "Deals massive damage to one target and great damage to all adjacent targets - chance to hurt self"
		return [name,guntype,desc]

	elif index == 10:
		name = "BFG9000"
		guntype = "Big Fucking Gun"
		desc = "Instantly kills enemies small-large - Extreme damage"
		return [name,guntype,desc]

	elif index == 11:
		name = "The Nemex"
		guntype = ("Sidearm" , "Energy")
		desc = "Instantly kills enemies small-medium - High damage"
		return [name,guntype,desc]

	elif index == 12:
		name = "Ingram-40 Fletchette Pistol"
		guntype = "Sidearm"
		desc = "Fires magnetic rounds that come back to the mag after fired. Instantly kills small enemies - Great damage"
		return [name,guntype,desc]