count = 1

def pow(x, y):
	return x**y

for x in range(2, 10):
	num = 1
	lenPow = len(str(pow(x, num)))
	while num <= lenPow:
		if lenPow == num:
			count += 1
			print str(x) + ":::" + str(num)
		num += 1
		lenPow = len(str(pow(x, num)))

print count
