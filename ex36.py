from sys import exit

def cave_spooky():
    print("\nLuna and Gus slowly enter Cave Spooky and their eyes adjust to the darkness. At the back of the cave the notice a huge troll sleeping, snoring loudly.\n")
    # choices: sneak by (find wand) or scream (die)

def deep_woods():
    print("Ahead in the trees, Luna sees the eyes of a tiger. She taps Gus to show him. They need to get away!\n\n=============================================\n")
    # choices: climb a tree (escape) or run (die)
    # use while True loop for Tiger leaving

def dinosaur_land():
    print("Suddenly, Gus spots a pterodatyl flying overhead! It's looking for its next meal.\n\n**********************************************\n")
    print("SHOULD LUNA AND GUS 'hide' UNDER A BUSH OR 'throw rocks' AT THE PTERODACTYL?")
    print("TYPE 'hide' OR 'throw rocks'\n")
    
    choice = input("> ")

    if choice == "hide":
        print("\n=============================================\n\nThe pterodactyl doesn't see them, and flies further into the valley. Luna and Gus continue on and arrive at the deep woods.")
        deep_woods()
    elif choice == "throw rocks":
        dead("\n=============================================\n\nThe pterodactyl swoops down and captures you both in its claws. It brings you back to its family for dinner.\n\n=============================================\n")
    else:
        dead("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\nYOU JUST TYPED IN ROBOT LANGUAGE AND THEY FOUND YOU WITH THEIR LASERS.\n")

def dead(why):
    print(why, "AND YOU DIED.\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    print("TRY AGAIN? 'yes' and 'no'")

    choice = input("> ")

    if choice == "yes":
        start()
    elif choice == "no":
        print("BYE!")
    else:
        dead("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\nYou just typed in robot language and the robots found you with their lasers.\n")

def start():
    print("\n=============================================\n\nSTART: \nLuna and Gus have to find the magical wand to save Mom and Dad from EVIL ROBOTS! They will need to pass across dinosaur-land, through the deep woods, and into Cave Spooky to get to the magic wand. It will a be very difficult journey.\n\n=============================================\n")
    print("ARE YOU READY TO HELP MOM AND DAD?")
    print("TYPE 'yes' or 'no'\n")

    choice = input("> ")

    if choice == "yes":
        print("\n**********************************************\n\nBrave Luna and strong Gus leave their neighborhood and start across dinosaur-land.")
        dinosaur_land()
    elif choice == "no":
        dead("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\nTHE ROBOTS HAVE STOLEN YOUR MOM AND DAD FOREVER. SO SAD. YOU STARVE WITH NO FOOD.")
    else:
        dead("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\nYOU JUST TYPED IN ROBOT LANGUAGE AND THEY FOUND YOU WITH THEIR LASERS.\n")

start()
