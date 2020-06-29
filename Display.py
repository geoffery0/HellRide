from dialogueText import *
from character import *
from location import *

def Display_Stats(player):
	printSlow("\n"+player.Classname + "\n" + "HP: " + str(player.HP) + "   Soul: " + str(player.Soul) + "   Ammo: " + str(player.Ammo) + "\nAtk: " + str(player.Atk) + "   Def: " + str(player.Def), .005 )

def Display_Abilities(Abil):
	printSlow("\nAbilities:")
	for index in Abil:
		single = Abilities(index)
		printSlow("Name: %-33s   Description: %s"%(single[0],single[1]),.005)

def Display_Skills(Skil):
	printSlow("\nSkills:")
	for index in Skil:
		single = Skills(index)
		printSlow("Name: %-33s   Description: %s"%(single[0],single[1]),.005)

def Display_Spells(Spel):
	printSlow("\nSpells:")
	for index in Spel:
		single = Spells(index)
		printSlow("Name: %-33s   Description: %s"%(single[0],single[1]),.005)

def Display_Guns(Gun):
	printSlow("\nGuns:")
	for index in Gun:
		single = Guns(index)
		printSlow("Name: %-33s   GunType: %-21s   Description: %s"%(single[0],single[1],single[2]),.005)

def Display_Location(Location):
	printSlow('{}:'.format(Location.name))