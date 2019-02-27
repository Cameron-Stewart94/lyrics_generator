from ask_user_input import *
from song_lyrics import *

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

	another_song = ask_user_again()
	# Asks user if they would like to choose another song

	if another_song == True:
		run_programme()


run_programme()
