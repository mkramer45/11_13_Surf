from lxml import html
import requests
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

	page = requests.get(url)
	tree = html.fromstring(page.content)


	#This will create master list containing SwellSize, SwellInterval, & Airtemp
	intervals = tree.xpath('//*[@class="nomargin font-sans-serif heavy"]/text()')
	#Navigating through master list, breaking down 3 data categories into variables
	swellsizeft = intervals[0::5]
	swellintervalsec = intervals[2::5]
	airtempdegrees = intervals[4::5]

	# Next we will need to iterate through our per category lists, and add to DB!

	# ['A', 'B', 'C', 'D']
	# ['Swell Size', 'Junk', 'SwellInterval', 'Junk', 'Airtemp']
	# ['  2', '  ', '  11', '  ', '38', ]

	conn = sqlite3.connect('SurfSend.db')
	cursor = conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS SurfReport(ID INTEGER PRIMARY KEY, SwellSizeFt TEXT, SwellIntervalSec TEXT, AirTemp TEXT )')

	for x, y, z in zip(swellsizeft, swellintervalsec, airtempdegrees):
			conn = sqlite3.connect('SurfSend.db')
			cursor = conn.cursor()
			# cursor.execute("INSERT INTO SurfReport VALUES (?,?,?)", (x,y,z))
			cursor.execute("INSERT INTO SurfReport (SwellSizeFt, SwellIntervalSec, AirTemp) VALUES (?,?,?)", (x,y,z,))
			conn.commit()
			cursor.close()
			conn.close()

#Executing this script should give us 616 rows