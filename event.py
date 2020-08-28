from dialogueText import *
from random import randint


def ultimaAtk(event,turns,mobs,player):
	if event == "Tutorial":
		if turns == 1:
			printSlow("\nGAME: HP is how much damage you can take before you can no longer fight\nGAME: Soul is how much energy you can use before you die, using Projections use Soul and resting will replenish it \nGAME: Ammo is how much ammunition you have projected for your weapons, using guns will deplete your ammo and you will have to project more\nGAME: Strength tells you the fighting shape youre in, the less Soul you have the weaker you will be\n",.005)
		else:
			pass


def BeforeAtk(event,turns,mobs,player):
	if event == None:
		return

	if event == "Tutorial":
		if turns == 1:
			printSlow("\nGAME: To choose a type of action, either write out the entire word(Ctrl + c,Ctrl + v) or type the first two letters lowercase\n",.005)
		else:
			pass



def AfterAtk(event,turns,mobs,player):
	if event == None:
		return

	if event == "Tutorial":
		pass



def ChoiceAtk(event,turns,mobs,player,choice):
	if event == None:
		return

	if event == "Tutorial":
		if turns == 1:
			printSlow("GAME: Type the name of the move that you want to use (Case sensitive - Copying it will yield best results)\nGAME: If you type an incomplete move the game will guess what move you were trying to use\nGAME: Typing 'Back' or 'back' will return you to the previous selection\n",.005)

		if choice == 'skills':
			printSlow("GAME: These are your skills, they are unique to this class and cost nothing to use, however they are weaker than other moves\n",.005)

		if choice == 'projections':
			printSlow('GAME: These are your Projections, they require Soul to use but are versitle and strong in return\nGAME: Be careful though, if you use too much Soul you will be weakened!\n',.005)

		if choice == 'guns':
			printSlow('GAME: These are your guns, they are your most powerful attacks that you have but they are expensive to use\n',.005)
	pass


