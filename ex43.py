# jumping right into his solution for time management

# Basic imports for game
from logging.config import valid_ident
from sys import exit
from random import randint
from textwrap import dedent # Oooh this is what I needed in Luna's text adventure game 

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1) # why exit(1)? "Exit the interpreter by raising SystemExit(status). If the status is omitted or None, it defaults to zero (i.e., success). If the status is an integer, it will be used as the system exit status. If it is another kind of object, it will be printed and the system exit status will be one (i.e., failure)."


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map # from self, get the scene_map attribute and set it to scene_map

    def play(self):
        # print(">>>> play") # could also print the scene map here
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        # print("^^^^ before while current_scene=", current_scene, "last_scene=", last_scene)
        while current_scene != last_scene:
            # print("^ top of while current_scene=", current_scene, "last_scene=", last_scene)
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            # print("^ end of while current_scene=", current_scene, "last_scene=", last_scene, "next_scene_name=", next_scene_name)

            # print("<<<< end of play: current_scene=", current_scene)
            current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud."
        "Mmkay"
        "I have a small puppy that's better at this."
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative

                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative

                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    The code is 3 digits
                    """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))
            return 'the_bridge'
        else:
            print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))
            return 'death'
            

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))
        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))
            return 'death'
        else:
            print(dedent("""
                    Adventure narrative
                    Adventure narrative
                    Adventure narrative
                    """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won, good job!")
        return Finished

class Map(object):

    # Dictionary map comes after the scenes because the scenes need to exists
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()