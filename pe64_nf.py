import math

class Number:
    def __init__(self, num_mult, num_sq, num, de_sq, de):
        self.num_mult = num_mult
        self.num_sq = num_sq
        self.num = num
        self.de_sq = de_sq
        self.de = de

    def value(self):
        return self.num_mult * (math.sqrt(self.num_sq) + self.num) / (math.sqrt(self.de_sq) + self.de)

    def inverted(self):
        if self.num_mult != 1:
            raise Exception("Warning: Nummult != 1, need to handle this case")
        return Number(1, self.de_sq, self.de, self.num_sq, self.num)

    def simplify(self):
        if self.de_sq == 0 and self.de % self.num_mult == 0:
            return Number(1, self.num_sq, self.num, self.de_sq, self.de // self.num_mult)
        else:
            raise Exception("Could not simplify")

    def __str__(self):
        return f"(sqrt({self.num_sq}) + {self.num}) / (sqrt({self.de_sq}) + {self.de})"

#a = Number(23, 0, 0, 1)
#a0 = int(a.value())
a = Number(1, 23, -4, 0, 1)
a_inv = a.inverted()
print(a_inv)
a_konj = Number(a_inv.num, a_inv.de_sq, -a_inv.de, 0, a_inv.de_sq - a_inv.de * a_inv.de)
print(a_konj)
a_konj = a_konj.simplify()
print(a_konj)
print(a_konj.value())
a0 = int(a_konj.value())

b = Number(a_konj.de, a_konj.num_sq, a_konj.num - a0 * a_konj.de, 0, a_konj.de)
b = b.simplify()
print(b)
b_inv = b.inverted()
print(b_inv)

