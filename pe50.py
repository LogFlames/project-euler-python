import math

def primeCheck(n):
    for p in primeList:
        if n % p == 0:
            return False
        if p > math.sqrt(n):
            primeList.append(n)
            return True
    return True

primeList = [2, 3, 5]

def seriesGen():
    summ = 0
    leng = 0
    maxLeng = 0
    ans = 0
    for j in range(len(primeList)):
        if primeList[j] * maxLeng > 1000000:
            break
        for k in range(len(primeList)):
            summ = sum(primeList[j:k])
            if summ in primeList:
                leng = k - j
                if leng > maxLeng:
                    maxLeng = leng
                    print("New record: " + str(ans))
                    ans = summ
            if (summ >= 1000000):
                break

    print("ans: " + str(ans))
    print("leng: " + str(leng))

def main():
    for n in range(7, 1000000, 2):
        if n % 5 != 0:
            primeCheck(n)

    maxLength = 0
    ans = 0
    seriesGen()

if __name__ == "__main__":
	main()
