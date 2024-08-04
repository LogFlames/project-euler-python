highest = 0

for a in range(1, 100):
    for b in range(1, 100):
        a_pow_b = a**b
        a_pow_b_list = list(str(a_pow_b))
        int_list = map(int, a_pow_b_list)
        if sum(int_list) > highest:
            highest = sum(int_list)

print highest
