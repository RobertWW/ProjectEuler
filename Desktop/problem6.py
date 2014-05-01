triples = [[1,2,3]]
a = 0
b = 1
c = 2
for a in range(1000):
	a += 1
	print a
	for b in range(1000):
		b += 1
		for c in range(1000):
			if (a + b + c == 1000 and (a < b) and (b < c) and (a**2 + b**2 == c**2)):
				triples.append([a,b,c])
				break
			else:
				c+= 1
print triples