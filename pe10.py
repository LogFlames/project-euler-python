import math

primeList = [2,3,5,7]
prime = 9
while True:
	prime += 2
	while True:
		root = math.sqrt(prime)
		for testDiv in primeList:
			isPrime = True
			if prime % testDiv == 0:
				isPrime = False
				break
			if testDiv > root:
				break
		if isPrime:
			primeList.append(prime)
			print prime
		break
	if prime > 2000000:
		break
print ("prime: " + str(prime))
print sum(primeList)
