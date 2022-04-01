import random

choices = ["rock", "paper", "scissors"]
i = 0
j = 0
winner = ""
wins = 0
losses = 0
ties = 0

while i < 3:
    while j < 3:
        player = None
        while player not in choices:
            player = input("rock, paper or scissors: ")
        computer = random.choice(choices)
        if player == computer:
            print("Computer: ", computer)
            print("Player: ", player)
            print("Tie!")
            ties += 1
        elif player == "rock":
            if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You LOSE!")
                losses += 1
            if computer == "scissors":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You WIN!")
                wins += 1
        elif player == "paper":
            if computer == "scissors":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You LOSE!")
                losses += 1
            if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You WIN!")
                wins += 1
        elif player == "scissors":
            if computer == "rock":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You LOSE!")
                losses += 1
            if computer == "paper":
                print("Computer: ", computer)
                print("Player: ", player)
                print("You WIN!")
                wins += 1
        j += 1
    retry = input("Would you like to play again (Y/N)?: ")
    if retry == "YES" or retry == "yes" or retry == "Y" or retry == "y" or retry == "Yes":
        print("RESTARTING...")
        continue
    elif retry == "NO" or retry == "no" or retry == "N" or retry == "n" or retry == "No":
        print("BYE!")
        break

if wins == losses:
    print("A Tie with ", str(wins), " wins, ", str(losses), " losses, and ", str(ties), " ties.")
elif wins > losses:
    print("You win with ", str(wins), " wins, ", str(losses), " losses, and ", str(ties), " ties.")
else:
    print("You Lose with ", str(wins), " wins, ", str(losses), " losses, and ", str(ties), " ties.")
