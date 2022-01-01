name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # inches * centimeters
weight = 180 / 2.205  # lbs => kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {round(height)} centimeters tall.")
print(f"He's {round(weight)} kilograms heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {round(weight)} I get {round(total)}.")