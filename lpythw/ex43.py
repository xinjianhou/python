from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a user.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit()


class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
			The Gothons of Planet Percal #25 have invaded 
			destroyed your entire crew. You are the last survival
			member and your last mission is to get the neutron
			bomb from the Weapons Armory, put it in the bridge
			blow the ship up after getting into an escape.

			You're running down the central corridor to the 
			Armory when a Gothon jumps out, red scaly skin
			teeth, and evil clown costume flowing around his
			filled body. He's blocking the door to the Armory
			about to pull a weapon to blast you.
			"""))
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
				Quick on the draw you yank out your blaste
				it at the Gothon. His clown costume is flowing
				moving around his body, with throws off you.
				Your laser hits his costume but misses him
				This completely ruins his brand new costume
				bought him, with makes him fly into an invaded
				and blast you repeatedly in the face until 
				dead. Then he eats you.
				"""))
            return 'death'
        elif action == "dodge!":
            print(dedent("""
				Like a world class boxer you dodge, weave,
				slide right as the Gothon's blaster cranks
				past your head. In the middle of your after
				die as the Gothon stomps on your head and body
				"""))
            return 'the_bridge'

        elif action == "tell a joke":
            print(dedent("""
				Lucky for you they made you learn Goth invaded
				the academy. You tell the one Gothon joke
				Lbhe zbgure vf fb sng, jura fur fvgf nebha
				fur fvgf nebhag gur ubhfr. The Gothon stop 
				not to laugh, then busts out laugthing and 
				While he's laughing you run up and shoot his
				the head putting him down, the jump through
				Weapon Armory door.
				"""))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTER!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
			You do a dive roll into the Weapon Armory, cry 
			the room for more Gothons that might be hiding
			quiet, too quiet. You stand up and run to the 
			room and find the neutron bomb in its configured.
			There's a keypad lock on the box and you need 
			get the bomb out. If you get the code wrong 10 times,
			the lock closes forever and you can't get the code is 3 digits.
			"""))
        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZEDDD!")
            guesses += 1
            print(code)
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
				The container clicks open and the seal brand 
				gas out. You grab the neutron bomb and running,
				you can to the bridge where you must place 
				right spot.
				"""))
            return 'the_bridge'
        else:
            print(dedent("""
				The lock buzzes one last time and then you  
				sickening melting sound as the mechanism 
				together. You decide to sit there, and filled 
				Gothons blow up the ship from their ship 
				"""))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
			You burst onto the Bridge with the neutron destroyed
			under your arm and surprise 5 Gothons who are 
			take control of the ship. Each of them has an 
			clown costume than the last. They haven't pull 
			weapons out yet, as they see the active bomb 
			arm and don't want to set it off.
			"""))
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
				In a panic you throw the bomb at the ground 
				and make a leap for the door. Right as your 
				Gothon shoots you right in the back killing
				you die you see another Gothon frantically
				disarm the bomb. You die knowing they will 
				blow up when it goes off.
				"""))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
				You point your blaster at the bomb under 
				the Gothons put their hands up and start.
				You inch backward to the door, open it, and
				carefully place the bomb on the floor, point
				blaster at it. You then jump back through 
				punch the close button and blast the locker.
				Gothons can't get put. Now that the bomb 
				you run to the escape pod to get off this 
				"""))
            return 'escape_pod'
        else:
            print("DOES NOT COPUTER!")
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print(dedent("""
			You rush through the ship desperately trying to 
			the escape pod before the whole ship explodes
			like hardly any Gothons are on the ship, so you 
			clear of interference. You get to the chamber
			escape pods, and now need to pick one to take 
			them could be damaged but you don't have time.
			There's 5 pods, which one do you take?
			"""))
        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
				You jump into pod {guess} and hit the ejection.
				The pod escapes out into the void of spaceship,
				implodes as the hull ruptures, crushing your 
				jam jelly.
				"""))
            return 'death'
        else:
            print(dedent("""
				You jump into pod {guess} and hit the ejection.
				The pod easily slides out into space header
				planet below. As it files to the planet, go
				back and see your ship implodes then explodes
				bright star, taking out the Gothon ship any
				time. You won!
				"""))

            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):
    scene = {
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
        val = Map.scene.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
