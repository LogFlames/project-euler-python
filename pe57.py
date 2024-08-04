def addNumberAndFraction(a, fra):
    return (fra[0] + a * fra[1], fra[1])

def oneOver(fra):
    return (fra[1], fra[0])

numberOfBigNom = 0

for n in range(1, 1000):
    fra = (1, 2)
    for m in range(n - 1):
        fra = addNumberAndFraction(2, fra)
        fra = oneOver(fra)

    fra = addNumberAndFraction(1, fra)

    if (len(str(fra[0])) > len(str(fra[1]))):
        numberOfBigNom += 1

print(numberOfBigNom)
