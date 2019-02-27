from song_lyrics import *

def ask_user():
	# Funtion to ask user for song and artist input, and returns choices in dict
	artist_choice = input('Enter an Artist: ')
	song_choice = input('Enter a Song: ')

	return {'Artist' : artist_choice, 'Song': song_choice}


def ask_user_again():
	# Funtion asks user for more inputs until told to stop


	another_choice = True
	while another_choice == True:
		# Loop asks for input until accepted input is entered

		choose_again = input('Choose another song?: ')
		choose_again = choose_again.lower()

		if choose_again == 'yes' or choose_again == 'y':
			user_choices = ask_user()

		elif choose_again == 'no' or choose_again == 'n':
			another_choice = False

		else:
			print('Invalid choice, try again.')
		# Allows user to pick another song

	return

def run_programme():
	# Funtion to run the programme

	user_choices = ask_user()
	song_lyrics_generator = lyrics(user_choices['Artist'], user_choices['Song'])
	# Creates instance of song_lyrics_generator

	print(song_lyrics_generator)
	#Lets user know their choice of song

	song_lyrics_generator.fetch_data()
	# Calls method to fetch song data from the web

	song_lyrics_generator.write_to_txt_file()
	# Writes song to text file

	song_lyrics_generator.write_to_mp3_file()
	# Writes song to mp3 file

	ask_user_again()
	# Asks user if they would like to choose another song

run_programme()
