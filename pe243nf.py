import math
from os import path

primes = []

code_path = path.dirname(__file__)

with open(path.join(code_path, "external_files/pe243_primes.txt"), "r") as f:
    for line in f:
        primes.append(int(line))

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

def getPrimeFactors(x):
    exit = False
    while not exit:
        for prime in getPrimes():
            if x % prime == 0:
                x /= prime
                yield prime
                break
            if x == 1:
                exit = True
                break

def R(value):
    count = value
    for n in range(1, value):
        if value % n == 0:
            count -= 1
        else:
            for primeFactor in getPrimeFactors(n):
                if value % primeFactor == 0:
                    count -= 1
                    break

    return float(count) / float(value - 1)

smallerThenNumberator = 15499.0
smallerThenDenumberator = 94744.0
smallerThenValue = smallerThenNumberator / smallerThenDenumberator
print("Checking for: " + str(smallerThenNumberator) + " / " + str(smallerThenDenumberator) + " == " + str(smallerThenValue))

d = 1
while True:
    if d % 500 == 0:
        print(d)
    d += 1
    if R(d) < smallerThenValue:
        print("answer: " + str(d))
        break
