import random

def roll_dice(num_dice=3):
    """
    Roll a specified number of dice and return the results as a tuple.
    """
    for i in range(3):
        dice.append(random.randint(1,6))
    return dice 

def count_occurences(dice):
    """Count the occurences of each die value."""
    counts = [0,0,0,0,0,0,0]
    for die in dice:
        counts[die] = counts[die] + 1
    return counts

def can_reroll(dice):
    """Determine which dice can be rerolled."""
    counts = count_occurences(dice)
    fixed_value = None
    for value in range(len(counts)):
        if counts[value] == 2:
            fixed_value = value 
            break

reroll_positions = []
position = 0
for die in dice:
    if die != fixed_value:
        re


def get_reroll_positions(current_dice):
    """
    Determine which dice can be rerolled based on fixed values (pairs).
    """
    counter = Counter(current_dice)
    fixed_value = next((value for value, count in counter.items() if count == 2), None)
    if fixed_value is not None:
        return [i for i, value in enumerate(current_dice) if value != fixed_value]
    return list(range(len(current_dice)))  # All dice can be rerolled


def computer_decision(current_dice, reroll_positions):
    """
    Computer strategy for deciding whether to reroll or stop.
    If the sum of the dice is high, or if fixed values are strong, stop.
    """
    dice_sum = sum(current_dice)
    fixed_value = next((value for value, count in Counter(current_dice).items() if count == 2), None)
    if dice_sum >= 12 or (fixed_value and fixed_value >= 4):
        return False  # Stop rolling
    return True  # Continue rolling


def play_turn(player, scores, target_score):
    """
    Play a single turn for the given player.
    Handles both the player's and computer's decisions.
    """
    current_dice = roll_dice()
    print(f"\n{player}'s initial roll: {current_dice}")

    turn_score = 0
    while True:
        counter = Counter(current_dice)

        # Check for tuple out
        if any(count == 3 for count in counter.values()):
            print(f"{player} tupled out with {current_dice}! No points scored.")
            return 0

        # Determine reroll positions
        reroll_positions = get_reroll_positions(current_dice)

        # Player decision
        if player == "Player":
            print(f"Current dice: {current_dice}")
            if input("Do you want to reroll? (y/n): ").lower() != 'y':
                turn_score = sum(current_dice)
                print(f"{player} stops with {turn_score} points.")
                return turn_score

            # Perform reroll
            dice_list = list(current_dice)
            for pos in reroll_positions:
                dice_list[pos] = random.randint(1, 6)
            current_dice = tuple(dice_list)
            print(f"New roll: {current_dice}")

        # Computer decision
        else:
            if not computer_decision(current_dice, reroll_positions):
                turn_score = sum(current_dice)
                print(f"Computer stops with {turn_score} points.")
                return turn_score

            # Perform reroll
            dice_list = list(current_dice)
            for pos in reroll_positions:
                dice_list[pos] = random.randint(1, 6)
            current_dice = tuple(dice_list)
            print(f"Computer rerolls: {current_dice}")


def main():
    """
    Main function to play the "Tuple Out" dice game.
    """
    TARGET_SCORE = 50
    scores = {"Player": 0, "Computer": 0}
    high_scores = {"Player": 0, "Computer": 0}
    game_history = {"Player": [], "Computer": []}

    print("Welcome to Tuple Out!")
    print(f"First to {TARGET_SCORE} points wins!\n")

    while True:
        # Reset game scores and history for a new game
        scores = {"Player": 0, "Computer": 0}
        game_history = {"Player": [], "Computer": []}

        while max(scores.values()) < TARGET_SCORE:
            for player in ["Player", "Computer"]:
                turn_score = play_turn(player, scores, TARGET_SCORE)
                scores[player] += turn_score
                game_history[player].append(turn_score)

                # Display current scores
                print("\nCurrent scores:")
                for p, s in scores.items():
                    print(f"{p}: {s}")

                # Check for a winner
                if scores[player] >= TARGET_SCORE:
                    print(f"\n{player} wins with {scores[player]} points!")
                    high_scores[player] = max(high_scores[player], scores[player])
                    break

            # Stop game if there is a winner
            if max(scores.values()) >= TARGET_SCORE:
                break

        # Display game statistics
        print("\nGame Statistics:")
        print("High Scores:")
        for player, score in high_scores.items():
            print(f"{player}: {score}")
        print("\nTurn History:")
        for player, history in game_history.items():
            print(f"{player}: {history}")

        # Ask to play again
        if input("\nPlay again? (y/n): ").lower() != 'y':
            break


if __name__ == "__main__":
    main()
