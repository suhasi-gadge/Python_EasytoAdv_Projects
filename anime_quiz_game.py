print("Welcome to My Anime Quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()

print("Alright! let's Play :)")
score = 0

answer = input("What is the name of the main character in Naruto? ")
if answer.lower() == "naruto uzumaki":
    print("Correct Answer!")
    score += 10
else:
    print("Wrong Answer :( Try Again!")


answer = input("Which anime features a boy who turns into a Titan? ")
if answer.lower() == "attack on titan":
    print("Correct Answer!")
    score += 10
else:
    print("Wrong Answer :( Try Again!")


answer = input("What is the name of the Soul Reaper in Bleach? ")
if answer.lower() == "ichigo kurosaki":
    print("Correct Answer!")
    score += 10
else:
    print("Wrong Answer :( Try Again!")


answer = input("In Death Note, what is the name of the Shinigami? ")
if answer.lower() == "ryuk":
    print("Correct Answer!")
    score += 10
else:
    print("Wrong Answer :( Try Again!")


answer = input("Name a hero who defeats every villain with one punch. ")
if answer.lower() == "one punch man":
    print("Correct Answer!")
    score += 10
else:
    print("Wrong Answer :( Try Again!")

answer = input("What is the name of the main character in One Piece? ")
if answer.lower() == "monkey d. luffy":
    print("Correct Answer!")
    score += 10
else:
    print("Wrong Answer :( Try Again!")

print ("You got " +  str(score)  + " points!")