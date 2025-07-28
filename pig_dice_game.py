import random

# --- Game Constants ---
WINNING_SCORE = 100

# --- Game Functions ---

def roll_die():
    """Simulates rolling a 6-sided die."""
    return random.randint(1, 6)

def next_player(current_index, total_players):
    """Returns the index of the next player."""
    return (current_index + 1) % total_players

def take_turn(player_name):
    """Executes a single player's turn."""
    turn_total = 0
    while True:
        print(f"\n{player_name}'s turn. Current turn total: {turn_total}")
        choice = input("Roll or Hold? (r/h): ").strip().lower()

        if choice == 'r':
            roll = roll_die()
            print(f"Rolled: {roll}")
            if roll == 1:
                print("Oops! Rolled a 1. Turn over. No points gained this turn.")
                return 0
            else:
                turn_total += roll
        elif choice == 'h':
            print(f"Holding. {player_name} gains {turn_total} points.")
            return turn_total
        else:
            print("Invalid input. Enter 'r' to roll or 'h' to hold.")

def print_scores(scores, player_names):
    print("\n-- Current Scores --")
    for i, score in enumerate(scores):
        print(f"{player_names[i]}: {score}")
    print("---------------------")

# --- Main Game Loop ---

def main():
    print("🎲 Welcome to the PIG Dice Game!")
    num_players = int(input("Enter number of players: "))
    player_names = [input(f"Enter name for Player {i + 1}: ") for i in range(num_players)]
    scores = [0] * num_players
    current_player = 0

    while max(scores) < WINNING_SCORE:
        print_scores(scores, player_names)
        gained = take_turn(player_names[current_player])
        scores[current_player] += gained

        if scores[current_player] >= WINNING_SCORE:
            print_scores(scores, player_names)
            print(f"\n🏆 {player_names[current_player]} wins with {scores[current_player]} points!")
            break

        current_player = next_player(current_player, num_players)

if __name__ == "__main__":
    main()
