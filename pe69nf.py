import math
from multiprocessing import Pool

def generatePrimesSmallerThan(num):
    primes = []

    for n in range(num + 1):
        primes.append(n)

    sqrt_n = math.sqrt(num)

    for n in primes:
        if (n < 2):
            continue
        if (n > sqrt_n):
            break

        if (n != -1):
            jump = n
            m = n + jump

            while (m < len(primes)):
                primes[m] = -1
                m += jump

    actualPrimes = []

    for prime in primes:
        if (prime != -1):
            actualPrimes.append(prime)

    return actualPrimes[2:]

primes = generatePrimesSmallerThan(1000000)
print("Primes done")

def primeFactorisate(num):
    if (num == 0 or num == 1):
        return [num]
    primeFac = []

    for prime in primes:
        while (num % prime == 0):
            num /= prime
            primeFac.append(prime)

    return primeFac

def getAmtOfSmallerRelativePrime(num):
    num_primes = set(primeFactorisate(num))
    numberOfRP = 0
    for a in range(1, num):
        if len(num_primes & set(primeFactorisate(a))) == 0:
            numberOfRP += 1

    return numberOfRP

def getPhiDiv(num):
    amt = getAmtOfSmallerRelativePrime(num)
    if (amt == 0):
        return -1
    return (num, amt, num / amt)

p = Pool(4)

#primeFactorisated = list(p.map(primeFactorisate, range(10000)))
#print("Prime factorisation up til 10000 done")

phiDiv = list(p.map(getPhiDiv, range(3, 1000000, 2)))
print("PhiDiv done")

minValue = -1
minN = 0
n = 2
for val in phiDiv:
    if (val[2] < minValue or minValue == -1):
        minValue = val[2]
        minN = n

    n += 1

print(minN)

