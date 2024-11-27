# Tuple out Dice Game

import random

print("Welcome to tuple out dice game!")

# User enters their name
def player_name():
    """
    Asks the player to enter their name 
    Then returns the name that was entered 
    """
    name = input("Enter your name please.")
    print(f"Let the games begin {name}!")
    return name

player_name()

# User rolls dice 
def dice_rolls():
    """
    Simulates rolling three six-sided dice
    Then return a set of three numbers that are the outcomes of the dice roll
    """
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    return [roll1, roll2, roll3]

# Check which dice can be rerolled
def rerollable_dice(dice):
    """
    Finds which dice from the three can be rerolled.
    """
    if dice [0] == dice[1]:
        return [2]
    elif dice [0] == dice[2]:
        return[1]
    elif dice [1] == dice [2]:
        return [0]
    return[0, 1, 2]

def play_turn(player_name):
    """
    Play a turn for the player
    Gives the player and computer the decision to keep rolling or stop
    """
    print(f"\n{player_name}'s turn!")
    dice = dice_rolls()
    print(f"\n{player_name}'s initial roll: {dice}")

    turn_score = 0
# Check if there is a tuple out 
    while True:
       if dice [0] == dice[1] == dice[2]:
           print("You tupled out! 0 points scored.")
           return 0
       turn_score = sum(dice)
       print(f"Current dice score: {turn_score}")

       rerollable = rerollable_dice(dice)
       if not rerollable:
           print("No dice can be rolled. Turn is over!")
           break
       preference = input("Do you want to continue rolling dice? (yes/no): ").lower()
       if preference != 'yes':
           print(f"{player_name} ends turn with {turn_score} points.")
           break
    else: 
        print(f"Continuing turn. Current score: {turn_score}")
        current_dice = dice_rolls()
        print(f"New roll: {current_dice}")
    return(turn_score)

def main():
    """
    Function which plays the "Tuple Out" Dice Game
    """
    Target_Score = 50
    scores = {"Player": 0, "Computer": 0}   

    print("Welcome to Tuple out Dice Game!")
    print(f"First to {Target_Score} points wins!\n")

    player = player_name()

    while scores["Player"] < Target_Score and scores["Computer"] < Target_Score:
        print("\nPlayer's Turn!")
        scores["Player"] += play_turn("Player")

        print("\nComputer's Turn!")
        scores["Computer"] += play_turn("Computer")

        print(f"Scores: Player {scores['Player']}, Computer {scores['Computer']}\n")
    if scores["Player"]>= Target_Score:
        print(f"Congratulations, {player} YOU WIN!")
    else:
        print("Computer wins! Better luck next time!")
main()