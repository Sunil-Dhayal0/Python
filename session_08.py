# calculate bill for give price with 18% gst and then print the amount

# type of method in oops
#1.instance method: -> they require object creation

#key pointers:
#1. first parameter should be 'self
#2. access instance variables
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
# class onlineplatform:
#     user = 0
#     name = 'Udemy'

#     def __init__(self,uname):
#         self.name = uname
#         onlineplatform.user+=1
#     @classmethod
#     def count(cls):
#         print("count of udemy users:", cls.user)  #cls keyword not a self keyword
        
# u1 = onlineplatform("ravi")
# u2 = onlineplatform("sunil")
# u3 = onlineplatform("rohit")

# onlineplatform.count()

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



# class test:
  
#    @staticmethod
#    def cal(a,b):
#        return a+b
   
# print('static method',test.cal(2,3))

# calculate the area of cone using static method
# v = 1/3*pi*r*r*h

# class area:

#     pi = 3.14

#     @staticmethod
#     def area_of_cone(r,h):
#       return 1/3*area.pi*r*r*h
    
# print('area of cone',area.area_of_cone(2,6))

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


# from abc import ABC, abstractmethod   # ABC -> abstract base classs

# class A(ABC):
#     def m1(self):                          # declaration of method that is ## abstract method
#         pass
#     def m2(self):
#         print('normal method in abstract class is allowed')
# class B(A):
#     def m1(self):                           # implementation of method
#         print('m1(): implemented in child class that is class B')  
# # abstract method: - an abstract method is a method that is declared but not implemented in the abstract class.
# #                    child classes must override and implement this method

# a  = A()   # can't use a method of abstract class function
# a.m1()
# a.m2()
# b = B()
# b.m1()
# b.m2()

#######---example
#------miss something important


####---example:-  

# from abc import ABC,abstractmethod

# class shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def display(self):
#         pass

# class rectangle(shape):

#     def area(self):
#         print("area of rectangle")
#     def display(self):
#         print(" rectangle")

# r = rectangle()
# r.area()
# r.display()


##---- another important example
# we can define constructor in abstract class

# from abc import ABC,abstractmethod

# class A(ABC):
#     @abstractmethod
#     def m1(self):
#         print('m1(): abstract method')

# class B(A):
#     def m1(self):
#         super().m1()                 ## execute parent class method as well as child also if child method have task
#         print("m1() : implement and execute in child class")

# a  = B()

# a.m1()

##-------example use of controller
# from abc import ABC,abstractmethod
# class A(ABC):
#     @property
#     @abstractmethod
#     def m1(self):
#         pass

# class B(A):
#     @property
#     def m1(self):
#         return 'm1(): child class implementation'
    
# a = B()
# print(a.m1)              # there is no need of parenthesis


#####--------classmethod
# from abc import ABC,abstractmethod
# class A(ABC):
#     @classmethod
#     @abstractmethod
#     def m1(self):
#         pass

# class B(A):
#     @classmethod
#     def m1(cls):
#         return 'example of classmethod m1(): child class implementation'
    
# a = B()
# print(a.m1())             

#########------- static method

from abc import ABC,abstractmethod
class A(ABC):
    @staticmethod
    @abstractmethod
    def m1():
        pass

class B(A):
    @staticmethod
    def m1():
        return 'example of static method m1(): child class implementation'
    
a = B()  # throw error because 
a.m1()
print(B.m1())             

# abstract class key pointers:
#- ABC is used to create abstract base class
#-@abstrcatmethod is used to declare absrtract method
# abstract class object can't be created
#-chlid class must implement all abrstrcat methods
# abstract 
# 
#
#Application:

from abc import ABC,abstractmethod
# vehicle abstract class,
#       -method start()
#       -method stop()
#     child class motorbike

# class vehicle(ABC):
      
#        @abstractmethod
#        def start(self):
#            print('start')
#        def stop(self):
#            print('stop')

# class moterbike(vehicle):
#     def start(self):
#         return super().start()
#     def stop(self):
#         return super().stop()

# m1 = moterbike()

# m1.start()


#interview important -> difference between normal vs abstract class

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



class employee:

    def __init__(self,name,salary):
        self.__name = name               # name and sal become private by write '__'
        self.__sal = salary

# getter method: read data
    def get_sal(self):
        return self.__sal
    def set_sal(self,amount):
        self.__sal = amount

    def display(self):
        print(self.__name)
        print(self.__sal)


emp = employee('sunil',10002000)

emp.display()

#emp.__sal                #AttributeError: 'employee' object has no attribute '__sal'

# using of getter and setter

emp.set_sal(200)
update_sal = emp.get_sal()
print(f'updated salary is {update_sal}')


#######--------------- decorator


########--------@property
# it is  a python decorator used to convert a method into a read-only attribute
# it allows a method to be accessed like a variable instead of a function.
# it is commanly used in encaps.. to accesss private variable safely

#key pointer:
#1. allow method access without parenthesis.
#2. it works with private variables(__sal)
#3. it work together with
#        @property -----------> getter
#        @property_name.setter -----> setter
#        @propertey_name.delete

class employee:

    def __init__(self,name,salary):
        self.__name = name               # name and sal become private by write '__'
        self.__sal = salary

# getter method: read data

    @property
    def salary(self):
        return self.__sal

    @salary.setter
    def salary(self,amount):
        self.__sal = amount
    
    # @salary.getter
    # def salary(self,amount):
    #      return self.__sal

    def display(self):
        print(self.__name)
        print(self.__sal)


emp = employee('sunil',10002000)

emp.display()

#emp.__sal                #AttributeError: 'employee' object has no attribute '__sal'

# using of getter and setter of decorator

emp.salary
emp.salary = 1234
print(emp.salary)


