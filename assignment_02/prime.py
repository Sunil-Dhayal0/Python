import math

num = int(input("enter the number to check prime or not: "))
flage = True  # Assume it is prime

if num <= 1:
    flage = False
elif num == 2:
    flage = True
elif num % 2 == 0:
    flage = False
else:
    limit = int(math.sqrt(num)) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            flage = False 
            break         
            
print(flage)


  