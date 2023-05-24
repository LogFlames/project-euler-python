def generate_primes(n):
    n_sqrt = n ** 0.5
    pot_primes = [i for i in range(3, n, 2)]

    primes = [2]

    ind = 0
    while pot_primes[ind] < n_sqrt:
        if pot_primes[ind] == -1:
            ind += 1
            continue

        primes.append(pot_primes[ind])
        for m in range(ind + pot_primes[ind], len(pot_primes), pot_primes[ind]):
            pot_primes[m] = -1

        ind += 1

    for i in range(ind, len(pot_primes)):
        if pot_primes[i] != -1:
            primes.append(pot_primes[i])

    return primes

# print([x for x in range(2, 101) if not sum([x % y == 0 for y in range(2, x)])])

primes = generate_primes(10_000_000)




