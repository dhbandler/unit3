#Daniel Bandler
#3/5/18
#quiz3.py -- tank my GPA by performing a variety of tasks
print("Prints out the numbers -15,-14,-13,...,-10,-9 using a while loop") #I used print statements to break it up in the console

i = -15
while i <= -9:
    print(i)
    i += 1

print("Prints out numbers 50,46,42,38...,22, 18 using a for loop")

for i in range(50,18,-4):
    print(i)

print("Prints out the sum of the even numbers from -100 to 1000 using my loop choice")

i = -100
total = 0
while i <= 1000:
    total += i
    i += 2
print(total, "is the sum")

print("Asks the user to guess until they type alpaca")

i = 0
while i == 0:
    guess = input("Type something: ")
    if guess == "alpaca":
        print("Password guessed against the odds")
        break
    else:
        print("nope")