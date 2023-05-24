##
#
# Project Euler 91
# https://projecteuler.net/problem=91
# By: Elias Lundell
#
##

import math

count = 0

limit = 50

for x1 in range(0, limit + 1):
    for y1 in range(0, limit + 1):
        if x1 == 0 and y1 == 0:
            continue
        for x2 in range(x1, limit + 1):
            for y2 in range(0, limit + 1):
                if x1 == x2 and y2 <= y1:
                    continue

                d1_2 = x1 * x1 + y1 * y1
                d2_2 = x2 * x2 + y2 * y2
                d3_2 = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)

                if d1_2 + d2_2 == d3_2 or d2_2 + d3_2 == d1_2 or d1_2 + d3_2 == d2_2:
                    count += 1

print(count)



