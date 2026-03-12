# s = {"amit":80,"sneha":60}

# print(s.get('sneha'))
# s["anil"] = 60
# print(s)
# print(s['anil'])

# s["anil"] = 100

# print("update value ",s)

# newitem = {'sunil':100}
# s.update(newitem)
# print(s)

# s.pop('amit')
# print(s)


# for i in s:
#     print(i,s[i])

#search


#higest marks

# highest = max(s,key=s.get)

# adding element with duplicate

# n = [12,3,4,6,7,8,92,3,4]

# list = []

# for num in n:
#       if num is not in list:
#         list.append(num)
    
# print(list)    

#reverse element of list with using reverse

# sum = 0

# for num in n:
#      sum+=num

# print(sum)     

# second largest number in list
# n.sort()

# listn = [-1,-2,-3,0,0,0,1,2,3,4]

# list0 = []
# listP = []
# listne = []

# for num in listn:
#      if num < 0:
#           listne.append(num)
#      elif num > 0:
#          listP.append(num)
#      else:
#           list0.append(num)
# print(list0,listP,listne)


###merge to sorted list

# a  = [1,3,5,7,8]
# b  = [2,6,9]

# merge = []
# i = j = 0
# while i < len(a) or j < len(b):
#           if  a[i] < b[j]:
#               merge.append(a[i])  
#               i+=1
#           else:
#                  merge.append(b[j])
#                  j+=1    

# print(merge)


s = {10,20,30,40,50}
print(s)