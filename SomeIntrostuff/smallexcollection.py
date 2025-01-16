#quiz prg

questions=("What is the fastest bird?: ",
           "What is the fastest land animal?: ",
           "What year are we currently in?: ",
           "Which country among these is a hot spot for tourism?: ",
           "Where is the hanging gardens of babylon located?: ")

options = (("A. Pigeon","B. Falcon","C. Mocking","D. Dove"),
           ("A. Rhino","B. Tiger","C. Cheetah","D. Leopard"),
           ("A. 2027","B. 2025","C. 2024","D. 2026"),
           ("A. Japan","B. America","C. Canada","D. England"),
           ("A. Iraq","B. Italy","C. Portugual","D. Russia"))

asnwers=("B","C","B","A","A")
guesses=[]
score=0
question_number=0


for question in questions:
    print("------------")
    print(question)
    for option in options[question_number]:
        print(option)
    
    guess=input("Enter A B C or D: ").upper()
    guesses.append(guess)
    if guess == asnwers[question_number]:
        score+=1
        print("Correct ans")
    else:
        print("INCorrect ans")
        print(f"{asnwers[question_number]} is the correct answer")
    question_number+=1

print()
print("RESULTS")
print("asnwers: ", end=" ")
for answer in asnwers:
    print(answer, end="")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end="")
print()

score= int(score/len(questions)*100)
print(f"Your score is : {score}%")
