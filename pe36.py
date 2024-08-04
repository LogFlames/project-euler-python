def dec(x):
	return int(bin(x)[2:])

sum_ = 0
for n in range(1000000):
	if n == int(str(n)[::-1]):
		k = dec(n)
		if k == int(str(k)[::-1]):
			sum_ += n
print sum_
