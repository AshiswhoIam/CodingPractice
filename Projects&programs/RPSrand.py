import random

options=("rock", "paper","scissors")


run=True

while run:
    player=None
    computer= random.choice(options)
    print()
    while player not in options:
        player = input("Enter a choice(rock paper or scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player=="rock" and computer == "scissors":
        print("You win")
    elif player=="paper" and computer == "rock":
        print("You win")
    elif player=="scissors" and computer == "paper":
        print("You win")
    else:
        print("you lost.")

    play_again= input("Enter y or n to either play again or not: ").lower()
    if not play_again=="y":
        run=False

print("games done")

