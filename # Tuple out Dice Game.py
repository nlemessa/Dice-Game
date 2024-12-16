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
    return random.choices([1, 2, 3, 4, 5, 6], k=3)
dice = dice_rolls()
print(f"You rolled: {dice}")
score = 0

def count_howmanytimes(dice):
    """
    Count how many times a value on a die is rolled
    """
    dice_list = list(dice)
    return [dice_list.count(value) for value in range(1, 7)]

while True:
    if dice[0] == dice[1] == dice[2]:
        print("You have tupled out! You scored 0 points." )
        score = 0
        break 

    fixed = []
    unfixed = []
    if dice[0] == dice[1] or dice[0] == dice[2]:
        fixed.append(dice[0])
    if dice[1] == dice[2]:
        fixed.append(dice[1])
    

# Counting how many times a number appears 

my_rolls = dice_rolls()
print("Dice rolls:", my_rolls)
roll_counts = count_howmanytimes(my_rolls)
print("Count of each number rolled:", roll_counts)

#Calculating scores 
def score_calculation(dice):
    """
    Calculates the score from a dice roll and gives a sum of the numbers
    A tuple that will indicate whether or not the player or computer has tupled out.
    """
    counts = count_howmanytimes(dice)
    if max(counts) >= 3:  # Changed to check for 3 or more of any number
        return 0, True
    return sum(dice), False 

def play_turn(player_name):
    """
    Play a turn for the player
    Gives the player and computer the decision to keep rolling or stop
    """
    current_dice = dice_rolls()
    print(f"\n{player_name}'s initial roll: {current_dice}")
# Check if there is a tuple out 
    while True:
        turn_score, tupled_out = score_calculation(current_dice)
        if tupled_out:
            print(f"{player_name} tupled out with {current_dice}! Scored 0 points.")
            turn_score = 0 
            break
        print(f"{player_name}'s current score: {turn_score}")
        # Give the option to the player whether or not they want to keep rolling
        preference = input("Do you want to continue rolling dice? (yes/no): ").lower()
        if preference =='no':
            print(f"{player_name} ends turn with {turn_score} points.")
            score = sum(dice)
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
