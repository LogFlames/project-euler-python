primesHuge = [False, False, True, True, False, True, False, True, False, False]
primes = [2, 3, 5, 7]

def isPrime(x):
    if x > len(primesHuge):
        num = len(primesHuge) - 1
        while len(primesHuge) - 1 < x:
            primesHuge.append(False)
            num += 2
            numIsPrime = True
            for n in primes:
                if num % n == 0:
                    numIsPrime = False
                    break
            if numIsPrime:
                primes.append(num)
                primesHuge.append(True)
            else:
                primesHuge.append(False)

    return primesHuge[x]

def isTruncatable(x):
    if not isPrime(x):
        return False
    saveX = x
    while len(str(x)) > 0:
        xStr = str(x)[:-1]
        if xStr == "":
            break
        else:
            x = int(xStr)
        if not isPrime(x):
            return False

    x = saveX

    while len(str(x)) > 0:
        xStr = str(x)[1:]
        if xStr == "":
            break
        else:
            x = int(xStr)
        if not isPrime(x):
            return False

    return True

count = 0
num = 9
sum_ = 0
save = []
while count < 11:
    num += 2
    if isTruncatable(num):
        count += 1
        sum_ += num
        save.append(num)

print(sum_)
print(save)
