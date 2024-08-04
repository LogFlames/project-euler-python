def commonTerm(a, b):
    commonTerms = []
    commonTermsInSamePos = []

    a_ = []
    for n in str(a):
        a_.append(n)

    index = -1
    for n in str(b):
        index += 1
        if n in a_:
            commonTerms.append(n)
            if a_[index] == n:
                commonTermsInSamePos.append(n)

    return [commonTerms, commonTermsInSamePos]

def findAndRemove(mainStr, removeStr):
    returnStr = ""
    for n in mainStr:
        if n != removeStr:
            returnStr += n

    return returnStr

numerator = 1
denumerator = 1

for a in range(10, 100):
    saveA = a
    for b in range(saveA, 100):
        a = saveA
        aOverB = float(a) / float(b)
        if aOverB:
            c_t = commonTerm(a, b)
            if len(c_t[1]) > 0:
                continue
            elif len(c_t[0]) > 0:
                if (len(c_t[0]) == 2):
                    continue
                a = int(findAndRemove(str(a), str(c_t[0][0])))
                b = int(findAndRemove(str(b), str(c_t[0][0])))
                if b == 0:
                    continue
                if float(a) / float(b) == aOverB:
                    numerator *= float(a)
                    denumerator *= float(b)

for n in range(2, int(denumerator / 2) + 1):
    if numerator % n == 0 and denumerator % n == 0:
        numerator /= n
        denumerator /= n

print(denumerator)
