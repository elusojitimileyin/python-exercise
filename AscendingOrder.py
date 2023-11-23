print('Ascending Order')
num1 =int(input("enter num1 digit:"))
num2 =int(input("enter num2 digit:"))
num3 =int(input("enter num3 digit:"))

if num1 > num2:
    num1, num2 = num2, num1

if num2 > num3:
    num2, num3 = num3, num2

if num1 > num2:
    num1, num2 = num2, num1


print(f"The numbers in ascending order: {num1}, {num2}, {num3}")


