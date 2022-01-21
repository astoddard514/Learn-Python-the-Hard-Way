# MODULES (ARE LIKE DICTIONARIES)

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# this goes in mystuff.py (separate file for this to work)
def apple():
    print("I AM APPLES!")

import mystuff
mystuff.apple()

def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of  a dream"

import mystuff

mystuff.apple()
print(mystuff.tangerine)

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable

# CLASSES (ARE LIKE MODULES)
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# OBJECTS (ARE LIKE IMPORT)
thing = MyStuff()
thing.apple()
print(thing.tangerine)

# GETTING THINGS FROM THINGS - 3 ways

# 1 - dict style
mystuff['apples']

# 2 - module style
mystuff.apples()
print(mystuff.tangerine)

# 3 - class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
