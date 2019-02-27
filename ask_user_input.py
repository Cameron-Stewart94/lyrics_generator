def ask_user():
	# Funtion to ask user for song and artist input, and returns choices in dict
	artist_choice = input('Enter an Artist: ')
	song_choice = input('Enter a Song: ')

	return {'Artist' : artist_choice, 'Song': song_choice}


def ask_user_again():
    # Funtion asks user for more inputs until told to stop

    ask_again = True
    while ask_again == True:
        # Loop asks if user for input until valid input is entered

        choose_again = input('Choose another song?: ')
        choose_again = choose_again.lower()
        # Asks user wether they want to choose another song

        if choose_again == 'yes' or choose_again == 'y':
            another_choice = True
            ask_again = False
            # If user chooses yes, programme will run again and ask again loop stops

        elif choose_again == 'no' or choose_again == 'n':
            another_choice = False
            ask_again = False
            # If user chooses no, programme will not run again and ask again loop stops

        else:
            print('Invalid choice, try again.')
            # If user inputs invalid input, ask again loop runs again

    return another_choice
