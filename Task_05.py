# Question 2 – Bank Account System
# Create a Python class BankAccount to simulate a basic banking system.

# The class should include:

# A class variable bank_name = "Secure Bank".

# A constructor that initializes:

# account holder name
# balance (default value = 0)
# A method deposit(amount) that:

# adds money to the account if the amount is positive.
# A method withdraw(amount) that:

# withdraws money if the balance is sufficient.
# A method check_balance() that displays:

# account holder name
# bank name
# current balance.
# Application Task
# Create two bank account objects.

# Perform the following operations:

# deposit money
# withdraw money
# Display the final account balance.


class Bank_Account:
        bank_name = "Secure Bank"

        
        def __init__(self,account_holder_name,balance = 0):
                   self.account_holder_name = account_holder_name
                   self.balance             = balance

        def bankName(cls):
              print(f'bank name is{cls.bank_name}')

        def check_balance(self):

             print(f'account holder name is {self.account_holder_name}')
             self.bankName()
             print(f'current balance is {self.balance}')
        
        def deposit_money(self,amount):
             if amount > 0:
               self.balance += amount
             else:
                 print('invalid amount')
        
        def withdraw_money(self,amount):
            if self.balance > amount*2:
                 self.balance-=amount
            else:
             print('insufficent balance')


user1 = Bank_Account("sunil",3000)

user1.check_balance()

user1.deposit_money(5000)
user1.check_balance()
user1.withdraw_money(30)
user1.check_balance()