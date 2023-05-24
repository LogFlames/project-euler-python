##
#
# Project Euler 72
# https://projecteuler.net/problem=72
# By: Elias Lundell
#
##

import math

def primes_under_n(n):
    primes = [2]
    pot_primes = [x for x in range(3, n, 2)]
    sqrt_n = math.sqrt(n)

    selected = 0

    while pot_primes[selected] < sqrt_n:
        if pot_primes[selected] == -1:
            selected += 1
            continue
        primes.append(pot_primes[selected])
        m = pot_primes[selected]
        for i in range(selected + m, len(pot_primes), m):
            pot_primes[i] = -1

        selected += 1

    for i in range(selected, len(pot_primes)):
        if pot_primes[i] != -1:
            primes.append(pot_primes[i])

    return primes

primes = primes_under_n(1000000 // 2 + 1)

def prime_factorize(n):
    factors = []
    sqrt_n = math.sqrt(n)
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
            n //= prime
        while n % prime == 0:
            n //= prime
        if n == 1:
            break
        if prime > sqrt_n:
            factors.append(n)
            break
    return factors

def totient(n):
    primesDiv = prime_factorize(n)
    # The number times (1 - 1 / p) for all it's distincte prime factors
    # Expl
    # We start with n numbers smaller than n
    # Then if we have a factor p, every p number is not coprime (n / p), aka we multiply with (1 - 1 / p) as we have everything but those n * (1 / p) left
    prod = n
    for fact in primesDiv:
        prod *= (fact - 1) / fact
    return int(prod)

sum_ = 0

for d in range(2, 1000001):
    sum_ += totient(d)

print(sum_)
