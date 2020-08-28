from Battle import *


def Move(player):
	while True == True:
		printSlow('\n\n{}:\n'.format(player.Location.room))
		if randint(1,100) <= player.Location.rates:
			strife(player,player.Location.area)
			printSlow()
		
		if player.Location.north != None:
			printSlowLoop('North: {}    '.format(player.Location.north.room))
		if player.Location.west != None:
			printSlowLoop('West: {}    '.format(player.Location.west.room))
		if player.Location.east != None:
			printSlowLoop('East: {}    '.format(player.Location.east.room))
		if player.Location.south != None:
			printSlowLoop('South: {}'.format(player.Location.south.room))
		printSlow()
		select = None
		while select == None:
			printSlow('GAME: Which way do you want to go?')
			select = inputSlow('Direction: ')
			if select in ['n','north','N','North'] and player.Location.north != None:
				player.Location = player.Location.north
			elif select in ['s','south','S','South'] and player.Location.south != None:
				player.Location = player.Location.south
			elif select in ['e','east','E','East'] and player.Location.east != None:
				player.Location = player.Location.east
			elif select in ['w','west','W','West'] and player.Location.west != None:
				player.Location = player.Location.west
			elif select in ['end','End']:
				quit()
			else:
				select = None