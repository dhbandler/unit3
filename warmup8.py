#Daniel Bandler
#2/28/18
#warmup8.py - Find the sum of numbers less than 100,000 that are divisible by 3, 10 and 17
i = 1
total = 0
for i in range(1,100001):
    
    if i%3==0 and i%10==0 and i%17==0:
        total = total + i
    i+=1
print(total)
    


