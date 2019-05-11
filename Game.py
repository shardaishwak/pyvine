from random import randint

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vocals = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l","m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

class Game:
	def __init__(self):
		self.running = True

	def start(self):
		last_pos = 0
		len_word = 0
		letters_guessed = 0
		counter = 0

		length_word_str = input("? What is the length of the word?: ")
		
		try:
			len_word_check = int(length_word_str)
			len_word = len_word_check
		except ValueError:
			print("! The value must be a number")

		#	Game starts only if the length of the word is greater that 0
		if len_word > 0:
			#	Put the _ in the array and when he guess the word, it will select that array and put it in it.
			printer_arr_init = []
			for i in range(0, len_word):
				printer_arr_init.append("_")

			printer_init = ''.join(map(str, printer_arr_init))
			print(f"\n+ Your letters are: {printer_init}\n")

			
			# Loop in the game, it will ask qquestions while he doesn't guess all!
			while letters_guessed < len_word:

				#	Algorithm for fast indovining
				random_guess = randint(0,len(alphabet) - 1)
				if counter > 0:
					if alphabet[last_pos] in consonants:
						random_vocal = randint(0, len(vocals) - 1)
						ask = input(f"? Does your word contain {vocals[random_vocal]}? [Y/N]: ")
					elif alphabet[last_pos] in vocals:
						random_consonant = randint(0, len(consonants) - 1)
						ask = input(f"? Does your word contain {consonants[random_consonant]}? [Y/N]: ")
				else:
					ask = input(f"? Does your word contain {alphabet[random_guess]}? [Y/N]: ")

				if ask ==  "y":
					ask_pos = input(f"? What is it's position from 1-{len_word}?: ")
					ask_pos = int(ask_pos)
					last_pos = ask_pos - 1
					printer_arr_init[ask_pos - 1] = alphabet[random_guess]
					letters_guessed += 1
					
					printer_init = ''.join(map(str, printer_arr_init))
					print(f"\n+ Your letters are: {printer_init}\n")
				elif ask == "n":
					print("Again!")
				elif ask == "quit":
					break;
				counter += 1
				print(f"Counter = {counter}")

			if letters_guessed == len_word:
				print("I won hurray!")
				print(f"\nYour word is: {printer_init}")

		else:
			print("! The length should be at least 1 character long")



