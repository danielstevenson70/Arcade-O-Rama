#The_Thing_RPG
class Character:
    def __init__(self, name, health=100, stamina=50):
        self.name = name
        self.health = health
        self.stamina = stamina 
        self.weapons = []

    def stamina(self):
        print(f"{self.name} is freaking out")
        self.health -= self.stamina
         
    def attack(self, enemy):
         print(f"{theThing.name} attacks")
         
    def is_alive(self):
        return self.health > 0

class Main(Character):
        def __init__(self, name, health, stamina):
            super().__init__(name, health=health, stamina=stamina)

class Friend(Character):
        def __init__(self, name, health, stamina):
            super().__init__(name, health=health, stamina=stamina)

class Doctor(Character):
     def __init__(self, name, health, stamina):
            super().__init__(name, health=health, stamina=stamina)

class Coworker(Character):
     def __init__(self, name, health, stamina):
            super().__init__(name, health=health, stamina=stamina)

class Assitant(Character):
     def __init__(self, name, health, stamina):
            super().__init__(name, health=health, stamina=stamina)

class TheThing(Character):
     def __init__(self, name, health, stamina):
            super().__init__(name, health=health, stamina=stamina)

theThing = TheThing("The Thing", 100, 100)
main = Main("MacReady", 100, 70)
friend = Friend("Childs", 100, 75)
doctor = Doctor("Dr. Copper", 80, 30)
coworker = Coworker("Palmer", 75, 45)
assitant = Assitant("Blair", 60, 45)

