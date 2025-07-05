from mpmath import mp

mp.dps = 150

def binary_search(target):
    lower = mp.mpf("0")
    upper = mp.mpf("100")

    while upper - lower > mp.mpf("0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"):
        mid = (lower + upper) / 2
        if mid * mid  == target:
            return mid
        elif mid * mid < target:
            lower = mid
        else:
            upper = mid
    return upper

ss = 0
for i in range(1, 101):
    if int(i**0.5)*int(i**0.5) == i:
        continue
    target = mp.mpf(str(i))
    out = binary_search(target)
    s = sum(map(int,str(out).replace(".","")[:100]))
    ss += s
print(ss)
