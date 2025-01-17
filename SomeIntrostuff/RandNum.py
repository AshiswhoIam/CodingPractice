import random

low=1
high=100
number= random.randint(low,high)
num=random.random()
print(number)
print(num)

options =("rock,paper,scissors")
option= random.choice(options)
print(option)

cards = ["2","3","4","5","6","7"]
random.shuffle(cards)
print(cards)


#exercise num guessing game

low_n=1
high_n=100
ans= random.randint(low_n,high_n)
guesses=0
is_running=True
print()
print("Num guesssing game")
print(f"Select a num b/w {low_n} and {high_n}: ")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess= int(guess)
        guesses+=1
        if guess < low_n or guess > high_n:
            print("num is not within range")
            print(f"Must Select a num b/w {low_n} and {high_n}: ")
        elif guess< ans:
            print("too low try again")
        elif guess > ans:
            print("too high try again")
        else:
            print(f"You got it, it was {ans}")
            print(f"Number of guesses: {guesses}")
            is_running=False
    else:
        print("Invalid guess")
        print(f"Must Select a num b/w {low_n} and {high_n}: ")


