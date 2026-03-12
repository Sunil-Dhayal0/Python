
##########-----------bitwise operator
# 1. & -> and ,2.  ~ -> or , 3. <<  -> left shift . 4.>> -> right shift 5. ^ -> xor

print(2 << 2)     # 01 <<2 = 0100   left shift
print(2 >> 2)     # 01 >>2  = 0000  right shift

#print(2 ` 3)  : syntax error : invalid syntax
#print(a++)    : syntax error : invalid syntax

#########----------- mebership operator
## in and not in

print('i' in 'sunil')      # it is case sensetive also
print('i' not in 'sunil')
nums = [10,20,30,40]
print("10 is in nums: ",10 in nums)
print("60 is in nums: ",60 in nums)

#######----------------identity operators
# is    : same object  in  memory
# is not : different object

a = [10,20]
b = [10,20]

print("is same object :",b is a)
print("is not same object",a is not b)
 

####------------------ arithmetic operators

# num1 = int(input('enter the value of number'))
# d1 = num1%10

# num1 = num1/10
# d2 = int(num1%10)

# num1 = num1/10
# d3 = int(num1%10)

# sum = d1+d2+d3
# print(sum)

#########---------- comparison operators similar to the  relational operator

a,b = 10,20
print(a==b)
print(b<a)


#########-------------- logical operator

age = 20
id = True
print(id and age > 20)

day = 22

match day:
     case 1:
          print("monday")
     case 2:
          print("tuesday")
     case 3:
          print("wednesday")
     case 4:
          print("thrusday")
     case 5:
          print("friday")                   
     case _:
          print("No day")      


#############------for loop

#for variable_name in sequence:
# statements

num = [10,20,30,40]

for n in num:
      print(n,end=" ")

for n in "cdac":
      print(n,end=" ")

for n in "c","d","a","c":
     print(n,end=" ")

#########-----------range():
print()
# start: default 0
# stop : excluded
# stop : 1


for n in range(5,150,5):           
     print(n,end=" ")


##########--------while statement
print()

i = 0
while i < 5:
     print(i,end=" ")
     i+=1


##########-------------List     
# it is built-in datatype used to store multiple values in a single variable
# - is ordered
# - is mutable
# - allows duplicate values
# - can store different data types
# - can support indexing and slicing

list = [10,20,30,40,50]
#oredered
print(list)

#mutable
list[0] = 11
print(list)

#duplicate
list = [10,10,20,10]
print(list)

#different datatype
list = [10,2.99,"Cdac",True,None]
print(list)

#empty list is allowed
a = []
print(a)

#slicing
list = [10,20.45,304,4067]
print(list[1:4])            # end is 4-1
print(list[:-1])            # end-1 se start hoga
print(list[::-1])           # start 10 .... end 4067

#insert method

list.insert(1,True)
print(list)

#exdent
list.extend("""sunil""")
print(list)

#remove  for particular element
list.remove('s')
print(list)

# for remove last element
list.pop()
print(list)

# for particular index element delete
del list[1]
print(list)

# change
list[1] = 22
print(list)

#length of list
print(len(list))

#count duplicate number
print(list.count(10))         # only one is present in list

#sort the list   -> don't allowed to sort different data type element to sort
lists = [1,5,2,4,3]
sortedList = sorted(lists,reverse=True)
print(sortedList)

# for clear whole elements
list.clear()
print(list)









