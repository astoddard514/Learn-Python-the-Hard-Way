types_of_people = 10 # variable
x = f"There are {types_of_people} types of people." # variable set to f-string

binary = "binary" # variable
do_not = "don't" # variable
y = f"Those who know {binary} and those who {do_not}." # f-string

print(x) # print variable (defined as f-string)
print(y) # print variable (defined as f-string)

print(f"I said: {x}") # print f-string
print(f"I also said: '{y}'") # notice the nested quotes

hilarious = False # variable set to boolean
joke_evaluation = "Isn't that joke so funny?! {}" # variable set to f-string with mysterious empty brakets

print(joke_evaluation.format(hilarious)) # .format syntax

w = "This is the left side of..." # string
e = "a string with a right side." # string

print(w + e) # lining strings up one after the other