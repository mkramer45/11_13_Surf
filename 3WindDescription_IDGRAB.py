import requests
from bs4 import BeautifulSoup
import re
import sqlite3

url = 'https://magicseaweed.com/Narragansett-Beach-Surf-Report/1103/'

conn = sqlite3.connect('SurfSend.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS IDGrab(ID INTEGER PRIMARY KEY, WindDescription TEXT)')

r = requests.get(url)

html = r.text

soup = BeautifulSoup(html, 'lxml')

# wind_directions = soup.find_all('td', {"class":"text-center last msw-js-tooltip td-square background-success"})

wind_dir = soup.find_all(class_=re.compile('^text-center last msw-js-tooltip td-square background-'))  

for w in wind_dir:

	windd = w['title']
	print(w['title'])


	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	# cursor.execute("INSERT INTO WindInfo VALUES (?)", (winb,))
	cursor.execute("INSERT INTO IDGrab (WindDescription) VALUES (?)", (windd,))
	conn.commit()
	cursor.close()
	conn.close()