from fetch_data import data
from gtts import gTTS

def normal_lyrics():
	# Function to create file with song lyrics and play them out loud

	song = data()
	# Gets lyrics from genius.com using data function in fetch_data

	with open('song.lyrics.txt', 'w', encoding= 'utf-8') as text_file:
		text_file.write(song)
		# Writes lyrics to a text file

	sing = gTTS(song)
	sing.save('lyrics.mp3')
	# Creates mp3 file of song
