from fetch_data import data
from gtts import gTTS
import os

def normal_lyrics():
	# Function to create file with song lyrics and play them out loud

	song = data()
	# Gets lyrics from genius.com using data function in fetch_data

	file_location = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'songs', 'lyrics.txt')

	with open(file_location, 'w', encoding= 'utf-8') as text_file:
		text_file.write(song)
		# Writes lyrics to a text file

	sing = gTTS(song)
	sing.save('song_lyrics.mp3')
	# Creates mp3 file of song
