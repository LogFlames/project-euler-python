import math

primes = [2]

def isPrime(prime):
    for n in primes:
        if prime % n == 0:
            return False
    return True

index = 3
prime_index = 0
found = False
while True:
    if isPrime(index):
        primes.append(index)
        prime_index += 1
        index += 2
    else:
        countdownIndex = prime_index
        currentSquare = 1
        while countdownIndex > 0:
            diff = index - primes[countdownIndex] - 2 * currentSquare ** 2
            if diff > 0:
                currentSquare += 1
            elif diff == 0:
                break
            else:
                countdownIndex -= 1
        if countdownIndex == 0:
            found = True
            break
        else:
            index += 2
if found:
    print("answer: " + str(index))
else:
    print("none found")
