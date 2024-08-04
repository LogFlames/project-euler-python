# 1p, 2p, 5p, 10p, 20p, 50, 100p, 200p

ans = 0

def calcSum(k1, k2, k5, k10, k20, k50, k100, k200):
    return 1 * k1 + 2 * k2 + 5 * k5 + 10 * k10 + 20 * k20 + 50 * k50 + 100 * k100 + 200 * k200

for k200 in range(0, 2):
    if calcSum(0, 0, 0, 0, 0, 0, 0, k200) > 200:
        break
    for k100 in range(0, 3):
        if calcSum(0, 0, 0, 0, 0, 0, k100, k200) > 200:
            break
        for k50 in range(0, 5):
            if calcSum(0, 0, 0, 0, 0, k50, k100, k200) > 200:
                break
            for k20 in range(0, 11):
                if calcSum(0, 0, 0, 0, k20, k50, k100, k200) > 200:
                    break
                for k10 in range(0, 21):
                    if calcSum(0, 0, 0, k10, k20, k50, k100, k200) > 200:
                        break
                    for k5 in range(0, 41):
                        if calcSum(0, 0, k5, k10, k20, k50, k100, k200) > 200:
                            break
                        for k2 in range(0, 101):
                            if calcSum(0, k2, k5, k10, k20, k50, k100, k200) > 200:
                                break
                            for k1 in range(0, 201):
                                if calcSum(k1, k2, k5, k10, k20, k50, k100, k200) == 200:
                                    ans += 1
                                    break

                                #print(str(k200) + " " + str(k100) + " " + str(k50) + " " +
                                #str(k20) + " " + str(k10) + " " + str(k5) + " " + str(k2) + " " + str(k1))

print(ans)
