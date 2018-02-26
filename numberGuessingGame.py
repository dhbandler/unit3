#Daniel Bandler
#2/16/18
#numberGuessingGame.py plays guessing game
from random import *
num = randint(1,100)
tries = 0
for i in range(1,101):
    guess = int(input("Guess a number between 1 and 100"))
    if guess > num:
        print("Your guess (", guess, ") was too high")
    elif guess < num:
        print("Your guess (", guess, ") was too low")
    elif guess == num:
        print("It is ", num, "!  You got it right!")
        break
    else:
        print("Invalid input")
        
    tries = tries + 1
    
print("it took you ", tries, " tries")
    
    
