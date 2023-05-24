##
#
# Project Euler 74
# https://projecteuler.net/problem=74
# By: Elias Lundell
#
##

from multiprocessing import Pool

prefac = {"0": 1, "1": 1, "2": 2, "3": 6, "4": 24, "5": 120, "6": 720, "7": 5040, "8": 40320, "9": 362880}

def chain_length(n):
    chain = {n}
    new = n
    while True:
        clen = len(chain)
        new = sum(map(lambda m: prefac[m], str(new)))
        if new in chain or clen > 60:
            return clen
        else:
            chain.add(new)

p = Pool(12)

chain_lengths = p.map(chain_length, [x for x in range(1, 1000001)])

print(chain_lengths.count(60))

