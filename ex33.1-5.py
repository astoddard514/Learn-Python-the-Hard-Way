i = 0 
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)



# Video follow-along - for loop would be guaranteed to stop after 5
for i in range(0,6):
    numbers.append(i)

# Study drills - convert while loop to a function and replace 6 with a variable
numbers = []

def show_list_build(i, range_high, increment):
    for i in range(0, range_high, increment): # range can take the increment in the arguments
        print(f"Start i: {i}")
        numbers.append(i)

        # i = i + increment # don't need this in a for loop
        print("List: ", numbers)
        print(f"End i: {i}")

show_list_build(6, 15, 3) # remember number in range_high needs to be one above the desired final value