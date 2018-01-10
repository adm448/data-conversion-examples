#read superheros.json
import json
import csv
from pprint import pprint

with open('superheros.json') as f:
	data = json.load(f)

#select members
members = data['members']

#write headers
with open('flatmembers.csv', 'w') as f:
	writer = csv.writer(f)
	header = [
	'name',
	'age',
	'secretIdentity',
	'powers', 
	'squadName',
	'homeTown',
	'formed',
	'secretBase',
	'active'
	]
	writer.writerow(header)

#write data
#loop over members
	for hero in members:
		row = [
		hero['name'],
		hero['age'],
		hero['secretIdentity'],
		str(hero['powers']),
		data['squadName'],
		data['homeTown'],
		data['formed'],
		data['secretBase'],
		]
		writer.writerow(row)
