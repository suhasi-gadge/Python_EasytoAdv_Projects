# Simple Text Adventure Game

player_name = input("Hey there! What's your name? ")
print(f"\nHi {player_name}, welcome to the world of choices!\n")

direction = input("You're standing at a fork in a dusty trail. Do you go 'left' or 'right'? ").lower()

if direction == "left":
    river_choice = input(
        "\nYou reach a wide river. Would you rather 'walk' around it or try to 'swim' across it? ").lower()

    if river_choice == "swim":
        print("\nYou try to swim, but sadly, an alligator was faster than you. Game over!")
    elif river_choice == "walk":
        print("\nYou walk for hours, dehydrated and lost... eventually collapsing. Game over.")
    else:
        print("\nThat wasn't a valid choice. The forest swallows you. Game over.")

elif direction == "right":
    bridge_decision = input(
        "\nYou find a shaky old bridge. Do you want to 'cross' it or go 'back'? ").lower()

    if bridge_decision == "back":
        print("\nYou head back the way you came and find nothing. Game over.")
    elif bridge_decision == "cross":
        stranger_interaction = input(
            "\nYou carefully cross the bridge and see a mysterious figure. Do you talk to them? ('yes' or 'no'): ").lower()

        if stranger_interaction == "yes":
            print("\nTurns out they were a friendly traveler! They hand you a pouch of gold. You WIN!")
        elif stranger_interaction == "no":
            print("\nThe stranger feels insulted and vanishes. You missed your chance. Game over.")
        else:
            print("\nUnrecognized response. Fate isn't kind to hesitation. Game over.")
    else:
        print("\nThat's not a real option. You stand confused until night falls. Game over.")

else:
    print("\nThat's not one of the paths. You get stuck and the game ends.")

print(f"\nThanks for playing, {player_name}! Come back soon for another adventure.")
