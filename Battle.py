from location import *
from enemies import *
from random import randint
from dialogueText import *
from character import *
heaven = Location(0)

#int,None/int --> list of objects
#takes an area code and uses to determine how many and what kind of enemies will spawn
def spawn(area, count = 0):
	mobs = []
	if count == 0:
		count = randint(1,3)
	if area == 0:
		ran = randint(1,100)
		if ran < 30:
			mobs.append(Angel())
		if ran == 30:
			mobs.append(MAngel())
		if ran > 30:
			mobs.append(Spirit())
		count -= 1
		if count != 0:
			return mobs + spawn(area, count)
		return mobs



def Display_enemies(mobs):
	if len(mobs) == 3:
		printSlow("{:25}{:25}{:25}".format(mobs[0].name, mobs[1].name, mobs[2].name),.005)
		printSlow("HP:{}/{:<18}HP:{}/{:<18}HP:{}/{:<18}".format(mobs[0].CHP,mobs[0].HP, mobs[1].CHP,mobs[1].HP, mobs[2].CHP,mobs[2].HP),.005)
		printSlow("Soul:{}/{:<17}Soul:{}/{:<17}Soul:{}/{:<17}".format(mobs[0].CSoul,mobs[0].Soul, mobs[1].CSoul,mobs[1].Soul, mobs[2].CSoul,mobs[2].Soul),.005)

	if len(mobs) == 2:
		printSlow("{:25}{:25}".format(mobs[0].name, mobs[1].name),.005)
		printSlow("HP:{}/{:<18}HP:{}/{:<18}".format(mobs[0].CHP,mobs[0].HP, mobs[1].CHP,mobs[1].HP),.005)
		printSlow("Soul:{}/{:<17}Soul:{}/{:<17}".format(mobs[0].CSoul,mobs[0].Soul, mobs[1].CSoul,mobs[1].Soul),.005)

	if len(mobs) == 1:
		printSlow("{}".format(mobs[0].name),.005)
		printSlow("HP:{}/{}".format(mobs[0].CHP,mobs[0].HP),.005)
		printSlow("Soul:{}/{}".format(mobs[0].CSoul,mobs[0].Soul),.005)

def Display_player(player):
	printSlow()
	printSlow("{}".format(player.name),.005)
	printSlow("HP:{}/{}".format(player.CHP,player.HP),.005)
	printSlow("Soul:{}/{}".format(player.CSoul,player.Soul),.005)
	printSlow("Ammo:{}/{}".format(player.CAmmo,player.Ammo),.005)
	
def Display_Battle_Skills(player):
	for move in player.Lskills:
		printSlow(move,.005)

def Display_Battle_Projections(player):
	for move in player.Lspells:
		printSlow(move,.005)

def Display_Battle_Guns(player):
	for move in player.LGuns:
		printSlow(move,.005)

def Player_choice(player,mobs):
	k = -1
	s = -1
	m = -1
	select = None
	Display_player(player)
	printSlow()

	while s == -1 or player.check(select) == None or player.check(select) == 'Not enough Soul' or player.check(select) == 'Not enough Ammo':
		if player.check(select) == 'Not enough Soul' or player.check(select) == 'Not enough Ammo':
			printSlow('{} for that attack!'.format(player.check(select)),.005)
			printSlow()
		choice = inputSlow('Action: Skills, Projections, Guns\n')
		printSlow()

		if 'sk' in choice or 'Skills' in choice or 'skills' in choice:
			while k == -1:
				Display_Battle_Skills(player)
				printSlow()
				select = inputSlow('Skill: ')
				if select == 'back' or select == 'Back':
					break
				for skill in player.Lskills:
					if select in skill:
						k = 0
						s = 0
						if select in 'Rest':
							m = 0
							target = -1


		elif 'pr' in choice or 'Projections' in choice or 'projections' in choice:
			while k == -1:
				Display_Battle_Projections(player)
				printSlow()
				select = inputSlow('Projection: ')
				if select == 'back' or select == 'Back':
					break
				for spell in player.Lspells:
					if select in spell:
						k = 0
						s = 0
						if select in 'Minor heal' or select in 'Cheat Life' or select in 'Load Gun':
							m = 0
							target = -1

		elif 'gu' in choice or 'Guns' in choice or 'guns' in choice:
			while k == -1:
				Display_Battle_Guns(player)
				printSlow()
				select = inputSlow('Gun: ')
				if select == 'back' or select == 'Back':
					break2
				for Gun in player.LGuns:
					if select in Gun:
						k = 0
						s = 0
		else :
			s = -1

	while m == -1:

		if len(mobs) == 1:
			target = 0
			m = 0

		elif len(mobs) == 2:
			target = inputSlow('Target(1,2): ')
			if target in ['1','2']:
				m = 0
				target = int(target) - 1

		elif len(mobs) == 3:
			target = inputSlow('Target(1,2,3): ')
			if target in ['1','2','3']:
				m = 0
				target = int(target) - 1

	return target , select


def strife(player, area = heaven.area):
	mobs = spawn(area)
	while len(mobs) != 0:
		if player.luck != False:
			player.luck -= 1
			print(player.luck)
			if player.luck == -1:
				player.luck = False
		printSlow()
		Display_enemies(mobs)
		target , select = Player_choice(player,mobs)

		if target != -1:
			attack , select = player.attack(select)
			if type(target) == int:
				if type(attack) == int: 
					damage = (attack*player.Atk) // mobs[target].Def
					mobs[target].CHP -= damage
					if mobs[target].CHP <= 0:
						printSlow()
						printSlow('{} used {} and dealt {} damage which killed the {}!'.format(player.name,select, damage, mobs[target].name), .005)
						del mobs[target]
						
					else:
						printSlow()
						printSlow('{} used {} and dealt {} damage to the {}!'.format(player.name,select, damage,mobs[target].name), .005)
				elif attack == 'acc':
					mobs[target].effect = 'acc'
					printSlow("{} used {} and lowered the {}'s accuracy!".format(player.name,select, mobs[target].name), .005)

		elif target == -1:
			attack , select = player.attack(select)
			printSlow('{} used {}!'.format(player.name,select), .005)

		if len(mobs) != 0:
			for mob in mobs:
				attack, Atkname = mob.attack()
				damage = (attack* mob.Atk) // player.Def
				if mob.effect == 'acc':
					if randint(1,2) == 2:
						damage = 0
				player.CHP -= damage
				if player.CHP <= 0:
					
					printSlow('The {} used {} and dealt {} damage which killed {}!'.format(mob.name,Atkname, damage, player.name), .005)
					input()
					quit()
				else:
					
					printSlow('{} used {} and dealt {} damage!'.format(mob.name,Atkname, damage), .005)








player = chtrcls(1,'Jake')

strife(player)



