# . Bank Withdrawal System using User-Defined Exception
# Create a bank account program.
# Requirements:
#  Accept account balance and withdrawal amount.
#  If withdrawal amount is greater than balance, raise a custom exception named 
# InsufficientBalanceError.
#  Display proper message.
#  If withdrawal is valid, show remaining balance.

account_balance = int(input("enter the balance :"))
withdrawal_amount = int(input("enter the amount to withdrawal :"))

try:
    if withdrawal_amount > account_balance:
        raise Exception("insufficent balance")
    account_balance-=withdrawal_amount
    print(f"remaining balance is {account_balance}")
except Exception as e:
    print(f"error is{e}")