def main():
    while theThing.is_alive() and friend.is_alive() and doctor.is_alive() and coworker.is_alive():
        print("")
        print("")
        print("Welcome to Outpost 31. There is a scientific research team that's in Anartica")
        print("  ")
        print("  ")
        print("There has been an alien life form imitating humans to live and inhabit their bodies")
        print("  ")
        print("")
        print("Man is the warmest place to hide")
        print("")
        print("   ")
        print("              ========   ==   ==   ===== ")
        print("                ===      ==   ==   == ")
        print("                ===      =======   ===== ")
        print("                ===      ==   ==   == ")
        print("                ===      ==   ==   ===== ")
        print("                                             ")
        print("     =========   ==   ==    ==    ==     ==  =======    ")
        print("        ==       ==   ==    ==    ===    ==  ==   ==    ")
        print("        ==       ==   ==    ==    ===    ==  ==         ")
        print("        ==       =======    ==    ==  =  ==  ==         ")
        print("        ==       ==   ==    ==    ==    ===  ==   ==    ")
        print("        ==       ==   ==    ==    ==     ==   ==   ==    ")
        print("        ==       ==   ==    ==    ==     ==  =======     ")
        print("")
        print("")
        print("")
        print("There's a dog running from a helicopter with people shooting at it")
        print("")
        print("")
        print("The helicopter has been shot down by MacReady")
        print("")
        print("")
        print("They go to inspect the helicopter, no one is alive and found the base they were at")
        print("")
        print("")
        print("Now to go insepct the other base where the helicopter came from")
        print(""" 
            %s's stats:
            Health: %d
            Stamina: %d
            """ % (theThing.name, theThing.health, theThing.stamina))
        
        choice = input("""
            1. Find the massive ice block that has been uncovered
            2. Do Nothing and return back to camp
            3. Just stay at the base and do nothing
            """)
        if choice == "1":
            print("Bring it back to camp to inspect")
            pass
        elif choice == "2":
            print("That was useless!")
            pass
        elif choice == "3":
            print("Let's retry that")
            continue
        else:
            print("Click the right button, please")
            pass

        choice = input("""
            1. Stay in the corner while the others check it out
            2. Inspect the massive ice boulder
            3. Do nothing
            """)
        if choice == "1":
            print("Just take some peaks at whats going on")
            pass
        elif choice == "2":
            print("The ice has some alien creature in it, what the hell is it?!")
            pass
        elif choice == "3":
            print("Come on now, do better!")
            pass
        else:
            print("Click the right button, please")
            pass

        print("There's been an ungodly noise in the kennel where the other dogs are in")

        choice = (input("""
            1. Ignore it
            2. Go outside
            3. Inspect the kennel
            """))
        if choice == "1":
            print("That's not going to help but now you hear screaming and all the noise")
            pass
        elif choice == "2":
            print("Go oustide and freeze but now you hear screaming inside")
            pass
        elif choice == "3":
            print("The dog has turned into the creature and is killing the other dogs!!")
            pass
        else:
            print("You don't care to find out what that noise was?!")
            continue

        choice = input("""
            1. Get inside the kennel to seperate the dogs
            2. Set fire to the creature
            3. Ignore it
            """)
        if choice == "1":
            print("Well that was dumb, no weapons?!")
            break
        elif choice == "2":
            print("Burning the creature clearly worked!")
            pass
        elif choice == "3":
            ("This can't be ignored for forever")
            pass
        else:
            print("Click the right button, please")
            pass

        choice = input("""
            1. Stand in the corner in drink
            2. Call someone on the radio
            3. Do some research on what this thing is
            """)
        if choice == "1":
            print("Getting drunk won't solve this")
            continue
        elif choice == "2":
            print("There's no response")
            pass
        elif choice == "3":
            print("This thing has imitated life and blood cells to get into someones body")
            pass
        else:
            print("Are you not wanting to help?!")
            pass
        
        print("")
        print("Perry is now dead, this thing has free roam around the entire base")
        print("")
        print("Anyone can be imitated at this point, will YOU make the right choice?")
        print("")
        print("Now we hear shooting in the base and the doctor is losing his mind!")

        choice = input("""
            1. Check on the doctor
            2. Do nothing
            3. Talk him down
            """)
        if choice == "1":
            print("Calm him down so he doesn't kill anyone")
            pass
        elif choice == "2":
            print("Doing nothing solves nothing")
            pass
        elif choice == "3":
            print("Distract him, knock him out and put him in the shed")
            pass
        else:
            print("Click the right button, please")
            pass

        choice = (input("""
            1. Call the radio again
            2. Escape on the helicopter
            3. Check on the doctor out in the shed
            """))
        if choice == "1":
            print("No response again")
            pass
        elif choice == "2":
            print("It's out of gas, you're stuck")
            pass
        elif choice == "3":
            print("He's still out there, seeming normal...so far")
            pass
        else:
            print("YOU ARE THE THING, I KNOW IT!!")
            pass
        
        print("")
        print("MacReady has locked himself in a room with C4")
        print("")
        print("The stress has gotten to Norris and now he's fallen over and needs CPR")

        choice = (input("""
            1. Give Norris CPR
            2. Help MacReady blow the place up
            3. Start shooting
            """))
        if choice == "1":
            print("Norris chest has opened and he's been imitated into an alien creature")
            pass
        elif choice == "2":
            print("Now you're all dead")
            break
        elif choice == "3":
            print("Everyone's dead but you, so you must be The Thing?")
            break
        else:
            print("YOU ARE THE THING, I KNOW IT!!")
            pass
        
        print("")
        print("Norris' head has stretched completely off and has grown legs, like a spider")
        print("")
        print("")
        print("Now this alien is crawling around nowhere to be found")
        print("")
        print("")
        print("With Norris dead, the head has been burned to a crisp, it' time to see who is being imitated")
        print("")
        print("")
        print("Now let's check the blood")


        choice = (input("""
            1. Check MacReady
            2. Check Childs
            3. Check Windows 
            """))
        if choice == "1":
             print("He's clear")
             pass
        elif choice == "2":
            print("He's clear")
            pass
        elif choice == "3":
            print("He's clear")
            pass
        else:
            print("Three down, Three to go")
            pass

        print("Three down, Three to go")

        choice = (input("""
            1. Check Nauls
            2. Check Palmer
            3. Check Garry
            """))
        if choice == "1":
            print("He's clear")
            pass
        elif choice == "2":
            print("HE HAS IT!! HE'S BEEN IMITATED")
            pass
        elif choice == "3":
            print("He's clear")
            pass
        else:
            print("It's Palmer since you didn't want to answer it correctly!")
            pass
        
        print("")
        print("")
        print("IT'S PALMER!! YOU HAVE TO BURN HIM!!")
        print("")
        print("")
        print("Now we need to check on Blair and have to watch Perry since Palmer had been imitated")
        
        choice = (input("""
            1. Insepct outside
            2. Watch Perry
            3. Go drink and pretend nothing's happening
            """))
        if choice == "1":
            print("Watch for Blair")
            pass
        elif choice == "2":
            print("Just stand there and watch him, he moves, burn him")
            pass
        elif choice == "3":
            print("Drinking the sorrows doesn't stop imitation!")
            pass
        else:
            print("please for the love of god click the right buttons!")
            pass

        choice = input("""
            1. Check the outdoor shed where Blair is
            2. Stay inside
            """)
        if choice == "1":
            print("Where did he go?! He has to be imitated!!")
            pass
        elif choice == "2":
            print("Just keep a watch out, at least")
            pass
        else:
            print("You gotta make the right decision here, it's life or death!!")
            pass
        
        choice = (input("""
            1. Blow the place up
            2. Sacrifice yourself
            """))
        if choice == "1":
            print("It's the only way to survive")
            pass
        elif choice == "2":
            print("Die without knowing the truth")
            break
        else:
            print("Either die or just blow it up")
            continue

        choice = (input("""
            1. Run with MacReady and Childs to find the spaceship
            2. Die in the fire
            """))
        if choice == "1":
            print("Go and search where this alien came from")
            pass
        elif choice == "2":
            print("Die without knowing the truth")
            break
        else:
            print("Will you just do the right thing?")
            pass

        choice = (input("""
            1. Face the Final Form of the Thing by burning it
            2. Try shooting the Thing 
            """))
        if choice == "1":
            print("Burn it and watch it set ablaze")
            pass
        elif choice == "2":
            print("You should've know that was not going to work")
            break
        else:
            print("You're dead. Retry")
            continue
            
        choice = (input("""
            1. Think MacReady is The Thing
            2. Think Childs is The Thing
            """))
        if choice == "1":
            print("You are correct but you're still dead and to be imitated by The Thing")
            break
        elif choice == "2":
            print("Wrong choice but either way you're going to die and will be imitated by The Thing")
            break
        else:
            print("Why can't you just cilck 1 or 2?!")
            continue

main()