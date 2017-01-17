states = {
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-'*10)
print("NY state: ", cities['NY'])
print("OR state: ", cities['OR'])

print('-'*10)
print('Michigan abbrev', states['Michigan'])
print('Florida abbrev', states['Florida'])

print("-"*10)
	
state = states.get('Texas', None)
if not state:
	

print('-'*10)
for state, abbrev in states.items():
	print("%s %s" % (state, abbrev))

print('-'*10)
for abbrev, city in cities.items():
	print("%s has city %s" % (abbrev, city))