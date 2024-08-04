def d(n):
    int_sum = 0
    for k in range(1, int((n/2)+1)):
        if n % k == 0:
            int_sum += k

    return int_sum

total_sum = 0

for num in range(10000):
    d_num = d(num)
    if d_num != num and d(d_num) == num:
        total_sum += num

print(str(total_sum))
