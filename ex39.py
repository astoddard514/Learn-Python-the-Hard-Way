"""Note when we put things in a dict, get them from a hash. Watch how we are mapping states to their abbreviations and then the abbreviations to cities in the states. Remember, mapping (or associating is the key concept in a dictionary.)"""

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
} 

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"and has city {cities[abbrev]}")

# now do both at the same time
print('-' * 10)
for state, avvrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

# ----------
# NY State has:  New York
# OR State has:  Portland
# ----------
# Michigan's abbreviation is:  MI
# Florida's abbreviation is:  FL
# ----------
# Michigan has:  Detroit
# Florida has:  Jacksonville
# ----------
# Oregon is abbreviated OR
# Florida is abbreviated FL
# California is abbreviated CA
# New York is abbreviated NY
# Michigan is abbreviated MI
# ----------
# and has city San Francisco
# and has city Detroit
# and has city Jacksonville
# and has city New York
# and has city Portland
# ----------
# Oregon state is abbreviated OR
# and has city Portland
# Florida state is abbreviated OR
# and has city Portland
# California state is abbreviated OR
# and has city Portland
# New York state is abbreviated OR
# and has city Portland
# Michigan state is abbreviated OR
# and has city Portland
# ----------
# Sorry, no Texas.
# The city for the state 'TX' is: Does Not Exist