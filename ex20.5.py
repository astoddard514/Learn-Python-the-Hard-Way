#this variation uses += in manual iteration section

# import module
from sys import argv 

# unpack arguments
script, input_file = argv 

#function for printing file
def print_all(f): 
    print(f.read())

#function to start at begining of file
def rewind(f): 
    f.seek(0)

# function for labeling each line with a number
def print_a_line(line_count, f): 
    print(line_count, f.readline())

# use second argv file
current_file = open(input_file) 

print("First let's print the whole file:\n")

# print_all function using current_file variable
print_all(current_file) 

print("Now let's rewind, kind of like a tape.")

# rewind function using current_file variable
rewind(current_file) 

print("Let's print three lines:")

# manual iteration section
# current_line provides the line_count argument each iteration, current_file provides f argument
current_line = 1 # line_count = 1
print_a_line(current_line, current_file)

current_line += 1 # line_count = 2
print_a_line(current_line, current_file)

current_line += 1 # line_count = 3
print_a_line(current_line, current_file)

# PS C:\Users\angel\temp\python> python ex20.py test.txt
# First let's print the whole file:

# ÿþT h i s   i s   a   t e s t   f i l e .(ÿþ is some weird UTF-8 versus UTF-16 thing.)


# Now let's rewind, kind of like a tape.
# Let's print three lines:
# 1 ÿþT h i s   i s   a   t e s t   f i l e .

# 2

# 3

# Use more suitable file:
# PS C:\Users\angel\temp\python> python ex20.py test4.txt
# First let's print the whole file:

  #  here we go
  #  test it out
  #  3 lines please

# Now let's rewind, kind of like a tape.
# Let's print three lines:
# 1     here we go

# 2     test it out

# 3     3 lines please