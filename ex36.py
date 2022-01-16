from sys import exit

def cave_spooky():
    print("""
    Luna and Gus slowly enter Cave Spooky and their eyes adjust to the darkness. At the back of the cave the notice a huge troll sleeping, snoring loudly.\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n""")
    # choices: sneak by (find wand) or scream (die)

def deep_woods():
    print("""    Ahead in the trees, Luna sees the glimmering eyes 
    of a wild boar. She taps Gus to show him. They need to get away!
    \n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n
    """)
    print("SHOULD LUNA AND GUS climb a tree or run away?")
    print("TYPE 'climb' or 'run'")
    boar_left = False

    while True:
        choice = input("> ")

        # kids have to throw snack, THEN try to run. Want to use a while loop like in the execise, using a boolean
        if choice == "run":
            fail("The boar chases you out of the deep woods, away from Cave Spooky.")
        elif choice == "climb": 
            print()

            cave_spooky()
        else:
            fail("\n*************************************************************\n\n    You just typed in robot language and they found you with their lasers.")
    

def dinosaur_land():
    print("""
    Suddenly, Gus spots a pterodactyl flying overhead! 
    It's looking for its next meal.  
        \n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n
        """)
    print("SHOULD LUNA AND GUS 'hide' UNDER A BUSH OR 'throw rocks' AT THE PTERODACTYL?")
    print("TYPE 'hide' OR 'throw rocks'\n")
    
    choice = input("> ")

    if choice == "hide":
        print("""
    \n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n
    The pterodactyl doesn't see them, and flies 
    further into the valley. Luna and Gus continue 
    on and arrive at the deep woods.
        """)
        deep_woods()
    elif choice == "throw rocks":
        fail("""
    \n*************************************************************\n
    The pterodactyl swoops down and captures you 
    both in its claws. It brings you back to its family for dinner.""")
    else:
        fail("\n*************************************************************\n\n    You just typed in robot language and they found you with their lasers.")

def fail(why):
    print(why, "\n    YOU FAIL TO RETRIEVE THE WAND.\n\n*************************************************************\n")
    print("TRY AGAIN? 'yes' and 'no'")

    choice = input("> ")

    if choice == "yes":
        start()
    elif choice == "no":
        print("BYE!")
    else:
        fail("\n*************************************************************\n\n    You just typed in robot language and they found you with their lasers.")

def start():
    print(
        """
        \n==============================================================\n
    START:
    Luna and Gus have to find the magical 
    wand to save Mom and Dad from EVIL ROBOTS! 
    They will need to pass across dinosaur-land, 
    through the deep woods, and into Cave Spooky 
    to get to the magic wand. It will a be very 
    difficult journey.
        \n==============================================================\n
        """)
    print("ARE YOU READY TO HELP MOM AND DAD?")
    print("TYPE 'yes' or 'no'\n")

    choice = input("> ")

    if choice == "yes":
        print(
        """
    \n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n
    Brave Luna and strong Gus leave their neighborhood 
    and start across dinosaur-land.""")
        dinosaur_land()
    elif choice == "no":
        fail(
        """
        \n*************************************************************\n
    The robots have stolen your mom and dad forever. 
    So sad. You give up on finding the wand and 
    survive like wildlings on berries and seeds.""")
    else:
        fail("\n*************************************************************\n\n    You just typed in robot language and they found you with their lasers.")

start()
