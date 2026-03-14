# second_largest_num


i_list = input("enter the list num sep by : ")

i_list = [int(x) for x in i_list.split()]

unique_list = []

for i in i_list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)

n = len(unique_list)

for i in range(0,n):
    for j in range(0,n-i-1):
        if unique_list[j] > unique_list[j+1]:
            temp    =   unique_list[j]
            unique_list[j] = unique_list[j+1]
            unique_list[j+1] = temp


print(f"sorted list is : {unique_list}")
print(f"second largest number is {unique_list[-2]}")