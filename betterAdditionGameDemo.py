#Daniel Bandler
#2/28/18
#betterAdditionGameDemo.py - more loop practice

from random import randint
numCorrect = 0

while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    answer = int(input("what is " + str(num1) + " + " + str(num2) + "? "))
    if answer == num1 + num2:
        numCorrect += 1
        print(answer, "is correct!")
    else:
        print("WRONG! Answer is.... ", num1 + num2, "!")
        
print("You win!")

