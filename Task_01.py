# Product_Items = 7

# Product_price = 200

# Buy_Product = int(input("enter number product_Item you want"))

# if  Buy_Product/Product_Items > 1 and Buy_Product%7 == 0:
#       print("you got 40 persent discount")
#       SellingPrice = (Product_price*40)/100
#       print(SellingPrice)


## Task 

list = [1,"cdac",True,2,4,5,6]
print(list)

#insert
list.insert(10,9)
list.insert(11,9)
list.insert(12,9)
print(list)

#append
list.append([55,66,77])
print(list)

#insert 
list.insert(10,555)
print(list)

#extend
list.extend([100])
print(list)
#pop
list.pop()
print(list)
#length
print(len(list))
#index
print(list.index(9))

#copy 
clist = list.copy
print(clist)

#clear
list.clear()
print(list)