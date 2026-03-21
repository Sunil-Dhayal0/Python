# 1. Student Marks Input Validation
# Write a Python program that accepts marks of 5 students from the user and stores them in a list.
# Requirements:
#  If the user enters a non-numeric value, handle the exception.
#  If the marks are less than 0 or greater than 100, raise a ValueError.
#  Display the final valid list of marks.
#  Use try-except-else-finally.

try:

    marks = [int(x) for x in input("enter students marks: ").split()]
    
    for i in marks:
        if i < 0 and i > 100:
            raise ValueError(" value is less than 0 and more than 100")
    print(f"marks of students is {marks}") 

except Exception as e:
    print(f"error is {e}")

else:
    print("else is printed")
finally:
    print("me toh chalunga hi bhai")

