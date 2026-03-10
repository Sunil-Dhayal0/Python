print('sunil')   # string datatype
print(4.5)       # float datatype
print(2+3j)      # complex datatype
print([2,3,1,5]) # list -> c -> array
print((2,6,7,1)) # tuple
print({2,4,1,5}) # sets
print({'name':'sunil','surname':'jaat'}) # dictionary

print(type({'name':'sunil','surname':'jaat'}))
print(type({2,3,4}))
print(type(2+3j))
print(type(4))


## dynamic typing in python very important for interview

#Ans# python is dynamic typing language it automatically detect the data type using the value of variable
#where as java and c++ support static typing

##static and dynamic binding very important

#Ans# in python we can change the value of variable with different data type value where as in c++ there is typeconversion
# eg. if we initialize a variable with int and furture we can assign float value also

a,b,c = 3,4,5
print(a,b,c)

#keywords -> print is keyword and identifiers -> a is identifier and function name if we give name to function also identifier

#user input -> static vs dynamic


# input in python
# input data store in string formate because string is universal data formate

# fnum = input('enter the value of first number')
# snum = input('enter the value of second number')

# sum = fnum+snum
# print(type(snum),sum)


## type conversion -> implicit and explicit

print(str(4))  ## int -> string conversion

print(int(3.456))  ## float -> int conversion that is explicit conversion

print(int("4")+5) ## explicit
print(3.6+2)      ## implicit


## literals
a = 0b10 # binary literals
b = 1000 # decimal literals
c = 0o10 # octal literals
d = 0x1c # hexadecimal literals

print(a)      # gives output in decimal formate
print(b)

#Exponential form (Scientific notation)
float1  =  1.5e2 # float literals -> 1.5e2 = 1.5*10^2
float2 =  1.5e-2 # 1.5*10^-2

print(float1,float2)

# complex literals
x = 3.14j
print(x.real,x.imag)

########## binary conversion functions

#bin() -> for binary
a  = 0b101
print(bin(a))

#oct() -> for octal
print(oct(a))

#hex()
print(hex(a))

#binary to octal
print(oct(a))

#############-------boolean : bool

# true = 1 false = 0
a = True
print(type(a))
print(type(a + a))

print(True+True)

a = 0
print(type(a)) ## o/p  -> 0


########----------- string : str type represent textual data
# A string which is a sequence of characters enclosed in qutoes
# its use both case that is 1. "A" and 2. 'A'

ex1 = 'cdac'             # '' and "" allowed in single line only 
ex2 = "kharghar"

print(type(ex1))
print(type(ex2))

# below is applicable

s1 =  '''cdac -
mumbai'''                   # """""" and '''''' this can write in multiple lines

s2 = """"
 cdac- kharghar
"""
#string indexing:

# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  c   d  a  c  k  h  a  r  g  h
#  0   1  2  3  4  5  6  7  8  9

# accessing character

print(s1[-4])

#string slicing:
#string[start:end]  -> end =  end-1 here

s = "cdacmumbai-1"
print(s[1:4])
print(s[:4])
print(s[1:])
print(s[:])

print(s*3)
print(len(s))

####################------------------  Type casting  
# int to float,complex,bool and 

r = 4
nr = float(r)
print(nr)
nr1 = complex(r)
nr2 = bool(r)
print(nr1,nr2)
print(complex(True))
### value error because string to complex  ->   print(complex("sunil"))