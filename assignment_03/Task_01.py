# 1. Bank Account System
# Design a class BankAccount with the following specifications:
#  Private attributes:
# o accountNumber
# o balance
#  Public methods:
# o deposit(amount)
# o withdraw(amount)
# o getBalance()
# Requirements:
#  The balance should not be directly accessible from outside the class.
#  Withdrawal should not allow the balance to become negative.
#  Deposit should reject negative values.
# Tasks:
# 1. Implement the BankAccount class.
# 2. Demonstrate its usage with appropriate inputs.
# 3. Explain how encapsulation is achieved in your implementation

class BankAccount:
    def __init__(self,accountNumber,balance):
        self.__accountNumber = accountNumber
        self.__balance      = balance
        ## public
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
        else:
            print("invalid input")
    def withdraw(self,amount):
        if self.__balance > amount:
            self.__balance-=amount
        else:
            print("insuffient balance")
    def getBalance(self):
        return self.__balance
    
user1 = BankAccount(1201203,50000)

print(f"the balance of bankaccount is {user1.getBalance()} ")
user1.withdraw(500)
print(f"the balance of bankaccount is {user1.getBalance()} ")
user1.deposit(700)
print(f"the balance of bankaccount is {user1.getBalance()} ")
user1.deposit(-700)
print(f"the balance of bankaccount is {user1.getBalance()} ")