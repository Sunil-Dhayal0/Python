
# 2. Simple Calculator with Multiple Exceptions
# Create a menu-driven calculator program for:
#  addition
#  subtraction
#  multiplication
#  division
# Requirements:
#  Accept two numbers from the user.
#  Handle:
# o ValueError for invalid input
# o ZeroDivisionError for division by zero
# o invalid menu choice using raise
#  Show proper messages for each case.


try:
     print("========menu calculator==========")
     print("for addition type 1: ")
     print("for subtraction type 2: ")
     print("for multiplication type 3: ")
     print("for division type 4: ")
     
     op = int(input("enter the operation you want to perform"))
     if op > 5:
      raise ValueError("op should be integer and in the range")
     try:     
         num1  = int(input("enter the number 1 "))
         num2  = int(input("enter the number 2 "))
         
         match op:
             case 1:
                 sum = num1+num2
                 print(f"sum of number is {sum}")
             case 2:
                 sub = num1-num2
                 print(f"sub of number is {sub}")
             case 3:
                 mul = num1*num2
                 print(f"mul of number is {mul}")
             case 4:
                 div = num1//num2
                 print(f"sum of number is {div}")
                 
     except ValueError:
         raise ValueError("both input should be integer: ")    

except Exception as e:
    print(f"error is :---> {e}")
