import itertools

sum_ = 0

def undoList(listToUndo):
    returnString = ""
    for s in listToUndo:
        returnString += s
    return returnString

for n in itertools.permutations("0123456789", 10):
    n = undoList(n)
    possible = True
    if not int(n[1] + n[2] + n[3]) % 2 == 0:
        possible = False
    if not int(n[2] + n[3] + n[4]) % 3 == 0:
        possible = False
    if not int(n[3] + n[4] + n[5]) % 5 == 0:
        possible = False
    if not int(n[4] + n[5] + n[6]) % 7 == 0:
        possible = False
    if not int(n[5] + n[6] + n[7]) % 11 == 0:
        possible = False
    if not int(n[6] + n[7] + n[8]) % 13 == 0:
        possible = False
    if not int(n[7] + n[8] + n[9]) % 17 == 0:
        possible = False

    if possible:
        sum_ += int(n)

print(sum_)
