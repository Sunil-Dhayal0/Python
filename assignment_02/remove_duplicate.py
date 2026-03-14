#remove duplicate
list_1 = input("enter the numbers seprate by space: ")

list_1 = [int(x) for x in list_1.split()]

unique_list = []

for num in list_1:
    if num not in unique_list:
        unique_list.append(num)

print(f"unique list is:  {unique_list}")
