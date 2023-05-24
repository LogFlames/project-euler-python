##
#
# Project Euler 78
# https://projecteuler.net/problem=78
# By: Elias Lundell
#
##

ans = {}

def p(n):
    if n in ans:
        return ans[n]
    sum_ = 1
    for m in range(1, n):
        sum_ += p(m) + p(n - m)
    ans[n] = sum_
    return sum_

print(p(5))
