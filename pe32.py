def isPandigital(a, b, c):
    usedValues = []
    for n in str(a):
        usedValues.append(int(n))
    for n in str(b):
        usedValues.append(int(n))
    for n in str(c):
        usedValues.append(int(n))

    usedValues.sort()

    if usedValues == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    return False

count = 0
sum_ = 0

savedPandigitals = []

a = 0
b = 0
while len(str(a)) <= 4:
    a += 1
    b = 0
    while len(str(a)) + len(str(b)) + len(str(a * b)) <= 9:
        b += 1
        abMult = a * b
        if isPandigital(abMult, a, b):
            if not abMult in savedPandigitals:
                count += 1
                sum_ += abMult
                savedPandigitals.append(abMult)


print("SavedPandigitals: ")
print(savedPandigitals)

print(" ")

print("Count: ")
print(count)

print(" ")

print("Sum: ")
print(sum_)
