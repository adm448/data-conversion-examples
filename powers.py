#read superheros.json
import json
from pprint import pprint

with open('superheros.json') as f:
	data = json.load(f)

#create a list of powers (loop over members)
powers = []

#for each member, loop over powers, add that to our list of powers.
members = data['members']
for member in members:
	member_powers = member['powers']
	for power in member_powers:
		powers.append(power)

#get only unique elements
unique_powers = list(set(powers))
#print unique elements
pprint(unique_powers)