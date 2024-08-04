# This is the solution to ProjectEuler 7.

# https://projecteuler.net/problem=7

import math

# generate the first x primes
def primeGen(amountOfPrimes):
	# start the prime list
	primeList = [2, 3, 5, 7]
	prime = 9
	while len(primeList) < amountOfPrimes:
		# we know that no primes other then 2 can be even so we can add 2 every time
		prime += 2
		isPrime = True
		# get the sqrt of the number we are testing, we don't need to test any numbers higher then the sqrt of the number
		sqrt = math.sqrt(prime)
		for testPrime in primeList:
			# if we can divide the number by any lower prime the number is not a prime
			if prime % testPrime == 0:
				isPrime = False
				break
			# we only have to test up to the sqrt of the number, if it is bigger break out, the number is a prime
			if testPrime > sqrt:
				break
		# if the number couldn't be divided by any other prime it is a prime
		if isPrime:
			# add the number to the list of primes
			primeList.append(prime)

	# return the list of all primes
	return primeList


# get a list of the 10001 first primes
PrimeList = primeGen(10001)
# print the 10000 object in the list. It starts with 0 so it is the 10001:th prime
print (PrimeList[10000])
