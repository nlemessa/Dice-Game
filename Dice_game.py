# Tuple out Dice Game

import random

print("Welcome to tuple out dice game!")

# User enters their name
def player_name():
    name = input("Enter your name please.")
    print(f"Let the games begin {name}!")

# User rolls dice 
def dice_rolls():
    roll1, roll2, rolls3 = dice_rolls
    print(f"The first die shows {roll1}")
    print(f"The first die shows {roll2}")
    print(f"The first die shows {rolls3}")

# Counting how many times a number appears 
def count_howmanytimes(dice):
    counts = list(range(7))
    return [dice.count(value) for value in range(1,7)]

# Get the final sum of the dices rolled 
def score_calculation(dice):
    counts = count_howmanytimes(dice)
    if 3 in counts:
        return 0, True
    return sum(dice), False 

def play_turn(player_name):
    curren_dice = dice_rolls()
    print(f"\n {player_name}'s initial roll: {curren_dice}")

    while True:
        turn_score, tupled_out = score_calculation(curren_dice)
        if tupled_out:
            print(f"{player_name} tupled out with {curren_dice}! Scored 0 points.")
            return 0
        
        print(f"{player_name}'s current score: {turn_score}")

        if player_name == "Player":
            prefrence = input("Do you want to continue rolling dice? (yes/no):").lower()
            if prefrence is not 'yes':
                print(f"Computer stops with {turn_score} points.")
                return turn_score
        current_dice = dice_rolls()
        print (f"New roll: {current_dice}")
            


