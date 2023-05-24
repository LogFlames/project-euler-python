##
#
# Project Euler 94
# https://projecteuler.net/problem=94
# By: Elias Lundell
#
##

import math

perimi = 0

"""
s1 = 0
n = 3

while s1 < 1000000000 // 3 + 1:
    i = n * n
    n += 1
    # (3/4)s1^2 + 2 * s1 + 1 = i
    # (3/4)s1^2 + 2 * s1 - (i - 1) = 0
    # s1 = (-2 + math.sqrt(4 - 4 * (3 / 4) * (i - 1))) / (2 * (3 / 4))
    # s1 = (-2+math.sqrt(4-3*(i-1)))/(3/2)
    s1 = 2 * (-2 + math.sqrt(4 + 3 * (i - 1))) / 3
    if s1 - int(s1) == 0:
        if s1 * 3 + 2 < 1000000000:
            perimi += s1 * 3 + 2

    s1 = 2 * (2 + math.sqrt(4 + 3 * (i - 1))) / 3
    if s1 - int(s1) == 0:
        if s1 * 3 - 2 < 1000000000: 
            perimi += s1 * 3 - 2

print(perimi)
exit()
"""


for a in range(3, 1000000000 // 3 + 3):
    if a % 3333334 == 0:
        print("{}%".format(int(1000 * a / (1000000000 // 3 + 3)) / 10))

    a_2 = a * a
    if 3 * a + 2 < 1000000000:
        sqrt1 = math.sqrt(3 * a_2 / 4 + 2 * a + 1)
        if sqrt1 - int(sqrt1) == 0:
            perimi += 3 * a + 2

    if 3 * a - 2 < 1000000000:
        sqrt2 = math.sqrt(3 * a_2 / 4 - 2 * a + 1)
        if sqrt2 - int(sqrt2) == 0:
            perimi += 3 * a - 2

print(perimi)


