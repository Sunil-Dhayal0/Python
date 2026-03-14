# sum_digits

num = int(input("enter the number :"))

sum = 0

while num > 0:
    digit = num%10
    sum+=digit
    num/=10

print(int(sum))