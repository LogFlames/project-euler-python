k = 0
n = 1
count = 0
while len(str(n)) != 1000:
	count += 1
	n = n + k
	k = n - k

print(count)
