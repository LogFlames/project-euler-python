def divi(a, b):
    savedRests = []
    savedAnsv = []
    ansver = ""
    rest = 1
    if a % b == 0:
        return a / b
    else:
        while rest != 0:
            rest = a % b
            ansv = (a - rest) / b
            for i in range(len(savedRests)):
                if savedRests[i] == rest and savedAnsv[i] == ansv:
                    return len(list(ansver))-1
            ansver += str(ansv)
            savedRests.append(rest)
            savedAnsv.append(ansv)
            a = rest * 10
        return 0

maxCycle = 0
saveN = None
for n in range(1, 1000):
    n_divi = divi(1, n)
    if n_divi > maxCycle:
        maxCycle = n_divi
        saveN = n
print(saveN)
