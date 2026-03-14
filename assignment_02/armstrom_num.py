#armstrom num

num = int(input("enter the number: "))

in_num = num
reversed_num = 0

while num > 0:
    last_digit = num%10
    reversed_num = reversed_num*10 + last_digit
    num//=10

print(reversed_num)
if in_num == reversed_num:
    print(f"number is armstrom number: {in_num}")
else:
    print(f"enter number is not armstrom: {in_num}")