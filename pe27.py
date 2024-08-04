import math

primeList = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,
103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,
199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,
313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,
433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,
563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,
673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,
811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,
941,947,953,967,971,977,983,991,997]
save_list = []

def isPrime(x):
    if x < 2:
        return False
    for nn in range(2, int(x / 2) + 1):
        if x % nn == 0:
            return False
    return True

for a in range(-999, 1000, 2):
    for b in primeList:
        n = 0
        count = 0
        while True:
            # "b" must be a prime since 0x0 + (some a value)x0 + b is equal to only b
            if isPrime((n * n) + (a * n) + b):
                count += 1
            else:
                break
            n += 1

        save_list.append([a, b, count, n])

maxnum = [0, 0, 0, 0]
for n in save_list:
    if n[2] > maxnum[2]:
        maxnum = n
print("A: " + str(maxnum[0]) + ", B: " + str(maxnum[1]) + ", Count (amount of primes): " + str(maxnum[2]) + ", highest N: " + str(maxnum[3]))

print("Length of save_list: " + str(len(save_list)))

print("answer: " + str(maxnum[0] * maxnum[1]))
