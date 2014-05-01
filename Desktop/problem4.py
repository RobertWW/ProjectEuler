def isDivisible(x):
	notDivisible = True
	while (notDivisible):
		if (divise(x)):
			notDivisible = False
			print "HURRAY"
		else:
			x = x + 1
			print ("Current value of x: ", x)
	print x


def divise(integer):
	count = 1
	while (count <= 20):
		if (integer%count != 0):
			#print ("This is considered False and the count is:" ,count)
			return False
			break
		else:
			count = count + 1
			#print ("This is considered True")
	return True
isDivisible(20)