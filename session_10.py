# Polymorphism
#  operator overloading   (+) 1. used for add and 2. used for concatenation of string



########--------magic method

# magic methiods are  special method:
#  they have double underscore before and after the name.
# they are also called as dunder method
# python program call them automaticallly , in defined situation.
# they help objects behave like built-in data types.

#--example
# ex 1.__init__
#    2.__str__  : called when print(object) is used
#    3.__len__  :             print(len(object))
#    4.__add__  :              obj1+obj2
#    5.__eq__   :             obj1+obj2
#    6.__getitem__:           called when indexing is used

# key pointer
# to  itialize objects
#  to print object in a readable form
# to use operator,like +,-,==
# to use bulit-in functions like len(),max()
# to support indexing like obj[0]


# class Test:
#     def __init__(self,name):
#         self.name = name
    
#     def __str__(self):
#         return f'employeeName:{self.name}'
#     def __len__(self):
#         return len(self.name)
#     def __add__(self, other):
#         return self.name + other




# t1 = Test("sunil")
# print(t1)
# print(len(t1))
# t2 = Test("dhayal")

# print(t1+t2)

# name = 'sunil'
# sal = 300

# method 4. using formate()
# print("name  = {0}, salary = {1}".format(name,sal))
# print("name  = {name}, salary = {sal}".format(name = 'amit',sal = 23111))


# method 5 . using f-string

# print(f'my name is {name}')

# x = 1234.13446785
# print(f'{x:.2f}')
# print(f'{x:10}')
# print(f'{x:<1}')

#########---------Is-A realtion

# class Vehicle:

#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(f"{self.brand} {self.model} is starting")
#     def stop(self):
#         print(f"{self.brand} {self.model} is stoping")

# class Car(Vehicle):
#     def __init__(self, brand, model,fuel_type):
#         super().__init__(brand, model)
#         self.fuel_type = fuel_type
    
#     def display(self):
#         print('car class info....')

# class bike(Vehicle):
#     def __init__(self, brand, model,cc):
#         super().__init__(brand, model)
#         self.cc = cc
#     def display():
#         print('bike class info ----')


# c1 = Car("hyundai","Creta","Electric")
# b1 = bike("Royal Enfield","classic",350)


#  Has- A realtion -----------------most important--------prepare

# class Engine:
#     def __init__(self,engine_no,power):
#         self.engine_no = engine_no
#         self.power = power
    
#     def start(self):
#         print('starting Engine')


# class Car:
#     def __init__(self,brand, model,engine):
#         self.brand = brand
#         self.model = model
#         self.engine = engine
#     def start_car(self):
#         print(f"start car {self.brand} with model {self.model} having {self.engine.engine_no}")
#         self.engine.start()

#     def display(self):
#         print("car details........")
#         print(f"brand {self.brand}")
#         print(f"car mode is {self.model}")
#         print(f"car engine is {self.engine}")


# e1 = Engine("ABC23466DFH",15000)

# c1 = Car("hundia","ABC23466DFH",e1)

# c1.start_car()




##----- Association
##  A general realtionship where one object releated to another object
# A tecaher teaches student
# both classes can exist independently
# class student:
#     def __init__(self,name):
#         self.name = name


# class teacher:
#     def __init__(self,name):
#         self.name = name
#     def teach(self,student_1):
#         print(f'{self.name} teaches {student_1.name}')


# s1 = student("neha")
# t1 = teacher('ravi')
# t1.teach(s1)


##--------- Aggregation:
#  A weak Has-A reationship is represented by aggregation.
#  one object uses or contains another object,
#  but the contained object can exit independently
#   example one to many in one department there is more than one employee

# class employee:
#     def __init__(self,name):
#         self.name = name
    
# class department:
#     def __init__(self,dname):
#         self.dname = dname
#         self.employees = []
#     def addemp(self,employee):
#         self.employees.append(employee)
#     def display(self):
#         print(f"dpart name is {self.dname}")
#         for i in self.employees:
#             print(f'employee name is {i.name}')

# e1 = employee("ravi")
# e2 = employee('sunil')
# e3 = employee("amit")

# d1 = department('Ai')

# d1.addemp(e1)
# d1.addemp(e2)
# d1.addemp(e3)
# d1.display()


####---------Composition
#  a strong Has_A realtionship  is represented by composition 
#  the contained object is strongly owned by the container, and its container,
# ex A house has room


class Room:
    def __init__(self,room_type):
        self.room_type = room_type

class House:
    def __init__(self):
        self.r1 = Room("kitchen")
        self.r2 = Room("Balcony")

    def display(self):
        print(f'House have {self.r1.room_type} and {self.r2.room_type}')


h1 = House()

h1.display()


# polymorphism:
# it is the ability of the same operation to behave differently for different object.
#  need of polymorphism:
# __________it imporoves code reusablilty
#    it improve readbility
#    it allows same interface for different object
#    support extensibilty


# type of polymorphism
#  compile time    -> also called static polymorphism
#   occure at compile time
#    method overloading

#  run time        -> also called dynamic polymorphism
#    method overriding


# example of compile time polymorphism
# class A:
#     def m1(self,a =None,b = None):
#         if a is not None and b is not None:
#             print(a + b)
#         elif a is not None:
#             print(a)
#         else:
#             print(b)

# a1 = A()

# a1.m1(10)
# a1.m1(10,22)

# example of run time polymorphism

# class A:
#     def m1(self):
#         print("class A : m1()")

# class B(A):
#     def m1(self):
#         print("class B :m1() : child class")


# b1 = B()

# b1.m1()


#  polymorphism -> operator overloading example + 
#  -> method overrinding   example same methods different class
# -> function compatiblity  example len(),max()

#1.polymorphism through   method overriding         -> run time polymorphism 

# class A:
#     def m1(self):
#         print("class A : m1()")

# class B(A):
#     def m1(self):
#         print("class B :m1() : child class")


# b1 = B()

# b1.m1()

#2.polymorphism through -> operator overloading     -> compile time polymorphism

#3. polymorphism : through method overloading style  -> compile time polymorphism
#   default argument
#   *args
# 

class A:
    def m1(self,a =None,b = None):
        if a is not None and b is not None:
            print(a + b)
        elif a is not None:
            print(a)
        else:
            print(b)

a1 = A()

a1.m1(10)
a1.m1(10,22)

#5.polymorphism duck typing  -> compile time polymorphism

class A:
    def m1(self):
        print("Class A: m1()")
class B:
    def m1(self):
        print("class B m1()")

def call(obj):
    obj.m1()

call(A())
call(B())


# 6. polymorphism -> through built in functions -> overloading

print(len("sona math! ! ! ! "))
print(len([10,20,30,40]))
print(len((1,2,3,4,5)))

