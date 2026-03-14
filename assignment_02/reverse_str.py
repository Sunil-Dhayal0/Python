#reverse str
inp_str = input("enter the string want to reverse: ")
reversed_str = ''

for char in inp_str:
    reversed_str = char + reversed_str

print(f"reverse str is: {reversed_str}")   

reversed_str = reversed_str[::-1]
print(reversed_str)