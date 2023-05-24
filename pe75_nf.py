##
#
# Project Euler 75
# https://projecteuler.net/problem=75
# By: Elias Lundell
#
##

import math

upper_length_limit = 1500000
upper_length_limit = 100000
# upper_length_limit = 50

t1 = []
t2 = []

# @profile
def main1():
    count = 0

    squares = []
    for i in range(upper_length_limit + 1):
        squares.append(i * i)

    for l in range(2, upper_length_limit + 1, 2):
        if l % 1000 == 0:
            print("{:.4f} %".format(l / upper_length_limit * 100))

        triangles = 0
        abs = []
        l2 = squares[l]
        a = 1
        upper_limit = l // 2
        while a < upper_limit:
            c1 = l2 - 2 * l * a + 2 * squares[a]
            c2 = 2 * (l - a)

            if c1 % c2 == 0:
                triangles += 1
                b = l - c1 / c2
                ab = [min(a, b), max(a, b)]
                if ab in abs:
                    print(ab)
                abs.append(ab)

                if l == 910:
                    print(a, l - c1 / c2 - a, c1 / c2)

                if triangles >= 2:
                    break

                c = c1 // c2
                ab = l - c
                upper_limit = int(ab / 2 + 2) + c // 2

                # if upper_limit > ab - a:
                    # break

                # if l == 210:
                #     print(upper_limit)

            a += 1

        if triangles == 1:
            t1.append(l)
            count += 1


    print(count)

##################################################

# @profile
def main2():
    triangles = {}
    for i in range(2, upper_length_limit + 1, 2):
        triangles[i] = 0

    for c in range(1, upper_length_limit // 2):
        if c % 100 == 0:
            print("{:.2f}%".format(c / (upper_length_limit // 2) * 100))
        c2 = c * c
        a = 3
        upper_limit = c
        while a < upper_limit:
            b = math.sqrt(c2 - a * a)
            if a > b:
                break
            l = a + b + c
            if l > upper_length_limit:
                break
            elif b.is_integer():
                triangles[l] += 1
                
                # if l == 12:
                    # print("Found, a: {}, b: {}, c: {}".format(a, b, c))

            a += 1

    for a in triangles.keys():
        if triangles[a] == 1:
            t2.append(a)
    print(list(triangles.values()).count(1))

if __name__ == "__main__":
    main1()
    main2()

    print("Elements from main1 not in main2: " + str(list(filter(None, map(lambda x: None if x in t2 else x, t1)))))
    print("Elements from main2 not in main1: " + str(list(filter(None, map(lambda x: None if x in t1 else x, t2)))))

