from os import path

row = [0]

code_path = path.dirname(__file__)

with open(path.join(code_path, "external_files/pe18_pyramid.txt"), "r") as f:
    for n in f:
        nextrow = []
        nextnumber = ""
        for char in n:
            if char == "." or char == "\n":
                nextrow.append(int(nextnumber))
                nextnumber = ""
            else:
                nextnumber += char
        zero = [0]
        for number in row:
            zero.append(number)
        row = zero
        row.append(0)

        newrow = nextrow
        for k in range(0, len(nextrow)):
            if row[k] > row[k+1]:
                newrow[k] = row[k] + nextrow[k]
            else:
                newrow[k] = row[k+1] + nextrow[k]
        row = newrow
    biggest = 0
    for n in row:
        if n > biggest:
            biggest = n
print(biggest)
