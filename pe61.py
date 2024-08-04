#
# tri
# n(n + 1) / 2
#
# sqr
# n * n
#
# pen
# n(3n - 1) / 2
#
# hex 
# n(2n - 1)
#
# hept
# n(5n - 3) / 2
#
# oct
# n(3n - 2)
#

def generate4digit_numbers(func):
    nums = []
    ind = 0
    while len(str(int(func(ind)))) < 5:
        if (len(str(int(func(ind))))) == 4:
            nums.append(str(int(func(ind))))
        ind += 1

    return nums

tri = generate4digit_numbers(lambda x: x * (x + 1) / 2)
sqr = generate4digit_numbers(lambda x: x * x)
pen = generate4digit_numbers(lambda x: x * (3 * x - 1) / 2)
hex = generate4digit_numbers(lambda x: x * (2 * x - 1))
hep = generate4digit_numbers(lambda x: x * (5 * x - 3) / 2)
oct = generate4digit_numbers(lambda x: x * (3 * x - 2))

tot = [tri, sqr, pen, hex, hep, oct]

def testNext(ind, num, totalSum, nums, printValues, inds, startValue):
    if (ind == -1):
        for i in inds:
            temp = inds[:]
            temp.remove(i)
            a = testNext(i, num, totalSum, nums[:], printValues, temp[:], startValue)
            for b in a:
                if (b != -1):
                    yield b
        return

    lastDig = num[2:]
    for n in tot[ind]:
        if (n.startswith(lastDig) and n not in nums):
            nums.append(n)
            if (printValues):
                print(str(ind) + ": " + str(n))

            if (len(inds) == 0):
                lastDig = n[2:]
                if (startValue.startswith(lastDig)):
                    if (printValues):
                        print("f: " + str(startValue))
                    print("solved")
                    yield totalSum + int(startValue) + int(n)
                    return
                else:
                    yield -1
                    return
            else:
                for i in inds:
                    temp = inds[:]
                    temp.remove(i)
                    a = testNext(i, n, totalSum + int(n), [nums + [n]][:], printValues, temp[:], startValue)
                    for b in a:
                        if (b != -1):
                            yield b
            nums.remove(n)

    yield -1

for t in tri:
    for a in testNext(-1, t, 0, [t], False, [1, 2, 3, 4, 5], t):
        if (a != -1):
            print("solution: ")
            print(a)
            print("t: " + str(t))
            for b in testNext(-1, t, 0, [t], True, [1, 2, 3, 4, 5], t):
                pass
            print()

