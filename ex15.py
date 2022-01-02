from sys import argv

script, filename = argv # Lines 1 & 3 use argv to get a filename

txt = open(filename) # new command to open file 

print(f"Here's your file {filename}:")
print(txt.read()) # read command will act on txt

print("Type the filename again:")
file_again = input("> ") # input prompt to rename txt file

txt_again = open(file_again) #open

print(txt_again.read()) #read & print