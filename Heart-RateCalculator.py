print('Heart-Rate Calculator')
age = int(input())
maxheartrate = int(220 - age)
print(maxheartrate,)

minRangefortargetheartrate = 0.50 * maxheartrate
maxRangefortargetheartrate = 0.85 * maxheartrate
if (maxheartrate >= 50 and  maxheartrate <= 85):
	print(f'mim range: {minRangefortargetheartrate}  max range: {maxRangefortargetheartrate}')
