import os
import re
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from titlecase import titlecase

class lyrics:
# Class to generate song lyrics from user input

    def __init__(self, artist_name, song_name, song_lyrics='', song_description =''):
        # Function initialises lyrics class
        self.artist_name = artist_name
        self.song_name = song_name
        self.song_lyrics = song_lyrics
        self.song_description = song_description

    def __repr__(self):
        # Function return song name and artis name when printed
        return 'You chose {song}, by {artist}...'.format(song=self.song_name, artist=self.artist_name)

    def fetch_data(self):
        #Function fetches lyrics from genius

        def format_song_to_url(artist_name, song_name):
            # Function takes user song choice and formats string to git genius url
            artist_name = artist_name.lower()
            artist_name = artist_name[0].upper() + artist_name[1:]
            artist_name = artist_name.split()
            artist_name = '-'.join(artist_name)
            # Takes artist input and formats string as needed in genius url

            song_name = song_name.split()
            song_name = '-'.join(song_name)
            # Takes song input and formats as needed in genius url

            title = artist_name + '-' + song_name + '-lyrics'
            website = 'http://genius.com/{title}'.format(title = title)
            # Creates full web address using formated user inputs
            return website

        def fetch_web(website):
            source = requests.get(website).text
            soup = BeautifulSoup(source, 'lxml')
            html_lyrics = soup.find('div', class_ = 'lyrics').text
            song_info = soup.find('div', class_ = 'header_with_cover_art-primary_info').text
            return {'Lyrics' : html_lyrics, 'Song Information' : song_info}
            # Scraps desired song from genius.com using requests and BeautifulSoup

        def remove_whitespace(string):
            #Funtion removes blank lines from song_info string
            song_info_lst = string.split('\n')
            song_info_lst = [i for i in song_info_lst if len(i) > 0]
            return song_info_lst


        song_url = format_song_to_url(self.artist_name, self.song_name)
        web_scrape = fetch_web(song_url)
        song_info = remove_whitespace(web_scrape['Song Information'])

        self.song_lyrics += web_scrape['Lyrics']
        self.song_name = song_info[0]
        self.artist_name = song_info[1]
        self.song_description += '\n'.join(song_info[2 : ])
        return {'song' : song_info[0], 'artist' : song_info[1], 'description' : '\n'.join(song_info[2 : ]) }

    def write_to_txt_file(self):
        # Funtion writes song lyrics to txt file and saves on PC

        txt_file_location = os.path.join(os.environ['USERPROFILE'], 'Python', 'Song Lyrics', 'song_lyrics.txt')
        # Creates path to save .txt file(c://Ellie/Desktop/songs)

        with open(txt_file_location, 'w', encoding= 'utf-8') as text_file:
            text_file.write(self.song_lyrics)
            # Writes lyrics to a text file

        return

    def write_to_mp3_file(self):
        # Function writes song lyrics to mp3 file and saves on PC
        mp3_file_location = os.path.join(os.environ['USERPROFILE'], 'Python', 'Song Lyrics', 'song_lyrics.mp3')
        # Creates path to save .txt file(c://Ellie/Desktop/songs)

        remove_verse_headings = self.song_lyrics
        remove_verse_headings = re.sub("\[[^]]+\]", "", remove_verse_headings)
        # Uses re to remove words in [] brackets - this removes verse heading so tts doesn't read them

        tts = gTTS(remove_verse_headings)
        tts.save(mp3_file_location)
        # Creates mp3 file of song

        return
