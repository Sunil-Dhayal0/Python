###----------- Exception handling


# 1.error  -> is a problem that causes the program to behave unexpectedly or stop
#  it can happen 1. before the program run
#                2. while program execute
#                3. it indicate something is wrong in the code or logic
# 2.exception
#                -> is a type of runtime error it occur during program execution
#                 - if exception is not handled, it stops the program.

#  type of error

# 1.syntax error
#  it occur when python rule are voilate

# 2. exception: runtime error
#  this occur after the program started its execution

#    ZeroDivisionError: division by zero
#     ex 5/0 
#    valueError : invalid value
#    ex  x  = int("xxx")
#    typeError : invalid type operation
#    ex  res = "10"+5
#    print(res)
#    indexerror : list index is out of range
#     
#    keyerror   : dictionary key not found
#    fileNotFoundError : file doesn't exist
#    NameError     : variable not found
#    AttributeError : attribute/method not found


# n = 10
# try:
#     print("start------------")
#     res = n/0
#     print("try----------")     ######### this line is not execute because of exception
# except ZeroDivisionError:
#     print("cannot divide by zero")
#     print("except----------")

# print("end-------")



# n = 10
# try:
#     print("start------------")
#     num = int(input("enter index "))
#     list = [10,202,30]
#     print(list[num])
#     print("try----------")                ######### this line willn't execute if exception there
# except ValueError:
#     print("cannot divide by zero")
#     print("except----------")

# except IndexError:
#     print("enter valid index")

# print("end-------")


# ### another way of write multiple exception together 

# try:
#     print("start------------")
#     num = int(input("enter index "))
#     list = [10,202,30]
#     print(list[num])
#     print("try----------")     ######### this line is not execute because of exception
# except (ValueError, IndexError):
#     print("cannot divide by zero")
#     print("except----------")
#     print("enter valid index")

# print("end-------")

############--------Exception class

# try:
#     print("start------------")
#     num = int(input("enter index "))
#     list = [10,202,30]
#     print(list[num])
#     print("try----------")     ######### this line is not execute because of exception
# except Exception as e:
#    print(f"name of exception {e}")

# print("end-------")

#ex--------- another one

# try:
#     n = 100/0
#     print("try")
# except Exception as e:
#        print(f"exception---------{e}")
# else:
#       print("else")
# finally:                                ####------ it always execute
#       print("finally")

#ex------------check----its work answer is yes

# try:
#       n = 100//10
#       print(n," try")

# finally:
#       print("finally")



#ex-------------------nested try and catch

# try:
#     num = int(input("enter the number: "))
#     try:
#         print(100/num)
#     except ZeroDivisionError:
#         print("zero division error")
# except Exception as e:
#     print(f"exception is -------{e}")
# finally:
#     print("finally")


###---------- raise is used to throw an exception manually

# age = -11
# if age < 0:
#     raise ValueError("employee age can't be negavtive")
#     print("age is invaild")


####---------exception chaining
# when one exception is raised whil handling another exception.
#  it helps to preserve the original error context.
#  it can be implemented using keyword:
#  it used to show the root cause of the error
# it also improves the debugging clarity which helps in tracking error flow.


# try:
#     x = int("abc")
#     print(x)
# except ValueError as e:
#     raise TypeError("conversion is not correct") from e


# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as e:
#         raise ValueError("cannot divide by zero, aise kon krta h ! ")

# divide(10,0)

# def divide(a,b):
#     try:
#         return a/b
#     except Exception as e:
#         raise print(e)

# divide(10,0)


class insuffientBalanceError(Exception):
    pass

def withdraw(balance,amount):
    if amount > balance:
        raise insuffientBalanceError("not sufficient balance......")
    
    return balance-amount

try:
    balance = withdraw(3000,5000)
except insuffientBalanceError as e:
    print("custom exception is defined......................",e)