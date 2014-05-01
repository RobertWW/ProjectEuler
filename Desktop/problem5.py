sum = 0
sumsquare = 0
for x in range(101):
	sumsquare += x**2
for i in range(101):
	sum +=i
sum = sum**2
print (sum - sumsquare)