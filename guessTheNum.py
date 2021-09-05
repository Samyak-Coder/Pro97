import random
print ("Number Guessing Game")

number = random.randint(1,9)
chances = 0

print ("Guess a number between 1 to 9:")

while chances < 5:
    guess = int(input("Enter Your guess:- "))

    if guess == number:
        print ("Congratulations! You Won!")
    else:
        print("Try again")