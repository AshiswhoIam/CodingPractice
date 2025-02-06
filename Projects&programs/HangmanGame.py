#hangman in py

#set of words
from HangmanWords import words
import random


#dictionary of key:()   key and tuple
hangman_art={0: ("   ",
                 "   ",
                 "   "),
             1: (" o ",
                 "   ",
                 "   "),
             2: (" o ",
                 " | ",
                 "   "),
             3: (" o ",
                 "/| ",
                 "   "),
             4: (" o ",
                 "/|\\ ",
                 "   "),
             5: (" o ",
                 "/|\\ ",
                 "/   "),
             6: (" o ",
                 "/|\\ ",
                 "/ \\ ") }

#for line in hangman_art[3]:
#    print(line)

#display of the ascii
def display_man(wrong_guesses):
    print("===================")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("===================")

#hint display for # of letters using join to format side by side
def display_hint(hint):
    print(" ".join(hint))

#answer of word display
def display_ans(ans):
    print(" ".join(ans))

#ans used to randomize words, hint len for the hints displayed based on length, wg = 0 to keep track for displaying wg for errors
#creating aset of guessed letters so later user cant guess again the same
def main():
    ans=random.choice(words)
    hint = ["_"]*len(ans)
    wrong_guesses=0
    guessed_letters=set()
    #bool to break loop
    is_running=True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        #display_hint(ans)
        guess=input("Enter the desired letter: ").lower()

        #if statements to prevent different inputs

        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input")
            print()
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in ans:
            for i in range(len(ans)):
                if ans[i]==guess:
                    hint[i]=guess
        else:
            wrong_guesses+=1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_ans(ans)
            print("You guessed it congrats!")
            is_running=False
        #out of lives here
        elif wrong_guesses>=len(hangman_art)-1:
            display_man(wrong_guesses)
            display_ans(ans)
            print("You ran out of lives and lost! ")
            is_running=False




if __name__ == '__main__':
    main()