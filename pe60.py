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

primes = generate_primes(10**6)
#print(f"{len(primes) = }")
primes_check = {*primes}
primes_strs = [*map(str, primes)]

rev_lookup = {str(primes[ind]): ind for ind in range(len(primes))}
#print(rev_lookup)

def is_prime(num):
    global primes
    global primes_check
    num = int(num)
    if num > primes[-1]:
        ip = True
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                ip = False
                break
        return ip
    return num in primes_check

dp = {}

def check_pair(p1, p2):
    r1, r2 = rev_lookup[p1], rev_lookup[p2]
    i1, i2 = min(r1, r2), max(r1, r2)
    tup = (i1, i2)
    if tup in dp:
        return dp[tup]
    res = is_prime(p1 + p2) and is_prime(p2 + p1)
    dp[tup] = res
    return res

count = 0

def check_pair_i(r1, r2):
    i1, i2 = min(r1, r2), max(r1, r2)
    tup = (i1, i2)
    if tup in dp:
        return dp[tup]
    res = is_prime(primes_strs[i1] + primes_strs[i2]) and is_prime(primes_strs[i2] + primes_strs[i1])
    dp[tup] = res
    return res

def check(a, b, smallest_sum_yet):
    workes_with_a_and_b = []

    ai = rev_lookup[a]
    bi = rev_lookup[b]
    for ind in range(ai + 1, len(primes)):
        if primes[ind] > smallest_sum_yet:
            break
        if check_pair_i(ai, ind) and check_pair_i(bi, ind):
            workes_with_a_and_b.append(primes_strs[ind])

    workes_with_a_and_b.sort(key = lambda x: int(x))


#    print(f"{len(workes_with_a_and_b) = }")

    pairs = []

    for i, p1 in enumerate(workes_with_a_and_b):
        for p2 in workes_with_a_and_b[i + 1:]:
            if int(p1) + int(p2) < smallest_sum_yet and check_pair(p1, p2):
                pairs.append(sorted([p1, p2]))

#    print(f"{len(pairs) = }")

    overlapping_trips = []


    for pp1 in pairs:
        for pp2 in pairs:
            if pp1[0] == pp2[0] and int(pp1[0]) + int(pp1[1]) + int(pp2[1]) < smallest_sum_yet and check_pair(pp1[1], pp2[1]):
                overlapping_trips.append({*pp1, *pp2})
            if pp1[0] == pp2[1] and int(pp1[0]) + int(pp1[1]) + int(pp2[0]) < smallest_sum_yet and check_pair(pp1[1], pp2[0]):
                overlapping_trips.append({*pp1, *pp2})
            if pp1[1] == pp2[0] and int(pp1[0]) + int(pp1[1]) + int(pp2[1]) < smallest_sum_yet and check_pair(pp1[0], pp2[1]):
                overlapping_trips.append({*pp1, *pp2})
            if pp1[1] == pp2[1] and int(pp1[0]) + int(pp1[1]) + int(pp2[0]) < smallest_sum_yet and check_pair(pp1[0], pp2[0]):
                overlapping_trips.append({*pp1, *pp2})

#    print(overlapping_trips)
#    print(f"{len(overlapping_trips) = }")

    smallest_sum = None
    ssop = None
    for op in overlapping_trips:
        s = sum(map(int, op))
        if smallest_sum is None or s < smallest_sum:
            smallest_sum = s
            ssop = op

    if smallest_sum is None:
        return 10**99

    print(f"sum({ssop | {a, b}}) = {smallest_sum + int(a) + int(b)}")

    return smallest_sum + int(a) + int(b)

smallest_sum_yet = 10**99
for p in primes:
    print(f"{p}          ", end = "\r")
    if p * 4 > smallest_sum_yet:
        break
    for p2 in primes:
        if p2 > p:
            break

        if check_pair(str(p), str(p2)):
#            print(f"{p} {p2}           ", end = "\r")
            ss = check(str(p), str(p2), smallest_sum_yet)
            if ss < smallest_sum_yet:
                smallest_sum_yet = ss

print(smallest_sum_yet)
