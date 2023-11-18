print('Input three numbers and display number that is largest')
number1 = int(input("enter number:"))
number2 = int(input("enter number:"))
number3 = int(input("enter number:"))
if number1 > number2 and number3:
	print("The largest number:",number1 )
if number2 > number1 and number3 :
	print("The largest number:",number2)
if number3 > number2 and number1 :
	print("The largest number:", number3)
