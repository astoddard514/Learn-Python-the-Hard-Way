print("I will now count my chickens:")

# math to number with tenths decimal (not integer math)
print("Hens", 25.0 + 30.0 / 6.0)
# modulo and multiplication have same precedence: 100 - ((25 * 3) % 4) = 100 - (75 % 4) . . . 75 % 4 is 3. (75/4 = 18.75, 18 * 4 = 72, 75 - 72 = 3)
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print("Now I will count the eggs:")

# decimal math practicing precedence
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

# understand less than
print("Is it true that 3.0 + 2.0 < 5.0 - 7.0?")

# print boolean answer (False)
print(3.0 + 2.0 < 5.0 - 7.0)

print("What is 3.0 + 2.0?", 3.0 + 2.0) # string, math operation
print("What is 5.0 - 7.0?", 5.0 - 7.0) # string, math operation (negative answer)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5.0 > -2.0) # string, boolean answer
print("Is it greater or equal?", 5.0 >= -2.0) #string, boolean answer
print("Is it less or equal?", 5.0 <= -2.0) #string, boolean answer (negative number)

print("My age in days on my 37th birthday was", 365.0 * 37.0, "days") # Drill #3