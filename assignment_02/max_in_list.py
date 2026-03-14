#max_in_list

l = input("enter the list seprated by space")

list_num = [int(x) for x in l.split()]

max_num = list_num[0]

for num in list_num:
    if num > max_num:
        max_num = num

print(max_num) 