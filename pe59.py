import itertools

data = []

letters = "abcdefghijklmnopqrstuvwxyz"

with open("external_files/pe59_chiper.txt", "r") as f:
    for line in f:
        line = line.strip()
        data.append(int(line))

for key in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3):
    message = ""
    for index, letter in enumerate(data):
        index %= 3
        message += chr(letter ^ ord(key[index]))

    if " the " in message and " and " in message:
        print(message)
        summ = sum(list(map(ord, message)))
        print("ascii sum: " + str(summ))
        break
