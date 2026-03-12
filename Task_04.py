#1. combine two lists index-wise
list1 = ["ma","na","i","kh"]
list2 = ["y","me","s","an"]

listoftuple = list(zip(list1,list2))
print(listoftuple)

ans = [[i,j] for(i,j) in listoftuple]
print('problem_01',ans)

#2.add item in 3d list 

list = [10,20,20,[40,50,60,[40,50,80]]]
list[3][3].append(7000)
print(list)

#3.

candy_list = ['5-star','dairy-milk','kitkat']
no_of_item = [2,3,6]

for (i,j) in zip(candy_list,no_of_item):
    print(i,j)

#4. sum list item

list = [2,3,1,2,4,5]
print(list)
# sum = 0
# for i in list:
#       sum+=i
# print(sum)

#5.you have to add numbers which are in list and greater than the current number 

result = []
list = [2,3,1,2,4,5]
for i in list:
     sum = 0
     for j in list:
        if j >= i:
         sum+=j
     result.append(sum) 


print(result)

#6.find list of common unique items from two list . and show in increasing order

num1 = [4,3,2,1,5]
num2 = [6,3,8,2,9]
common = []

for i in num1:
   if i  not in common:
        common.append(i)

print(common)            

#7.Sort a list of alphanumeric strings based on product value of numeric character in it. 
# If in any string there is no numeric character take it's product value as 1.

# data_list = ['1ac21', '23fg', '456', '098d','1','kls']
# product_val = []

# for item in list:
#     product = 1
#     for char in item:
#         if char.isdigit():
#             product = product*int(item)
#     product_val.append(product)  
    

# print(product_val)
# sorted_l = [i[1] for i in sorted(list(zip(product_val,data_list)))]
# product_val(sorted_l)

#8.Split String of list on K character.

l = ['CampusX is a channel', 'for data-science', 'aspirants.']

inp = ' '
result = []
for i in l:
    print(i.split(inp))
    result.extend(i.split(inp))
print(result)