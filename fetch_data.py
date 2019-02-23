import requests
from bs4 import BeautifulSoup
import re


def data():
	#Function to fetch lyrcis from genius.com
	artist = input('Enter an Artist: ')
	artist = artist.lower()
	artist = artist[0].upper() + artist[1:]
	artist = artist.split()
	artist = '-'.join(artist)
	# Takes artist input and formats string as needed in genius url

	song = input('Enter a song: ' )
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

	return(div)
