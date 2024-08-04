import math

primes = [2, 3, 5]

def generateNextPrime():
    global primes
    num = primes[len(primes) - 1]
    isPrime = False
    while not isPrime:
        num += 2
        isPrime = True
        rootOfNum = math.sqrt(num)
        for n in primes:
            if num % n == 0:
                isPrime = False
                break
            if n > rootOfNum:
                break
        if isPrime:
            primes.append(num)
            return num

def getPrimes():
    for n in primes:
        yield n

    while True:
        yield generateNextPrime()

def removeDublets(x):
    newList = []
    for n in x:
        if not n in newList:
            newList.append(n)

    return newList

def haveMoreThenXPrimeFactors(x, primeFactorsEdge):
    primeFactors = []
    while True:
        for prime in getPrimes():
            if x % prime == 0:
                primeFactors.append(prime)
                x /= prime
                break
        primeFactors = removeDublets(primeFactors)
        if len(primeFactors) == primeFactorsEdge:
            return True
        elif x == 1:
            return False

num = 1
while True:
    num += 1
    if num % 10000 == 0:
        print(num)
    if haveMoreThenXPrimeFactors(num, 4):
        if haveMoreThenXPrimeFactors(num + 1, 4):
            if haveMoreThenXPrimeFactors(num + 2, 4):
                if haveMoreThenXPrimeFactors(num + 3, 4):
                    print(num)
                    break
