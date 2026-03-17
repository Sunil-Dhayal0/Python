# Question 1 – Student Management System
# Create a Python class Student to manage student information.

# The class should have the following features:

# A class variable school_name set to "CDAC : AI Learning Academy".

# A constructor (__init__) that accepts:

# student name
# age
# course
# A method display_info() to display the student details:

# Student Name
# Age
# Course
# School Name
# A method is_adult() that checks whether the student is an adult (age ≥ 18).

# Application Task
# Create two student objects with different details.
# Display their information.
# Check whether each student is an adult.


class Student:

    school_name = "CDAC : AI Learning Academy"

    def __init__(self,student_name,age,course):
        self.studentName = student_name
        self.sAge  = age
        self.scourse = course
 
    def display_info1(cls):
         print(f'student school name is {cls.school_name}')
         

    def display_info(self):
        print(f'student name is {self.studentName}')
        print(f'student age is {self.sAge} ')
        print(f'student course is {self.scourse}')   
        self.display_info1()  

    def is_adult(self):
        if self.sAge > 18:

            print(f" {self.studentName} is adult")        

student1 = Student("sunil",23,"Ai")
student1.display_info()
student1.is_adult()