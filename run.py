from markov_chain_lyrics import *


def ask_user():
	# Function asks user for lyrics or Markov Chains

	markov_chain_choices = ['markov chain', 'markov', 'mc', 'chain', 'markov chains', 'markovchain', 'markovchains', 'markov_chain', 'markov_chains']
	lyrics_choices = ['lyrics', 'lyric', 'l']
	# List of accepted inputs
	
	ask_again = True
	# Initialises while loop

	while ask_again == True:
		# While loop asks for input until accepted input is eneterd

		user_choice = input('Choose Markov Chains or Lyrics: ')
		user_choice = user_choice.lower()
		# Formats user input

		if user_choice in markov_chain_choices:
			markov_chain()
			ask_again = False

		elif user_choice in lyrics_choices:
			normal_lyrics()
			ask_again = False

		else:
			print('Invalid choice, try again. ')
		# Pick funtion user chooses

	
	another_choice = True
		# Initialises loop for second choice

	while another_choice == True:
		# Loop asks for input until accepted input is entered

		choose_again = input('Choose another song?: ')
		choose_again = choose_again.lower()

		if choose_again == 'yes' or choose_again == 'y':
			ask_user()

		elif choose_again == 'no' or choose_again == 'n':
			another_choice = False

		else:
			print('Invalid choice, try again.')
		# Allows user to pick another song

	return

ask_user()