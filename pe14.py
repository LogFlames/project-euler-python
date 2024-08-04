maxCount = (0, 0)
counted = [0]

for n in range(1,1000000):
	saveN = n
	count = 0
	if n % 100000 == 0:
		print n
	while n != 1:
		if(n % 2 > 0):
			n = 3 * n + 1
			count += 1
		if(n % 2 == 0):
			n = n / 2
			count += 1
		if n < saveN:
			count += counted[n]
			n = 1
	if(count > maxCount[0]):
		maxCount = (count, saveN)
	counted.append(count)
print maxCount
