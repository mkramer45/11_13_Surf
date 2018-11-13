import bs4
import requests
from bs4 import BeautifulSoup as soup
import sqlite3
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#list of URLs to scrape from
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
# opening up connecting, grabbing the page

conn = sqlite3.connect('SurfSend.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS WindInfo(ID INTEGER PRIMARY KEY, WindMPH TEXT)')

#iterate over list of URLS
for url in my_url:
	#initiating python's ability to parse URL
	uClient = uReq(url)
# this will offload our content in'to a variable
	page_html = uClient.read()
# closes our client
	uClient.close()

# html parsing
	#beautifulsoup magic
	page_soup = soup(page_html, "html.parser")
	#variable for soon to be parsed page
	wind = page_soup.findAll('td', class_=re.compile("text-center table-forecast-wind td-nowrap"))
	#prints the list of URLs we scraped from

# iterates over parsed HTML
	for w in wind:
		#wavesize
		wi = w.find('span', class_='stacked-text text-right')
		winb = wi.text.strip()

		conn = sqlite3.connect('SurfSend.db')
		cursor = conn.cursor()
		# cursor.execute("INSERT INTO WindInfo VALUES (?)", (winb,))
		cursor.execute("INSERT INTO WindInfo (WindMPH) VALUES (?)", (winb,))
		conn.commit()
		cursor.close()
		conn.close()
