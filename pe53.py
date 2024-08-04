import math

count = 0

for n in range(1, 101):
    for r in range(1, n + 1):
        combinatorics = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
        if combinatorics > 1e6:
            count += 1

print(count)
