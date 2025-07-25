import random

print("🎯 Welcome to the Number Guessing Game!")
upper_limit = input("Enter the maximum number I can choose from: ")

if not upper_limit.isdigit():
    print("❌ That wasn't a valid number. Please restart the game and enter a positive number.")
    exit()

max_value = int(upper_limit)

if max_value <= 0:
    print("⚠️ Please enter a number greater than 0.")
    exit()

secret_number = random.randint(0, max_value)
attempt_count = 0

while True:
    guess = input("🔢 Your guess: ")

    if not guess.isdigit():
        print("⛔ Numbers only please!")
        continue

    guess = int(guess)
    attempt_count += 1

    if guess == secret_number:
        print(f"🎉 Correct! You guessed it in {attempt_count} tries.")
        break
    elif guess < secret_number:
        print("📉 Too low! Try again.")
    else:
        print("📈 Too high! Try again.")
