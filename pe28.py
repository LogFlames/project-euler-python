x = 0
counter = 0
maxCounter = 2
num = 1
totalSum = 0

while True:
  num += 1
  counter += 1
  if counter == maxCounter:
    counter = 0
    totalSum += num
    x += 1
  if x == 4:
    x = 0
    maxCounter += 2
  if num == 1001 ** 2:
    break

print(totalSum + 1)
