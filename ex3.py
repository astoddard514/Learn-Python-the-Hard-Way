print("I will now count my chickens:")

# math to number with tenths decimal (not integer math)
print("Hens", 25 + 30 / 6)
# modulo and multiplication have same precedence: 100 - ((25 * 3) % 4) = 100 - (75 % 4) . . . 75 % 4 is 3. (75/4 = 18.75, 18 * 4 = 72, 75 - 72 = 3)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

# decimal math practicing precedence
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# understand less than
print("Is it true that 3 + 2 < 5 - 7?")

# print boolean answer (False)
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2) # string, math operation
print("What is 5 - 7?", 5 - 7) # string, math operation (negative answer)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2) # string, boolean answer
print("Is it greater or equal?", 5 >= -2) #string, boolean answer
print("Is it less or equal?", 5 <= -2) #string, boolean answer (negative number)