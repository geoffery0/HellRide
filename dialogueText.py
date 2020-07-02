import sys

from time import sleep

#str int -> prints
# takes a string and a number representing seconds and prints each letter after that many seconds
def printSlow(words = '', num = .015):
	words = str(words)
	for char in words:
		if char != ' ':
			sleep(num)
		print(char, end='', flush=True)
	print()
	


#str int --> str
#prints similarly to printSlow but also returns an input
def inputSlow(words = '', num = .015):

	for char in words:
		if char != ' ':
			sleep(num)
		print(char, end='', flush=True)
	put = input()
	put.strip()
	return put