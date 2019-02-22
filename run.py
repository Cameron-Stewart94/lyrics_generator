from get_lyrics import *


def ask_user():
	# Function asks user for lyrics or Markov Chains

	normal_lyrics()
	#Calls normal_lyrics function from get_lyrics




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
