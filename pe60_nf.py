import math

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


length = 7
num_matches = 4

primes = generate_primes(10**length)
primes_check = {*primes}

pp = {}
for i, p1 in enumerate(primes):
    if i % 1000 == 0:
        print(f"{i} / {len(primes)}")

    if int(math.log10(p1)) == length:
        break
    for j, p2 in enumerate(primes):
        if j >= i:
            break

        if p1 * 10**(int(math.log10(p2)) + 1) + p2 in primes_check and p2 * 10**(int(math.log10(p1)) + 1) + p1 in primes_check:
            if p1 not in pp:
                pp[p1] = []
            if p2 not in pp:
                pp[p2] = []
            pp[p1].append(p2)
            pp[p2].append(p1)

ppp = {}


print("Sorting out the ones with too few connections...")

for p in pp:
    if len(pp[p]) >= num_matches - 1:
        ppp[p] = pp[p]


print("Sorting out the ones with too few connections... Done")
print("Finding all triangles of primes...")
trigs = []
for p in ppp:
    for p2 in ppp[p]:
        for p3 in ppp[p]:
            if p2 == p3:
                continue
            if p2 in ppp and p3 in ppp and p3 in ppp[p2] and p2 in ppp[p3]:
                trigs.append([p, p2, p3])

print("Finding all triangles of primes... Done")
print("Finding all four-sets of primes...")

fours = []
for t1 in trigs:
    for p in ppp:
        if p in t1:
            continue
        if t1[0] in ppp[p] and t1[1] in ppp[p] and t1[2] in ppp[p]:
            fours.append([p, *t1])

print("Finding all four-sets of primes... Done")
print("Finding all five-sets of primes...")

fives = []
for f1 in fours:
    for p in ppp:
        if p in f1:
            continue
        if f1[0] in ppp[p] and f1[1] in ppp[p] and f1[2] in ppp[p] and f1[3] in ppp[p]:
            fives.append([p, *f1])

print("Finding all five-sets of primes... Done")

ss = -1
for f in fives:
    s = sum(map(int, f))
    if ss == -1 or s < ss:
        ss = s

print(ss)
print(fives)
