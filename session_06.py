############--------function

def add(a,b):
    return a+b

print(add(1,2))

##Types: of arguments:
#1. positional argument
#2. keyword argument
#3. default argument
#4. variable length argument 

########--- positional arg

def sub(a,b):
    return a- b

print(sub(10,5))
print(sub(5,10))

############------ keyword argu

def sub(a,b):
    print(a-b)
sub(a = 10 , b = 20)
sub(a = 20 , b = 10)

############----default argu

def greet(name = "Test"):
    print("hi",name)

greet("sunil")
greet()

##########------variable length argu
# - used when the number of arguments is not know in advanced 


def sum(*n):
    s = 0
    for i in n:
        print(i,end=" ")
        s+=i
    print(s)
sum(10,20,30,40)

#####---------return statement:
#-return used to send a value back from the function
#-return one single value
#- return multiple value

def calc(a,b):
    return a+b , a-b, a*b
x,y,z = calc(2,3)
print(x,y,z)

#Recursive function:
# - function that call itself
# - every recursive function must have base condition


#############---------lambda function:
#-it is a small anonymous function it may not have any name
#-generally it is written in one line

#lambda arguments: expression

sq = lambda n: n*n
print(sq)