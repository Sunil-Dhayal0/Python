########-----------tuple
########---- declare
#empty tuple

t1 = ()
print(t1)

# create a tuple with a single item

t2 = ('hello',)
print(t2)
print(type(t2))

#homo

t2 = (1,2,3,4)
print(t2)

#hetro

t2 = (True,1,4,2,3,"sunil")
print(t2)

#nested tuple

t3 = (1,2,3,(4,5,6))
print(t3)

#using type conversion

t3 = tuple("sunil")
print(t3)

##########-----------indexing and slicing

print(t2[-1])

####--------edit
# t2[2] = 999         #type error  because tuple is immutable 
# print(t2)     

####adding also not allowed

##########--- delete tuple
print(t2)
del t2
#print(t2)        # name error   because t2 is already deleted

##########------operation on tuple

#  + and *

t1 = (1,2,3,4)
t2 = (5,6,7,8)

print(t1+t2)    # combine the element of both tuples
print(t2*3)     # multiply the number of element of tuple and give duplicate elements

# iterate

for i in t1 :
      print(i,end=" ")

print()    
print(t1[2])

##################------tuple functions

#len 
print(len(t1))

#count -> count duplicate
print(t1.count(t1[1]))

#max -> max element of tuple
print(max(t1))

#min -> min element of tuple
print(min(t1))

#sorted
print(sorted(t1,reverse=True))

#index
# print(t1.index(10))                #ValueError: tuple.index(x): x not in tuple

#tuple unpacking
(a,b,c) = (1,2,3)
print(a,b,c)

# value swap
a = 2
b = 3
a,b = b,a
print(a,b)

#tuple unpacking
(a,b,*other) = (1,2,3,4,5)
print(a,b,other)


#zipping tuples
a = (1,2,3,4)
b = (5,6,7,8)
c = zip(a,b)
print(tuple(c))


################
####################
#############################--------Sets

# set is unorder collection of items . every element is unique there is no duplicates and must me immutable(can't be changed).
# however set itself is mutable we can add and remove item from it


#empty set
s = set()                 ##set = {} this one is wrong
print(s)
print(type(s))


#nested set 2D 
# s = {1,2,{3,4}}                ## type error can't use a mutable datatype in set 
# print(s)


#homo and hetro set
s = {"sunil",1,True}              ## true is considered by python as 1 and there is no duplicate allowed in set datatype
print(s)

s2 = {"sunil",1,2,2,(1,2,3)}      ## only immutable datatype element we can put in to the set that is tuple
print(s2)

s1 = {1,2,3}
s2 = {3,1,2}
print(s1==s2)

#access item from set
#print(s1[0])                       # havn't order that's doesn't follow indexing system

for i in s1:
      print(i,end=" ")              # we can access the element by loop


#adding
s1.add(4)
print()

#update -> use for add multiple item in set
# first we have make list of item which we want to add in set
s1.update([6,7,8,9])
print(s1)

#delete -> we can delete the complete set not only element of set
del s2
#print(s2)               # name error -> because s2 is not exist

#dicard  -> delete particular object and set or item of set
s1.discard(4)
print(s1)

#remove  ->   dicard not show key error if item not found but remove show error 
s1.remove(1)
print(s1)

###########------------set operations
s2 = {9,10,11,12,13,14,15}

#Union(|)
uni = s1|s2
print(uni)           # elements of both set without duplicate

#Intersection(&)
int = s1&s2
print(int)

#Difference(-)
print(s1-s2)          # item of s1 that is not present in s2 

#symmetric difference(^)
print(s1^s2)         # item except the common all will be print
 
# set built in functions len/sum/min/max/sorted
print(len(s1))
print(sum(s1))
print(max(s1))
print(min(s1))
print(sorted(s1,reverse=True))

#union / update
print(s1.union(s2))  # same as s1|s2

#update
s1.update(s2)        # union of s1 | s2 is stored in s1
print(s1)

#intersection
s1.intersection(s2)  # same as s1&s2
s1.intersection_update(s2)
print(s1)

#isdisjoint/issubset/issuperset
s1 = {1,2,3,4}
s2 = {5,6,7,8}
print(s1.isdisjoint(s2))          #return true or false
print(s1.issubset(s2))

#copy 
s3 = {5,6,7,8}
s4 = s3.copy()
print(s4)               # but point different address both set
print(id(s3)==id(s4))


############### frozen set---- it is immutable version of set 

#create frozen set
fs  = frozenset((1,2,3))    # we can pass list and tuple

#works -> all read operations on fset
#   we can't perform write operation on fset
# used for 2D set
#  except add dele and update all operation are work example union and etc


# 2D frozenset can exist
fs = frozenset((2,3,4,frozenset((6,7,8))))
print(fs)

# set ,tuple and list comprehensive
list1  = [ i for i in range(1,11) if i > 5]
tuple1 = (i for i in range(1,11) if i < 7)
set1    = {i for i in range(1,20) if i%2 == 0}
print(list1,end=" ")
print(tuple1,end=" ")
print(set1,end=" ")


##################
#######
###################-----------Dictionary
# collection of key value pair ,key item can't we mutable data type, but dictionary is mutable

#create dictionary
#empty dictionary
d = {}
print(d)

#1D
print()
d1 = {'name' : 'sunil','gender':'male'}
print(d1)

#2D 

d2 = {
      'name':'sunil',
      'gender':'male',
      'subject':{
            'dsa':100,
            'math':80
      }
}
print(d2)
#using sequence and dict function

d3 = dict([(1,2),('name','sunil'),('gender','male')])
print(d3)

#access item from dict
print(d2["name"])
print(d2.get("name"))

#adding key-value pair
d2["address"] = "rajasthan"
print(d2)
d2['subject']['english'] = 150
print(d2)

# create dictionary and tuple from 2 differenent list

# keys = ["id","name","gender"]
# values = ["101","sunil","male"]
# d = dict(zip(keys,values))
# t = tuple(zip(keys,values))
# print(d,t)


#remove 
# d2.pop('subject')
# d2.pop()    # it throw typeerror because pop take argument
print(d2)

#popitem
# d2.popitem()
# print(d2)