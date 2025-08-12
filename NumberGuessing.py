import random

Random_number = random.randint(1,100)
Guessed_number = 0
Guess_count = 0

while (Guessed_number != Random_number):
    Guessed_number = int(input("Enter Your Guess :"))

    if(Guessed_number > Random_number):
        print("You have to guess a lower Number!!")
        Guess_count +=1
    elif(Guessed_number < Random_number):
        print("You have to guess a higher number!!!!")
        Guess_count +=1
    else:
        print("~~~!!!You Guessed it right!!!~~~")

print(f"you have taken '{Guess_count}' number of guesses.")