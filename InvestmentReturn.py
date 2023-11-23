print("Investment Return")
p = int(1000)
r = 7/100
n = int(input('Enter number of year:'))

a = int(p*(1+r)**n)

print(a,'is the amount on deposit at the end of the nth year')