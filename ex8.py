formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4)) # these numbers insert into those sets of curly brackets
print(formatter.format("one", "two", "three", "four")) # these strings insert into the curly brackets
print(formatter.format(True, False, False, True)) # these boolean values fill into those curly brackets
print(formatter.format(formatter, formatter, formatter, formatter)) # the formatter variable inserts its own set of 4curly brackets into each curly bracket

# this is another way to list arguments for the formatter curly brackets
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))    
