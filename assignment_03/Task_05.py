#  Base class:
# o Employee → attributes: id, name
#  Derived classes:
# o Manager → attribute: bonus
# o Developer → attribute: programming_language
# Tasks:
# 1. Implement the class hierarchy.
# 2. Demonstrate how common properties are inherited.
# 3. Show object creation for both derived classes.

class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def display(self):
        print(f"name :{self.name} and bonus {self.bonus}")

class Manager(Employee):
    def __init__(self, id, name,bonus,programming_language):
        super().__init__(id, name)
        self.bonus = bonus
        self.programming_language = programming_language
    def display(self):
        super().display()


class Developer(Employee):
    def __init__(self, id, name,bonus,programming_language):
        super().__init__(id, name)
        self.bonus = bonus
        self.programming_language = programming_language
    def display(self):
        super().display()


m1 = Manager(101,"sunil",300,"c++")
d1 = Developer(1002,"amit",20,"java")

m1.display()