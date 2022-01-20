ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # split(ten_things)
more_stuff = ["Day", "Night", "Song", "Frisbee", 
                "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # why does he use a while loop here? a for loop would need to use booleans and increment until the boolean changes. Might be more code. 
    next_one = more_stuff.pop() # pop(more_stuff)
    print("Adding: ", next_one)
    stuff.append(next_one) # append<next_one>(stuff)
    print(f"There are {len(stuff)} items now.")



print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) 
print(stuff.pop()) # pop(stuff)
print(' '.join(stuff)) # join<stuff>(' ') # spaces between list items
print('#'.join(stuff[3:5])) # join<stuff3:5>('#') #hashes between list items from index locations




# Wait there are not 10 things in that list. Let's fix that.
# Adding:  Boy
# There are 7 items now.
# Adding:  Girl
# There are 8 items now.
# Adding:  Banana
# There are 9 items now.
# Adding:  Corn
# There are 10 items now.
# There we go:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
# Let's do some things with stuff.
# Oranges
# Corn
# Corn
# Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
# Telephone#Light