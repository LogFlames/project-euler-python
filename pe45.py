import math

def TT(x):
    n = -0.5 + math.sqrt(0.25 + 2*x)
    if n - round(n) == 0:
        return n
    else:
        return -1

def PT(x):
    n = 1.0/6.0 + math.sqrt(1.0/36.0 + 2.0 * x/3)
    if n - round(n) == 0:
        return n
    else:
        return -1

#T n(n+1)/2
#P n(3n-1)/2
#H n(2n-1)

hn = 143
tn = - 1

while tn < 0:
    hn += 1
    x = hn * (2 * hn - 1)
    if PT(x) > 0 and TT(x) > 0:
        tn = TT(x)
print (int(tn*(tn+1)/2))
