import math

primes = [2, 3, 5]

def getPrimesReplace(size):
    allNumbers = []
    #primes = []
    global primes

    primes = []

    for n in range(2, size):
        allNumbers.append(n)

    for n in range(len(allNumbers)):
        if allNumbers[n] == -1:
            continue

        primes.append(allNumbers[n])
        for j in range(allNumbers[n] ** 2 - 2, len(allNumbers), allNumbers[n]):
            allNumbers[j] = -1

    return primes

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

def isPrime(num):
    rootOfNum = math.sqrt(num)
    for n in getPrimesReplace(rootOfNum):
        if num % n == 0:
            return False
    return True

def getListOfZeroes(num):
    isAnyZeroes = False
    list_ = []
    for n in str(num):
        if n == "0":
            list_.append(1)
            isAnyZeroes = True
        else:
            list_.append(0)

    return list_, isAnyZeroes

def copyList(originalList):
    returnList = []
    for n in range(len(originalList)):
        returnList.append(originalList[n])

    return returnList

def getBinary(bit):
    binary = []
    for n in range(bit):
        binary.append(0)

    for n in range(1, 2 ** bit):
        binary[0] += 1
        index = 0
        while binary[index] == 2:
            binary[index] = 0
            index += 1
            binary[index] += 1
        yield binary
        

def buildInt(list_):
    buildTo = ""
    for n in list_:
        buildTo += str(n)

    return int(buildTo)

def replaceDigits(list_, digit, number):
    number = list(str(number))
    if len(list_) != len(number):
        print("The length of the list must be the same as on the number given to the replaceDigits function!")
        return

    for n in range(len(list_)):
        if list_[n] == 1:
            number[n] = digit

    return buildInt(number)

guessValue = 100000
while True:
    for prime in getPrimesReplace(guessValue):
        #n, test = getListOfZeroes(prime)
        #if not test:
        #    continue
        # we know the is at least one with all the zeroes
        for n in getBinary(len(str(prime))):
            count = 0
            for nn in range(0, 10):
                # test if there is enough numbers from 1 -> 10 to reach 8?
                if (9 - nn) >= (8 - count):
                    break
                if isPrime(replaceDigits(n, nn, prime)):
                    count = 9
                    break

        if count == 8:
            print(prime)
            exit()
    guessValue *= 10
