from sys import argv 
# import - how you add features (modules, libraries) to your script from the Python feature set
# argv is the argument variable - holds the arguments you pass to your Python script
# read the WYSS section for how to run this
script, first, second, third = argv
# unpacks argv "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order."

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)