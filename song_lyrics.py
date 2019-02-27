import os
import re
import requests
from bs4 import BeautifulSoup
from gtts import gTTS

class lyrics:
# Class to generate song lyrics from user input

    def __init__(self, artist, song, song_lyrics=''):
        # Function initialises lyrics class
        self.artist = artist
        self.song = song
        self.song_lyrics = song_lyrics

    def __repr__(self):
        # Function return song name and artis name when printed
        return 'You chose {song}, by {artist}'.format(song=self.song, artist=self.artist)

    def fetch_data(self):
        #Function fetches lyrics from genius
        artist = self.artist
        artist = artist.lower()
        artist = artist[0].upper() + artist[1:]
        artist = artist.split()
        artist = '-'.join(artist)
        # Takes artist input and formats string as needed in genius url

        song = self.song
        song = song.split()
        song = '-'.join(song)
        # Takes song input and formats as needed in genius url

        title = artist + '-' + song + '-lyrics'
        website = 'http://genius.com/{title}'.format(title = title)
        # Creates full web address using formated user inputs

        source = requests.get(website).text
        soup = BeautifulSoup(source, 'lxml')
        div = soup.find('div', class_ = 'lyrics').text
        # Scraps desired song from genius.com using requests and BeautifulSoup

        self.song_lyrics += div
        return div

    def write_to_txt_file(self):
            # Funtion writes song lyrics to txt file and saves on PC
            txt_file_location = os.path.join(os.environ['USERPROFILE'], 'Python', 'Song Lyrics', 'lyrics.txt')
            # Creates path to save .txt file(c://Ellie/Desktop/songs)

            with open(txt_file_location, 'w', encoding= 'utf-8') as text_file:
                text_file.write(self.song_lyrics)
                # Writes lyrics to a text file

            return

    def write_to_mp3_file(self):
            # Function writes song lyrics to mp3 file and saves on PC
            mp3_file_location = os.path.join(os.environ['USERPROFILE'], 'Python', 'Song Lyrics', 'lyrics.mp3')
        	# Creates path to save .txt file(c://Ellie/Desktop/songs)

            remove_verse_headings = self.song_lyrics
            remove_verse_headings = re.sub("\[[^]]+\]", "", remove_verse_headings)
        	# Uses re to remove words in [] brackets - this removes verse heading so tts doesn't read them

            sing = gTTS(remove_verse_headings)
            sing.save(mp3_file_location)
        	# Creates mp3 file of song

            return
