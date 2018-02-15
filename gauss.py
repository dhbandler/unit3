#Daniel Bandler
#2/15/18
#gauss.py adds up numbers from 1-100
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
dif = int(input("What number do you want to count by? "))
total = 0
for i in range(num1,num2+1,dif):
    total = total + i
    
print(total)
