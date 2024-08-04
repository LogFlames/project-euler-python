number = ""
a = 0

while len(number) <= 1000000:
    a += 1
    number += str(a)

answ = 1
div = 1
for n in range(len(number)):
    if (n + 1) % div == 0:
        answ *= int(number[n])
        div *= 10

print answ
