# calculate bill for give price with 18% gst and then print the amount

# type of method in oops
#1.instance method: -> they require object creation

#key pointers:
#1. first parameter should be 'self
#2. acces instance variables
#3. called using objects

#Note: object created ---> instance method called -> access instance variable

#2.class method :
# class method operates on class variables
# @classmethod : decorator  # a notation

#key pointer:
#1.first parameter is 'cls'
#2.used to modify class variable
#3.called using class name
@classmethod
def m1(cls):
    print("hello")

#Ex udemy online plateform application:
#- class variable
#- constructor
# - 1 static method / class method
# - multiple object 


## access class variable outside the class using cls keyword and class method
class onlineplatform:
    user = 0
    name = 'Udemy'

    def __init__(self,uname):
        self.name = uname
        onlineplatform.user+=1
    @classmethod
    def count(cls):
        print("count of udemy users:", cls.user)  #cls keyword not a self keyword
        
u1 = onlineplatform("ravi")
u2 = onlineplatform("sunil")
u3 = onlineplatform("rohit")

onlineplatform.count()

#3.static method

#- it don't use instance variable or class variables.
#- they behave like normal function placed insed the class
#- key pointer:
#--------
#1.@staticmethod
#2. no self
#3. no cls
#4. used for utility functions
#5. independent to use class and instance variable

#ex.

class test:
  
   @staticmethod
   def cal(a,b):
       return a+b
   
print('static method',test.cal(2,3))

# calculate the area of cone using static method
# v = 1/3*pi*r*r*h

class area:

    pi = 3.14

    @staticmethod
    def area_of_cone(r,h):
      return 1/3*area.pi*r*r*h
    
print('area of cone',area.area_of_cone(2,6))

#HW----- library management------
# create an application for library management system using interface, static/class and local variable. also
# use instance method, class method , static method.

# OOPS pillars:
#1. abstraction
#2. encapsulation
#3. inheritance
#4. polymorphism

# modular programming , flexiblity, code reusability , data protection

#1. hiding internal implementation details and showing only essentail functionality to the user

# abstract class:
# an abstract class is a class that cannot be instantiated(cannot create object)
# and is used as a blueprint for other classes.
# abstraction contains:
#   - abstract method
#   - normal method
#   - variables

#-Abstract classes ensures that child classes implements certain required methods.
#1. defined using ABC(abstract base class) module
#2. must inheritance from ABC
#3. may not contain abstract method
#4. 
#5. child class must implement abstract method


from abc import ABC, abstractclassmethod

class classname(ABC):
    pass


# abstract method: - an abstract method is a method that is declared but not implemented in the abstract class.
# child classes must override and implement this method

@abstractclassmethod
def abstractmethod_name(self):
    pass


##########---------- encapsulation:
#- Binding data (variables) and methods(function) together into a single unit.
 
 #key pointer:
 #---------
 #1. protecting sensetive data
 #2. prevent accidential function
 #3. control access of variables using method
 #4. improve the maintainability

 # Access specifiers: : use in with in the classess
 #1. private variable:()
 #ex. _accno,_bal
 #2. protected variable(_var) : use in child classess
 #ex bal,speed,pi
 #3. public variable(var) : use anywhere

 #rules to implement encapsulation:
 #----------------------
 # sensetive data should be private
 # access direct modification of important variables.
