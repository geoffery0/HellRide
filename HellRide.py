#why are you looking here
#code written by geoffery6ix
#I mean if youre here you might as well peep my game. oh wait.
from dialogueText import *
from character import *
from Display import *


printSlow("Beta: What's up shitlips? Welcome to The Ride.")
printSlow()
gamername = "|"
while gamername == "|":
	gamername = inputSlow('Beta: Gimme your name: ')
	choice = inputSlow("GAME: Are you sure?(YES or NO) ")
	if (choice != "YES") and (choice != "yes"):
		gamername = "|"
printSlow()
printSlow("Beta: Buckle up %s we're already balls deep" %(gamername))
printSlow()
printSlow('GAME: You see pearly white gates ahead of you,')
printSlow("      you can't be certain but you think they may be THE Pearly White Gates.")
printSlow()
printSlow('GAME: An explosion booms in front of you, cracks spread upwards along its pearly surface.')
printSlow()
choice = inputSlow('GAME: Are you sure you want to do this? (YES or NO): ')
if choice == 'NO':
	quit()
elif choice != 'YES' and choice != 'yes':
	printSlow()
	printSlow('Beta: What the fuck are you on about over there')
	printSlow('Beta: %s my ass' %(choice))
printSlow()
printSlow('GAME: you have said: %s which calculates to be approximately...........' %(choice))
printSlow('\n      Lets fuckin do this')
printSlow()
printSlow('geo: For a better experience listen to this: https://youtu.be/b2YG8DX0ees')
printSlow('geo: If you are in fact a pansie you can listen to this: https://youtu.be/SC0RnPbP_pc')
printSlow()
printSlow("geo: Oh yeah before we get too far I'm the developer! ")
printSlow("geo: My name is geoffery6ix but you can call me geo")
printSlow("geo: Thank you for playing my game, I know it isn't finished yet but it's my first game so please be patient")
printSlow("geo: If you have any suggestions or run into any bugs please let me know!")
printSlow()
printSlow("geo: For the purpose of this demo there will be 3 classes:")
printSlow()
printSlow("GAME: Choose your class (Pure of Heart, Dumb of Ass, Ass of Hole)")
gameclass = ""
doom = 0
while gameclass == "":
	if inputSlow("GAME: Are you Pure of Heart? (YES or NO): ") == "YES":
		gameclass = 0
		player = chtrcls(gameclass,gamername)

		Display_Stats(player)
		Display_Abilities(player.Abil)
		Display_Skills(player.skills)
		Display_Spells(player.spells)
		Display_Guns(player.Guns)
		gameclass = ""
		if inputSlow("\nGAME: Are you sure? (YES or NO): ") == 'YES':
			gameclass = 0
			break
	if inputSlow("GAME: Are you Dumb of Ass? (YES or NO): ") == "YES":
		gameclass =  1
		player = chtrcls(gameclass,gamername)

		Display_Stats(player)
		Display_Abilities(player.Abil)
		Display_Skills(player.skills)
		Display_Spells(player.spells)
		Display_Guns(player.Guns)
		gameclass = ""
		if inputSlow("\nGAME: Are you sure? (YES or NO): ") == 'YES':
			gameclass = 1
			break
	if inputSlow("GAME: Are you Ass of Hole? (YES or NO): ") == "YES":
		gameclass =  2
		player = chtrcls(gameclass,gamername)
		Display_Stats(player)
		Display_Abilities(player.Abil)
		Display_Skills(player.skills)
		Display_Spells(player.spells)
		Display_Guns(player.Guns)
		gameclass = ""
		if inputSlow("\nGAME: Are you sure? (YES or NO): ") == 'YES':
			gameclass = 2
			break
	if doom == 2:
		printSlow()
		printSlow("you load your shotgun with malicious intent.", .05)
		gameclass = -1
	doom+=1

player = chtrcls(gameclass,gamername)
player.lvl = 1

Display_Stats(player)
Display_Abilities(player.Abil)
Display_Skills(player.skills)
Display_Spells(player.spells)
Display_Guns(player.Guns)
area = Location(0)
printSlow()
printSlow()
Display_Location(area)
inputSlow()