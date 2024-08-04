counted = range(10000001)
print(counted)
count = 0

for n in range(1, 10000001):
    if n % 1000000 == 0:
        print(n)
    N_counted = []
    while n != 89 and n != 1:
        N_counted.append(n)
        digit_sum = 0
        for digit in str(n):
            digit_sum += int(digit)**2
        n = digit_sum
        if counted[n] == -1:
            n = 89
        elif counted[n] == -2:
            n = 1
    if n == 89:
        for k in N_counted:
            counted[k] = -1
        count += 1
    else:
        for k in N_counted:
            counted[k] = -2
print(count)
