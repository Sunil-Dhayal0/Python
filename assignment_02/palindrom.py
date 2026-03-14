def is_palindrom(n):
    if n < 0:
        return False
    reversed_num = 0
    orignal_num = n
    while n > 0:
        last_digit = n%10
        reversed_num = reversed_num*10 + last_digit 
        n//=10
    
    if orignal_num == reversed_num:
        return True
    else:
        return False
    

number = int(input("enter the number :"))

print("is number palindrom or not ",is_palindrom(121))
 