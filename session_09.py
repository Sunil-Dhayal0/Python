########---------- decorator example
# class Product:
#     def __init__(self,price):
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self,amount):
#         self.__price += amount
    
# p = Product(500)
# print(p.price)
# p.price = 500
# print(p.price)


#######---------- Inheritance:
# one class (child class/ drived class/ sub class) acquires the methods of another class(parend class/base class/super class )

# syntax
# class parentclassname:
#       state1
# class childclass(parentclassname):
#         state2

##---- advantages
#- code reuse
#- reduced code duplication
#- easy maintenance
#- logical program struture
#- supports hiearchical reationship
#- hybrid inheritance

#type of inheritance

#1. single inheritance:
# a- child class inherits properties and methods from only one parent class
# b- child class can access the methods of parent class
# c- this simplest form of inherotance

# class A:
#     def m1(self):
#         print("m1(): parent class method ")
# class B(A):
#     def m2(self):
#         print("m2() : child class method")

# s  = B()

# s.m1()

#2.multiple inheritance
#- A child class inherits properties and method from more than one parent class.


# class A:
#     def m1(self):
#         print("m1(): parent class method ")
# class B:
#     def m2(self):
#         print("m2() : child class method")

# class C(A,B):
#     def mf(self):
#         print('child function')

# c = C()
# c.m1()
# c.m2()
# c.mf()


#3.multi-level inheritance
# occurs in multiple levels.
# in this one class inherits from multiple derived class

# class A:
#     def m1(self):
#         print("m1(): parent class method ")
# class B(A):
#     def m2(self):
#         print("m2() : child class method")

# class C(B):
#     def mf(self):
#         print('child function')

# c = C()
# c.m1()
# c.m2()
# c.mf()

#4. hierarchical inheritance:
# multiple child classes inherits properties and methods from one parent class
#  parent class
# class A:
#     def m1(self):
#         print("m1(): parent class method ")
# # chid class one
# class B(A):
#     def m2(self):
#         print("m2() : child class method")
# # child class two
# class C(A):
#     def mf(self):
#         print('child function')

# b = B()
# b.m1()

# c = C()
# c.m1()


#5. hybrid inheritance:
#-it is a combination of two or more inheritance
# it may combination of multi + hierarchical
# it is more complex

# class A:
#     def m1(self):
#         print("m1(): parent class method ")
# # chid class one
# class B(A):
#     def m2(self):
#         print("m2() : child class method")
# # child class two
# class C(A):
#     def mf(self):
#         print('child function')
# class D(B,C):
#     def hybridIn(self):
#         'child of hybrid inheritance: '
    

# d = D()
# d.m1()
# d.m2()
# d.mf()

# method overriding

# it means child class provide its own creation of parent class.
# the same method name is used in both  parent and child class.
# child class method gets priority to execute
# super()  is used to call parent class method for child class. , it help
# to avoid rewriting code .
# it is usefull when  child class wants to extend parent behvaiour 


# multi-level parent ->  employee second  -> manager  last one -> admin

class admin:

    def display(self):
        print("i am the admin")
    def __init__(self):
        print('class admin')

class manager:

    def display(self):
        print('i am a manager')
    def __init__(self):
        print('class manager')

class employee(admin,manager):
    
    def diplay(self):
        # super()
        print('i am employee')
    def __init__(self):
        print('class employee')


e = employee()
e.diplay()
print(employee.mro())


#Is-A realtiinship and Has-A relationship

# it is realtionship  defines inheritance.
# one class is a specialized form of another class
# child class is a type of parent class
# meaning sing inheritance B(A): B class Is-A A class

#Has-A realtionship
# it means one class contains object of another class
# it is achived using composition and aggregation
# one object uses another object as a member
# meaning: B Has-A A 


#ex
# car has-A engine
# employee has_a address


