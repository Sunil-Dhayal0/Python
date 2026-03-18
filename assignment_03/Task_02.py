# Q2. Student Result System
# Create a class Student with:
#  Private attribute:
# o marks
#  Public methods:
# o setMarks(m)
# o getGrade()
# Conditions:
#  Marks must be between 0 and 100.
#  Grade calculation:
# o A (≥ 80)
# o B (≥ 60)
# o C (≥ 40)
# o Fail (< 40)
# Tasks:
# 1. Implement validation logic using setter method.
# 2. Write code to calculate and display grade.
# 3. Explain why marks should be kept private

class student:
    def __init__(self,marks):
        self.__marks = marks
    def setMarks(self,marks):
        self.__marks = marks
    def getGrade(self):
        if self.__marks >= 80:
            return 'A'
        elif self.__marks >= 60 and self.__marks < 80:
            return 'B'
        elif self.__marks >= 40 and self.__marks < 60:
            return 'C'
        elif self.__marks < 40:
            return'Fail'

s1 = student(80)
s1.__marks = 100
print(s1.getGrade())