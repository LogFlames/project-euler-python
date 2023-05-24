import math

def primeGen(n):
    pot = list(range(3, n + 1, 2))
    primes = [2]

    i = 0
    while 2 * i + 3 < math.sqrt(n):
        if pot[i] != 0:
            primes.append(pot[i])

            j = i + pot[i]
            while j < len(pot):
                pot[j] = 0
                j += pot[i]

        i += 1

    for ii in range(i, len(pot)):
        if pot[ii] != 0:
            primes.append(pot[ii])

    return primes

def checkForLength(x, size):
    pr = primeGen(10 ** x)
    pr = [*filter(lambda p: len(p) == x, map(str, pr))]

    lastDig = {}

    for p in pr:
        if p[-1] not in lastDig:
            lastDig[p[-1]] = []
        lastDig[p[-1]].append(p)

    for ld in lastDig:
        ret = testCandidates(x, [[a,None] for a in lastDig[ld]], x - 2, size)
        if ret is not None:
            return ret

def testCandidates(x, cds, i, size):
    if i == -1:
        if len(cds) == size:
            return cds
        else:
            return

    catego = {}
    for cd in cds:
        if cd[0][i] not in catego:
            catego[cd[0][i]] = []
        catego[cd[0][i]].append(cd)

    for cat in catego:
        ret = testCandidates(x, catego[cat], i - 1, size)
        if ret is not None:
            return ret


    fil = []
    for cd in cds:
        if cd[1] is None:
            cd[1] = cd[0][i]

        if cd[0][i] == cd[1]:
            fil.append(cd)

    ret = testCandidates(x, fil, i - 1, size)
    if ret is not None:
        return ret

def findPrimeFamily(size):
    x = 1
    while True:
        ret = checkForLength(x, size)
        if ret is not None:
            break
        x += 1

    primes = [int(cd[0]) for cd in ret]

    print(primes)
    print(min(primes))
    

findPrimeFamily(8)
