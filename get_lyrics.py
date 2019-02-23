from fetch_data import data
from gtts import gTTS
import os
import re


def normal_lyrics():
	# Function to create file with song lyrics and play them out loud

	song = data()
	# Gets lyrics from genius.com using data function in fetch_data

	txt_file_location = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'songs', 'lyrics.txt')
	# Creates path to save .txt file(c://Ellie/Desktop/songs)

	with open(txt_file_location, 'w', encoding= 'utf-8') as text_file:
		text_file.write(song)
		# Writes lyrics to a text file

	mp3_file_location = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'songs', 'lyrics.mp3')
	# Creates path to save .txt file(c://Ellie/Desktop/songs)

	remove_verse_headings = song
	remove_verse_headings = re.sub("re.sub("[\(\[].*?[\)\]]", "", remove_verse_headings)
	# Uses re to remove words in [] brackets - this removes verse heading so tts doesn't read them

	sing = gTTS(remove_verse_headings)
	sing.save(mp3_file_location)
	# Creates mp3 file of song
