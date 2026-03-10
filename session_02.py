
##bitwise operator
print(2 << 2)     # 01 <<2 = 0100   left shift
print(2 >> 2)     # 01 >>2  = 0000  right shift


## mebership operator
## in and not in
print('i' in 'sunil')
print('i' not in 'sunil')


num1 = int(input('enter the value of number'))


d1 = num1%10

num1 = num1/10
d2 = int(num1%10)

num1 = num1/10
d3 = int(num1%10)

sum = d1+d2+d3
print(sum)