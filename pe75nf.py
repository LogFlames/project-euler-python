import math
from multiprocessing import Pool

# a2 + b2 == c2
# a2 == c2 - b2
# b2 == c2 - a2
#
# a + b + c == L
# a + b > c
# c < L / 2
#
# c > a
# c > b

#squares = [x * x for x in range(890)]
squares = [x * x for x in range(375001)]

print("Squares list done")

def amtOfTri(c):
    amt = 0
    c2 = c * c
    for a in range(1, int((c - 1) / 2)):
        b2 = c2 - squares[a - 1]
#        if float(b) == float(int(b)):
        if b2 in squares:
            amt += 1
            if amt >= 2:
                return 0

    return amt

p = Pool(4)
totalAmtOfTri = sum(p.map(amtOfTri, [x for x in range(1, int(1500000 / 2))]))

print(totalAmtOfTri)
