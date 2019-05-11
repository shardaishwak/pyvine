from pprint import pprint
from Hashon import Encoder
from Game import Game

question = input("What do you want to do: ")

list_of_hashes = []

if question == "hash":

	code = input("Code: ")

	hasher = Encoder(code, list_of_hashes)
	hasher.encode()

elif question == "list of hashes":
	if list_of_hashes:
		pprint(list_of_hashes)
	else:
		print("No hash found")

elif question == "play":
	game = Game()

	print("---------------------------------------\n")
	print("Game 2019. Version 1.0.0 \n")
	print("Welcome to my first python game. It consists in indovining the word you are thinking, by just giving the length of the word. Hope you enjoy it. \n")
	print("---------------------------------------\n")

	sq = input("Are you ready to play? (y/n): ")
	if sq == "y":
		game.start()
	else:
		print("Ok the next time!")
	

else:
	print("No command found")



