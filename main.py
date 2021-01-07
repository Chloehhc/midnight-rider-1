# main.py
# Midnight Rider
# Text-based adventure game.
# Gamespot gives it 9 out of 10.

import random
import sys
import textwrap
import time

# it's in capitals b/c it's a constant (INTRODUCTION)
INTRODUCTION = """
WELCOME TO MIDNIGHT RIDER

WE'VE STOLEN A CAR, WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.

THAT'S WHY THE GOVERNMENT WANTS IT.

WE CAN"T LET THEM HAVE IT.

ONE GOAL: SURVIVAL... and THE CAR
REACH THE END BEFORE THE MAN GON GETCHU.

----------
"""

WIN = """ 
YOU PRESS THE BUTTON TO OPEN THE GATE.
THIS ISN'T THE FIRST TIME YOU'VE DONE THIS.
YOU CAN TIME IT PERFECTLY SO THAT YOU SLIDE THE CAR IN AS THE GATES CLOSE.

YOU KNOW YOU DID THE RIGHT THING.
THE GOVERNMENT WOULD HAVE TORN THE CAR APART, ANALYSING IT, TESTING IT, THEN DESTROYING IT.

THEY DON'T KNOW ITS SECRETS...
THAT IT HOLDS THE KEY TO DIFFERENT WORLDS.

AS YOU STEP OUT OF THE VEHICLE, FIDO RUNS UP TO YOU.
"THANK YOU FOR SAVING ME," HE SAYS.

AS YOU TAKE A COUPLE OF STEPS AWAY FROM THE CAR, IT MAKES A STRANGE NOISE.

BEFORE YOUR EYES, T SHIFTS ITS SHAPE.
YOU'VE SEEN IT BEFORE, BUT ONLY ON TV.

"BUBLEBEE...?"

----GAME OVER----
"""

CHOICES = """
    ----
    A. Eat a piece of tofu.
    B. Drive at moderate speed.
    C. Speed ahead at full throttle.
    D. Stop to refuel (NO FOOD AVAILABLE)
    E. Status Check
    Q. QUIT
    ____
"""

def type_text_output(string):
    for char in textwrap.dedent(string):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(1)

def main():
    #type_text_output(INTRODUCTION)

    # CONSTANTS (use caps for constants)
    MAX_FUEL_LEVEL = 50
    MAX_DISTANCE_TRAVELLED = 100
    MAX_TOFU = 3

    # Variables
    done = False

    kms_travelled = 0      # 100 km is the end
    agents_distance = -20  # 0 is the end (agents have caught up)
    turns = 0
    tofu = MAX_TOFU        # 3 is max
    fuel = MAX_FUEL_LEVEL  # max is 50 L
    hunger = 0

    # MAIN LOOP
    while not done:
        # Random events
        # FIDO - refills your food (5% chance)
        if tofu < 3 and random.random() < 0.05:
            # refill tofu
            tofu = MAX_TOFU
            # player feedback
            print("******** You look at your tofu container.")
            print("******** It is filled magically.")
            print("******** \"You're welcome!\", sats a small voice.")
            print("******** THe dog used its magic tofu cooking skills.")

        # Check if reached END GAME
        # WIN -- Travelled the Distance Required
        if kms_travelled > MAX_DISTANCE_TRAVELLED:
            # Print win scenario - STYLISTIC TYPING
            time.sleep(2)
            type_text_output(WIN)
            break

        # Present the user their choices
        print(CHOICES)

        user_choice = input("What do you want to do? ").lower().strip("!,.?")

        if user_choice == "a":
            # EAT/HUNGER
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("-------- Mmmmmm. Soybean goodness.")
                print("-------- Your hunger is sated.")
                print()
            else:
                print()
                print("-------- You have none left.")
                print()

        elif user_choice == "b":
            # MODERATE SPEED
            players_distance_now = random.randrange(6, 14)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel (anywhere from 2 - 7 L)
            fuel -= random.randrange(2, 7)

            # Player distance travelled
            kms_travelled += players_distance_now

            # Agents distance traveled
            agents_distance -= players_distance_now - agents_distance_now

            # Feedback to Player
            print()
            print("--------Vroooooom.")
            print(f"-------- You traveled {players_distance_now} km.")
            print()

        elif user_choice == "c":
            # FAST SPEED
            players_distance_now = random.randrange(10,16)
            agents_distance_now = random.randrange(7,15)

            # Burn fuel (anywhere from 5 - 10 L)
            fuel -= random.randrange(5, 11)

            # Player distance travelled
            kms_travelled += players_distance_now

            # Agents distance traveled
            # ex.               20                      -4
            #      = 16
            agents_distance -= players_distance_now - agents_distance_now

            # Feedback to Player
            print()
            print("--------ZOOOOOOOOOM.")
            print(f"-------- You traveled {players_distance_now} km.")
            print()

        elif user_choice == "d":
            #  Refueling
            # Fill up the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer (anywhere from 7 - 14 km)
            agents_distance += random.randrange(7,15)

            # Give player feedback
            print()
            print("-------- You filled the fuel tank.")
            print("-------- The agents got closer...")
            print()

        elif user_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkm travelled: {kms_travelled}")
            print(f"\tFuel remaining: {fuel} L")
            print(f"\tAgents are {abs(agents_distance)} kms behind.")
            print(f"\tYou have {tofu} tofu left.")
            print(f"\t------------\n")
        elif user_choice == "q":
            done = True

        # HUNGER
        if user_choice is not ["a","e"]:
            hunger += random.randrange(5, 13)

        time.sleep(1.5)

    # Outro
    print("Thanks for playing the game! See you next time!")

if __name__ == "__main__":
    main()