print('Input three integer')
num1= int(input("enter first integer:"))
num2= int(input("enter second integer:"))
num3= int(input("enter third integer:"))

sum= num1+num2+num3
print(sum)
average= (num1+num2+num3)/3
print(average)
product= num1*num2*num3
print(product)

smallest=int (num1)
largest =int (num1)


if num2<smallest:
	print(smallest, '= num2')
if num3<smallest:
	print(smallest, '= num3')
if num2>largest:
	print(largest, '= num2')
if num3>largest:
	print(largest, '= num3')