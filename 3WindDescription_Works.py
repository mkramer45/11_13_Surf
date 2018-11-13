import requests
from bs4 import BeautifulSoup
import re
import sqlite3

my_url = ['https://magicseaweed.com/Narragansett-Beach-Surf-Report/1103/', 
'https://magicseaweed.com/2nd-Beach-Sachuest-Beach-Surf-Report/846/',
'https://magicseaweed.com/Nahant-Surf-Report/1091/',
'https://magicseaweed.com/Nantasket-Beach-Surf-Report/371/',
'https://magicseaweed.com/Scituate-Surf-Report/372/',
'https://magicseaweed.com/Cape-Cod-Surf-Report/373/',
'https://magicseaweed.com/The-Wall-Surf-Report/369/',
'https://magicseaweed.com/Green-Harbor-Surf-Report/864/',
'https://magicseaweed.com/Cape-Ann-Surf-Report/370/',
'https://magicseaweed.com/27th-Ave-North-Myrtle-Surf-Report/2152/',
'https://magicseaweed.com/Cocoa-Beach-Surf-Report/350/']

for url in my_url:

	r = requests.get(url)

	html = r.text

	soup = BeautifulSoup(html, 'lxml')

	# wind_directions = soup.find_all('td', {"class":"text-center last msw-js-tooltip td-square background-success"})

	wind_dir = soup.find_all(class_=re.compile('^text-center last msw-js-tooltip td-square background-'))  

	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS WindDirection(ID INTEGER PRIMARY KEY, WindDescription TEXT)')

	for w in wind_dir:

		windd = w['title']
		print(w['title'])


		conn = sqlite3.connect('SurfSend.db')
		cursor = conn.cursor()
		# cursor.execute("INSERT INTO WindInfo VALUES (?)", (winb,))
		cursor.execute("INSERT INTO WindDirection (WindDescription) VALUES (?)", (windd,))
		conn.commit()
		cursor.close()
		conn.close()