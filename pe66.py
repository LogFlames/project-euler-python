# -*- coding: utf-8 -*-

sqrs = [0, 1, 4, 9]
def is_square(n):
    if float(n) == float(int(n)):
        n = int(n)
    else:
        return False
    if sqrs[len(sqrs) - 1] < n:
        for a in range(len(sqrs), n + 1):
            sqrs.append(a * a)
    return n in sqrs

biggestX = -1
saveD = -1

for D in range(2, 1001):
    if is_square(D):
        continue

    x = 2
    while True:
        if is_square((x * x - 1) / D):
            if x > biggestX:
                biggestX = x
                saveD = D
            break
        x += 1

print(saveD)
print(biggestX)
