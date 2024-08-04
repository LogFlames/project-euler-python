triangles = []

for l in range(1001):
    if l == 0:
        triangles.append(0)
        continue
    count = 0
    for a in range(int((l + 2) / 3), int((l - 1) / 2) + 1):
        for b in range(round((l - a) / 2), a + 1):
            if l - a - b > b:
                continue
            c = l - a - b
            if c ** 2 + b ** 2 == a ** 2:
                count += 1
    triangles.append(count)

maxCount = [0, 0]
for index in range(len(triangles)):
    if triangles[index] > maxCount[0]:
        maxCount = [triangles[index], index]

print(maxCount)
