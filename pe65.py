import math

class Number:
    def __init__(self, num, de):
        self.num = num 
        self.de = de

    def __add__(self, other):
        mgm = self.de * other.de // math.gcd(self.de, other.de)
        return Number(self.num * mgm // self.de + other.num * mgm // other.de, mgm)

    def __floordiv__(self, other):
        return Number(self.num * other.de, self.de * other.num)

    def minimize(self):
        g = math.gcd(self.num, self.de)
        self.de //= g
        self.num //= g

    def __str__(self):
        return f"{self.num}/{self.de}"



def conv_sqrt_2(iters, first = True):
    if iters == 1:
        n = Number(0, 1)
    else:
        n = conv_sqrt_2(iters - 1, False)


    if first:
        n2 = n + Number(1, 1)
    else:
        n2 = Number(1, 1) // (Number(2, 1) + n)
    return n2


def conv_sqrt_23(iters, first = True):
    if iters == 1:
        n = Number(0, 1)
    else:
        n = conv_sqrt_23(iters - 1, False)


    if first:
        n2 = n + Number(4, 1)
    else:
        n2 = Number(1, 1) // (Number([1, 3, 1, 8][(iters + 3) % 4], 1) + n)
    return n2

def conv_e(iters, first = True, depth = -1):
    if iters == 1:
        n = Number(0, 1)
    else:
        n = conv_e(iters - 1, first = False, depth = depth + 1)


    if first:
        n2 = n + Number(2, 1)
    else:
        if depth % 3 == 0 or depth % 3 == 2:
            v = 1
        else:
            v = 2 * ((depth + 2) // 3)
        n2 = Number(1, 1) // (Number(v, 1) + n)
    return n2

n = conv_e(10)
print(sum(map(int, str(n.num))))
n = conv_e(100)
print(sum(map(int, str(n.num))))
