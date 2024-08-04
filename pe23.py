abundantList = []
sum_ = 0

for n in range(28123):
	if n % 1000 == 0:
		print n
	divi = []
	for k in range(1, (n / 2) + 1):
		if n % k == 0:
			divi.append(n)
	if sum(divi) > n:
		abundantList.append(n)

for n in range(28123):
	notSum = True
	for a in abundantList:
		if a > n:
			break
		if n - a in abundantList:
			notSum = False
			break
	if notSum:
		sum_ += n

print sum_
