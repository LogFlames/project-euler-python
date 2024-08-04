import math

N = 10

pot = list(range(2, N + 1))
num = [0] * (N - 1)

for i, p in enumerate(pot):
    for j in range(i, len(pot), p):
        num[j] += 1

print(pot)
print(num)

print([pot[i] - num[i] for i in range(len(pot))])


maximum_relative_tot = 0
maximum_n = None
for n in range(2, 1000000 + 1):
    num_rel_prim = 0
    for j in range(1,n):
        if math.gcd(n, j) == 1:
            num_rel_prim += 1
    if n / num_rel_prim > maximum_relative_tot:
        maximum_relative_tot = n / num_rel_prim
        maximum_n = n

print(maximum_n)
