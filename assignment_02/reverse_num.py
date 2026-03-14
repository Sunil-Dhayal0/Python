num = int(input("enter the number"))
ans = 0
while num > 0:
    last_digit = num%10
    ans = ans*10 + last_digit   
    num//=10


print(ans,end=" ")