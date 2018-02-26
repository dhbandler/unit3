#Daniel Bandler
#2/26/18
#perfectNumber.py finds if a number is perfect

num = int(input("enter a number"))
sum = 0
for i in range(1,num//2+1):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print(num, " is perfect")
else:
    print(num, " isn't perfect")
