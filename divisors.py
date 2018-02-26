#Daniel Bandler
#2/26/18
#divisors.py finds round divisors of number
num = int(input("Input a number here "))
for i in range(1,num//2+1):
    if num % i == 0:
        print(i)

    