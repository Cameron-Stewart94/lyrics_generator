def ask_user():
	# Funtion to ask user for song and artist input, and returns choices in dict
	artist_choice = input('Enter an Artist: ')
	song_choice = input('Enter a Song: ')

	return {'Artist' : artist_choice, 'Song': song_choice}


def ask_user_again():
	# Funtion asks user for more inputs until told to stop

    ask_again = True
    while ask_again == True:
		# Loop asks for input until accepted input is entered

		choose_again = input('Choose another song?: ')
		choose_again = choose_again.lower()

		if choose_again == 'yes' or choose_again == 'y':
			another_choice = True
            ask_again = False

		elif choose_again == 'no' or choose_again == 'n':
			another_choice = False
            ask_again = False

		else:
			print('Invalid choice, try again.')
		# Allows user to pick another song

	return
