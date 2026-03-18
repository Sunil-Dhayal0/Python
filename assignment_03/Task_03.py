# Q3. Payment System
# Design an abstract class Payment with:
#  Abstract method:
# o pay(amount)
# Create the following subclasses:
#  CreditCardPayment
#  UPIPayment
# Tasks:
# 1. Implement all classes using abstraction.
# 2. Allow the user to choose a payment method.
# 3. Execute payment without exposing internal logic.
# 4. Explain how abstraction is achieved in your design.

from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    @abstractmethod
    def pay(self,amount):
        self.balance-= amount

    def displayBalance(self):
         print(f"show {self.balance}")

class CreditCardPayment(Payment):

    def __init__(self, name, balance):
        super().__init__(name, balance)
    
    def pay(self, amount):
        self.balance-= amount
        super().displayBalance()
    
       
    

user1 = CreditCardPayment("sunil",200)
user1.pay(50)




        
    
    






