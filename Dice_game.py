# Tuple out Dice Game

import random

print("Welcome to tuple out dice game!")

# User enters their name
"""
Asks the player to enter their name 
Then returns the name that was entered 
"""
name = input("Enter your name please.")
print(f"Let the games begin {name}!")

Target_Score = 50
scores = {"Player": 0, "Computer": 0}

print(f"First to {Target_Score} points wins!\n")

while scores["Player"] < Target_Score and scores["Computer"] < Target_Score:
    print("\nPlayer's Turn!")
    dice = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    print(f"\n{name}'s initial roll: {dice}")
    break   
turn_score = 0
#Check if there is a "Tuple Out" 
active_turn = True 
while active_turn:
    if dice [0] == dice[1] == dice [2]:
        print("You tupled out! 0 points scored.")
        turn_score = 0
        active_turn = False
    else:
        turn_score = sum(dice)
        print(f"Current dice score: {turn_score}")
        break   
# Check which dice can be rerolled
    """
    Finds which dice from the three can be rerolled.
    """
    if dice [0] == dice[1]:
        rerollable = [2]
    elif dice [0] == dice[2]:
        rerollable = [1]
    elif dice [1] == dice [2]:
        rerollable = [0]
    else:
        rerollable = [0, 1, 2]

    if not rerollable:
        print("No dice can be rerolled. Turn is over!")
        break 
#Ask user their prefrence to roll again or not
preference = input("Do you want to continue rolling dice? (yes/no): ").lower()
if preference != 'yes':
    print(f"{name} ends turn with {turn_score} points.")
else: 
    turn_score = sum(dice)
    print(f"Continuing turn. Current score: {turn_score}")
    current_dice = dice
    print(f"New roll: {dice}")

#Computer's turn
print("\nComputer's Turn!")
dice = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
print(f"\nComputer's initial roll: {dice}")

turn_score = 0
active_turn = True
while active_turn:
    if dice [0] == dice[1] or dice [0] == dice [2] or dice [1] == dice[2]:
        print("Computer tupled out! Scored 0 points.")
        turn_score = 0
        active_turn = False
    else:
        turn_score = sum(dice)
        print(f"Computer's current dice score is: {turn_score}")
        if dice [0] == dice[1]:
            rerollable = [2]
        elif dice [0] == dice[2]:
            rerollable = [1]
        elif dice [1] == dice [2]:
            rerollable = [0]
        else:
            rerollable = [0, 1, 2]

    if not rerollable:
        print("No dice can be rerolled. Turn is over!")
        break 

    print("Computer decides to re-roll.")
    dice = [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    print(f"New roll: {dice}")
print (f"Computer ended turn with:{turn_score}")

if scores["Player"] >= Target_Score:
    print(f"Congratulations, {name}, You are the winner!")
else:
    print("Computer wins! Try again next time.")
