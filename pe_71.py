##
#
# Project Euler 71
# https://projecteuler.net/problem=71
# By: Elias Lundell
# 
# #


curN = 2
curD = 5

def gcd(a, b):
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
        if r == 0:
            return b

for d in range(1000000):
    # We can start at curN as we know that d is bigger and we are looking for a slightely bigger value than we have right now, c cannot be smaller than the last saved c
    for c in range(curN, d):
        if c == 3 and d == 7:
            continue
        if gcd(d, c) == 1:
            if c / d <= 3 / 7:
                if curD == -1 or curN == -1:
                    curD = d
                    curN = c
                else:
                    if c / d > curN / curD:
                        curD = d
                        curN = c
            else:
                break

print(curN)
