##
#
# Project Euler 100
# https://projecteuler.net/problem=100
# By: Elias Lundell
#
##

import math

def get_blue(tot):
    val = tot * (tot - 1) // 2
    blue = math.ceil(math.sqrt(val))
    if blue * (blue - 1) == val:
        return blue
    return -1

tot = 1000000000000
blue = get_blue(tot)

while blue == -1:
    tot += 1
    blue = get_blue(tot)

print(blue)
