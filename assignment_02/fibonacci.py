num = int(input("enter the n value :"))
num = num-2
a = 0
b = 1
print(a,b,end=" ")
c = 0
while num > 0:
    c = a + b
    print(c,end=" ")
    a = b
    b = c
    num-=1

num = int(input("enter the n value :"))
a = 0
b = 1
print(a,b,end=" ")

for i in range(2,num):
     c = a + b
     print(c,end=" ")
     a = b
     b = c
      