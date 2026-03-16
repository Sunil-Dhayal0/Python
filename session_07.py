#########-----  oops

## advantage of use of oops --> need of oops
#1. code reusability:
#      - classes can be reused using inheritance.
#2. modularity
#      - programs can be divided into small parts
#3 secuirty:
#      - data hiding can be implement using encapsulation
#4 easy maintenance:
#      - code became easy to update and management
# 5 flexbility
#      - supports polymorphism
# 6 real-world modeling:
#      - program resemble tha real world objects which provides real time solution.

# interview question why the need of oops  -> 1.override ,2.

## class -> it is a blueprint or template used to create objects
## object -> it represents real-world entity or instance of class


######--------- empty class
class cake:
    pass

######class

# class student :
#     print('hello')
#     def display(self):
#         print("getting display")

# s1 = student()
# s1.display()


# example 

# class employee :
#     pass
# s1 = employee()
# s2 = employee()
# print(s1,s2)


class employee:
     def __init__(self,emp_id):
         self.emp_id = emp_id            # emp_id -> parameter , self.emp_id -> reference variable
     def show(shelf):
         print(shelf.emp_id)
     


emp1 = employee(101)
emp1.show()
# importance of 'shelf' keyword
# shelf : referes  to current object 

#4. used to call other method of same class

class employee:
    def hello(self):
        print('hello every_one')
    
    def display(self):
        self.hello()

emp1 = employee()
emp1.display()

class employee:
    def __init__(self,name):
        self.name = name


# constructor-------  special method invoke automatically when an object of class created
# syntax: __init__()

#-initiaized object varianle
#- assign initial value to object properties.
#- constructor executes when an object is created.

#- default constructor -> automaticallu when object created default value asigned to attribute

class Abc:
    def __init__(self):
        self.name = 'sunil'
        self.last_name = 'dhayal'
    def display(self):
        print('name',self.name)
        print('last_name',self.last_name)
        

ob1 = Abc()
ob1.display()

#--- parameterized constructor
# value passed when object creation
# 
class Abc:
    def __init__(self,name1,last1):
        self.name = name1
        self.last_name = last1
    def display(self):
        print('name',self.name)
        print('last_name',self.last_name)
        

ob1 = Abc('sunil','dhayal')
# obj1 = Abc()  once define parameterized constructor we can't call default constructor
ob1.display()


# Types of variable
#1. instance varibale
#2. static variavle (class variable)

# class employee:
#     company = 'IBM' # static var
#     def __init__():
#         print("obj created")

# e1 = employee()
# e2 = employee()
## company value same for both e1 and e2 

#3. local variable
# variable declare into method accesible into the method only

#instance variable -> it belong to individual object, each object gets its own copy of these variable
# they are defined using 'self' inside the method(inside constructor)

#key pointer:
#1. created when object is created.
#2. stored iinside object memory
#3. access them using 'self' keyword.
#4. different object my have different values.


##########------ create a bank application bankname , balance
# deposite, withdraw,and show balance 
# initialized the default values 
# finnaly display the content with different multiple object

class Bank_management:
    def __init__(self,BankName,DepositAmount):
        self.Bank_Name = BankName
        self.Deposit_Amount = DepositAmount

    def showAmount(self):
        print("amount of bank: ",self.Bank_Name,'is: ',self.Deposit_Amount)

    def withdraw(self,amount):
        if self.Deposit_Amount < amount:
            print('insufficent balance')
        else:
            self.Deposit_Amount -= amount
    def deposit(self,amount):
        self.Deposit_Amount += amount


user1 = Bank_management('SBI',20000)
user1.deposit(20030)
# user1.showAmount()
user1.showAmount()

class employee:
    company = 'IBM' # static var
    def __init__():
        print("obj created")

e1 = employee()
e2 = employee()

## company value same for both e1 and e2 