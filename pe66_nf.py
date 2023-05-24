##
#
# Project Euler 66
# https://projecteuler.net/problem=66
# By: Elias Lundell
#
##

# Didnt work, obviously
# Some thoughts:
    # can a - b = 1 if a and b are not coprime, I think not, will need to prove
    # If so, construct "possible" x:s by using factors not found in D

def find_x(D):
    if float(int(D ** 0.5)) == float(D ** 0.5):
        return -1
    x = 1
    while True:
        part1 = x * x - 1
        if part1 % D != 0:
            if D % 2 == 0:
                x += 2
            else:
                x += 1
            continue
        y = ((x * x - 1) // D) ** 0.5
        if float(int(y)) == float(y) and y != 0:
            print("{} done".format(D))
            return x
        else:
            if D % 2 == 0:
                x += 2
            else:
                x += 1

x_sols = list(map(find_x, range(2, 1001)))
print(x_sols)
print(max(x_sols))

