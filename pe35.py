from os import path

primes = []
isPrime = []
for n in range(1000000):
    isPrime.append(0)

code_path = path.dirname(__file__)

with open(path.join(code_path, "external_files/pe35_primes.txt"), "r") as f:
    for line in f:
        primes.append(int(line))
        isPrime[int(line)] = 1

def getBiggestAndSmallestFromList(list_):
    biggest = int(list_[0])
    smallest = int(list_[0])
    for num in list_:
        num = int(num)
        if num > biggest:
            biggest = num
        if num < smallest:
            smallest = num
    return biggest, smallest

class listObject():
    def __init__(self, list_):
        self.list_ = list_
        if len(list_) > 0:
            self.biggest, self.smallest = getBiggestAndSmallestFromList(list_)

    def getObjectAt(self, index):
        return self.list_[index]

    def getBiggest(self):
        return self.biggest

    def getSmallest(self):
        return self.smallest

    def isInRange(self, x):
        x = int(x)
        if x >= self.smallest and x <= self.biggest:
            return True
        return False

    def addObject(self, x):
        if len(self.list_) >= 1250:
            return False
        self.list_.append(x)
        return True

    def recalcBigAndSmall(self):
        self.biggest, self.smallest = getBiggestAndSmallestFromList(self.list_)

    def isIn(self, a):
        if a in self.list_:
            return True
        return False

def circleOnce(intToCircle):
    intToCircle = str(intToCircle)
    firstString = intToCircle[0]
    intToCircle = intToCircle[1::]
    intToCircle += firstString
    return intToCircle

index = 0
count = 0

primeDivider = []

primeDivider.append(listObject([]))

for n in range(len(primes)):
    primes[n] = str(primes[n])

    if primeDivider[len(primeDivider) - 1].addObject(primes[n]):
        pass # everything is fine
    else:
        primeDivider.append(listObject([]))
        primeDivider[len(primeDivider) - 1].addObject(primes[n])
        primeDivider[len(primeDivider) - 2].recalcBigAndSmall()

primeDivider[len(primeDivider) - 1].recalcBigAndSmall()

def isInPrimes(prime_, useLongIsPrimeList):
    if useLongIsPrimeList:
        if isPrime[int(prime_)] == 1:
            return True
        return False


    if prime_ > primes[len(primes) - 1]:
        # print("Bigger then biggest object " + str(prime_) + " / " + str(primes[len(primes) - 1]))
        return False
    for smallList in primeDivider:
        if smallList.isInRange(prime_):
            if smallList.isIn(prime_):
                return True
            return False
    return False

circularPrimes = []

for prime in primes:
    index += 1
    if index % 10000 == 0:
        print(str(index) + " / " + str(len(primes)))
    editPrime = prime
    editPrime = circleOnce(editPrime)
    if not isInPrimes(editPrime, True):
        continue
    quit = False
    while editPrime != prime:
        editPrime = circleOnce(editPrime)
        if not isInPrimes(editPrime, True):
            quit = True
            break
    if quit:
        continue
    count += 1
    circularPrimes.append(prime)

print(count)
print(circularPrimes)
