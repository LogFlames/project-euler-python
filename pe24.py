import itertools

count = 0
for n in itertools.permutations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 10):
    count += 1
    if count == 1000000:
        answ = ""
        for k in n:
            answ += k
        print(answ)
        break
