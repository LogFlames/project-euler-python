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

primes = generate_primes(1000000)
primes = {*map(str, primes)}

pp = {}
for p1 in primes:
    for p2 in primes:
        if p1 >= p2:
            continue

        if p1 + p2 in primes and p2 + p1 in primes:
            if p1 not in pp:
                pp[p1] = []
            if p2 not in pp:
                pp[p2] = []
            pp[p1].append(p2)
            pp[p2].append(p1)

ppp = {}

for p in pp:
    if len(pp[p]) >= 3:
        ppp[p] = pp[p]

print(ppp)
print([*ppp])




