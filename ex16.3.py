from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.") # truncate means empty file
print("If you don't want that, hit CTRL-C (^C).") # not sure that this command works as intended in terminal.
print("If you do want that, hit RETURN.")

input("?") # nonsense input?

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!") # emptying
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ") 
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"""
    {line1}  
    {line2}
    {line3}
""") # escape \n is redundant in this format

print("And finally, we close it.")
target.close()