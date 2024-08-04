maxN = 0
for i in range(300, 1000): # 300 because we know the result is going to be large.
	for j in range(300, 1000):
		product = i * j
		if product > maxN and product == int(str(product)[::-1]):
			maxN = product
print(maxN)
