import math

def generatePT():
    num = 0
    while True:
        num += 1
        yield num * (3 * num - 1) / 2.0

def isP(x):
    n = 1.0 / 6.0 + math.sqrt(1.0 / 36.0 + 2.0 * x / 3.0)
    if n == round(n):
        return True
    return False

exit = False

for a in generatePT():
    if exit:
        break
    for b in generatePT():
        if b > a:
            break
        if isP(a - b) and isP(a + b):
            print(int(a - b))
            exit = True
