import random

# Initialize score counters
player_score = 0
ai_score = 0

# Available choices
choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock-Paper-Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'q' anytime to quit.\n")

while True:
    player_move = input("Your move: ").strip().lower()

    if player_move == "q":
        print("\nThanks for playing! Final Score:")
        print(f"👉 You: {player_score} | 🤖 Computer: {ai_score}")
        break

    if player_move not in choices:
        print("⚠ Invalid choice! Please pick rock, paper, or scissors.\n")
        continue

    # Computer makes a random choice
    computer_move = random.choice(choices)
    print(f"Computer chooses: {computer_move}")

    # Determine the winner
    if (player_move == "rock" and computer_move == "scissors") or \
       (player_move == "paper" and computer_move == "rock") or \
       (player_move == "scissors" and computer_move == "paper"):
        print("🎉 You win this round!")
        player_score += 1
    elif player_move == computer_move:
        print("🤝 It's a tie!")
    else:
        print("💻 Computer wins this round!")
        ai_score += 1

    print(f"Current Score -> You: {player_score} | Computer: {ai_score}\n")
