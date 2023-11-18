print("Enter three integers")
number1= int(input("Enter integer:"))
number2= int(input("Enter integer:"))
number3= int(input("Enter integer:"))

if number1 > number2 and number3:
	print("largest is",number1)
if number2 >number1 and number3:
	print("largest is",number2)
if number3> number1 and number2:
	print("largest is",number3)
